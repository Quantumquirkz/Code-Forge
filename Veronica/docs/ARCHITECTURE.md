# Veronica Architecture Deep Dive

This document provides a technical architecture overview of the current backend/frontend implementation and the intended evolution path.

---

## 1) Architectural Principles

1. **Safety first:** side-effectful actions require explicit user confirmation.
2. **Modularity:** orchestration, protocol handling, policy, and tools remain separable.
3. **Observability-ready:** request IDs and explicit audit events support traceability.
4. **Evolvability:** domain model introduction enables personalization and multi-tenant extensions.

---

## 2) Backend Component Map

```mermaid
flowchart TB
  subgraph API[FastAPI Layer]
    E[endpoints.py]
    M[middleware.py]
    H[chat_handler.py]
  end

  subgraph ORCH[Orchestration]
    O[AgentOrchestrator]
    CE[ContextEnricher]
    MR[MemoryRecorder]
  end

  subgraph POLICY[Policy & Governance]
    AG[ActionGuard]
    CF[Confirmation Handler]
    AL[Audit Logger]
  end

  subgraph STATE[State & Memory]
    SS[SessionStore]
    MM[MemoryManager\nChromaDB]
    DM[Domain Models]
  end

  subgraph TOOLS[Tools]
    TB[Tool Registry]
    BS[BlockchainService]
    VT[Voice/Vision Processors]
  end

  E --> H
  E --> M
  H --> AG
  H --> CF
  H --> O
  H --> SS
  O --> CE
  O --> MR
  CE --> MM
  MR --> MM
  CF --> AL
  AG --> TB
  TB --> BS
  E --> VT
  E --> DM
```

---

## 3) Conversation Lifecycle

```mermaid
stateDiagram-v2
  [*] --> ReceiveFrame
  ReceiveFrame --> ValidatePayload
  ValidatePayload --> Invalid: malformed payload
  Invalid --> SendError
  SendError --> [*]

  ValidatePayload --> CheckPending
  CheckPending --> HandleConfirm: confirm/cancel command
  HandleConfirm --> EmitChunkEnd
  EmitChunkEnd --> [*]

  CheckPending --> EvaluatePolicy
  EvaluatePolicy --> RequireApproval: sensitive intent detected
  RequireApproval --> EmitApprovalMessage
  EmitApprovalMessage --> [*]

  EvaluatePolicy --> GenerateModelResponse: no policy intervention
  GenerateModelResponse --> StreamChunks
  StreamChunks --> PersistTurn
  PersistTurn --> EmitEnd
  EmitEnd --> [*]
```

---

## 4) Data and State Boundaries

## Session state (process-local)
- Conversation history for each websocket session.
- Optional pending action for confirmation flow.

## Long-term memory (vector DB)
- Persistent memory snippets queried for context enrichment.
- Current implementation is global, to be upgraded to tenant-scoped namespaces.

## Audit trail
- Local JSONL records of confirmed/cancelled sensitive actions.
- Planned evolution: centralized append-only audit sink.

---

## 5) Deployment Perspective

```mermaid
flowchart LR
  Browser[Next.js Client] --> Backend[FastAPI Service]
  Backend --> Chroma[(ChromaDB Storage)]
  Backend --> LLM[LLM Provider APIs]
  Backend --> Eleven[ElevenLabs API]
  Backend --> RPC[Blockchain RPC Provider]
```

### Production recommendations
- Place API behind reverse proxy with TLS termination.
- Externalize session state to Redis (or equivalent) before horizontal scaling.
- Use managed secret store for API keys.
- Add OpenTelemetry for traces and metrics.

---

## 6) Known Design Trade-offs

1. **Regex-based policy detection** is simple but brittle for natural language variance.
2. **Process-local session state** is fast for prototype but not multi-instance safe.
3. **Simulation-based tools** reduce risk during development but limit real-world utility.
4. **Single-service architecture** simplifies early velocity but constrains independent scaling.
