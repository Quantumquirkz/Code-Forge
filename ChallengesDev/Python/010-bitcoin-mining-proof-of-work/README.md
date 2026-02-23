# Challenge 010: Bitcoin Mining Proof-of-Work

## Problem Description
Simulate the **Proof-of-Work (PoW)** mechanism used in Bitcoin. The goal is to find a number called a `nonce` that, when concatenated with block data and processed with the `SHA-256` hashing algorithm, produces a hash that starts with a specific number of zeros (referred to as `difficulty`).

## Input and Output Format
- **Input**: 
  - `block_data` (str): The information contained in the block.
  - `difficulty` (int): The number of leading zeros required in the hexadecimal hash.
- **Output**: A tuple `(nonce, hash_result)` where `nonce` is the number found and `hash_result` is the valid hash.

## Constraints and Edge Cases
- The `nonce` must be a non-negative integer starting from 0.
- Difficulty typically ranges between 1 and 5 for this challenge (more than 6 can take a long time on a normal CPU).
- Use the standard `hashlib` library.

## Usage Example
```python
block_data = "Transaction: A pays B 10 BTC"
difficulty = 4
# The program will look for a nonce such that sha256(block_data + str(nonce)) starts with "0000"
```

## Key Concepts
- **Cryptographic Hashing**: One-way functions that transform data into a fixed-length string.
- **Brute Force**: The only way to find the `nonce` is by trying one by one.
- **Difficulty**: Increasing difficulty exponentially increases the required computation time.
