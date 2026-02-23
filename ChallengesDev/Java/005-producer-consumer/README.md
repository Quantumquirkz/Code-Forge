# Reto 005: Producer-Consumer Pattern

## Descripción del Problema
Implementa el patrón de diseño **Productor-Consumidor** utilizando una `BlockingQueue` personalizada o una existente. El objetivo es que uno o más hilos "productores" generen datos y los coloquen en una cola con capacidad limitada, mientras que uno o más hilos "consumidores" retiren esos datos para procesarlos. El sistema debe manejar correctamente situaciones donde la cola esté llena (productores esperan) o vacía (consumidores esperan).

## Formato de Entrada y Salida
- **Clases**:
  - `Producer`: Un hilo que produce enteros.
  - `Consumer`: Un hilo que consume enteros.
  - `DataBuffer`: La estructura que actúa como cola sincronizada.

## Restricciones y Casos Borde
- Capacidad máxima de la cola.
- Manejo de interrupciones de hilos.
- Señalización de fin de producción (veneno/poison pill).

## Ejemplo de Uso
```java
DataBuffer<Integer> buffer = new DataBuffer<>(5);
Thread producer = new Thread(new Producer(buffer));
Thread consumer = new Thread(new Consumer(buffer));
```

## Conceptos Clave
- **Synchronization**: Uso de `wait()` y `notifyAll()` o `Condition`.
- **Inter-thread Communication**: Intercambio de datos seguro entre hilos.
- **Backpressure**: Qué sucede cuando la producción es más rápida que el consumo.
