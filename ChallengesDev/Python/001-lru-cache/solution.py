"""
Solution to Challenge 001: LRU Cache
Optimized implementation using a Dictionary and a Doubly Linked List.
"""

class Node:
    """Node for the doubly linked list."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    LRU Cache with O(1) operations.
    Uses a hash map for direct node access and a doubly linked list
    to maintain the usage order.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        
        # Sentinel nodes (facilitates list manipulation)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Removes a node from the linked list."""
        prev = node.prev
        new_next = node.next
        prev.next = new_next
        new_next.prev = prev

    def _add(self, node):
        """Adds a node right after the head (recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """
        Gets the value of the key.
        If it exists, moves the node to the front.
        Time Complexity: O(1)
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates a value.
        If capacity is exceeded, removes the node before the tail (LRU).
        Time Complexity: O(1)
        """
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        
        if len(self.cache) > self.capacity:
            # Remove the LRU (node before tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

# --- Complexity Analysis ---
# Time:
#   - get(key): O(1) - Dictionary access and pointer rearrangement.
#   - put(key, value): O(1) - Dictionary insertion and pointer manipulation.
# Space:
#   - O(Capacity): We store 'capacity' nodes in the dictionary and the list.
