from collections import deque
from typing import Optional

class TreeNode:
    """Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """Implementation of serialization and deserialization using BFS."""

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encapsulates a tree into a single string."""
        if not root:
            return ""
            
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
                
        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes the serialized string back to a tree."""
        if not data:
            return None
            
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1
        
        while queue and index < len(values):
            node = queue.popleft()
            
            # Left side
            if values[index] != "None":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1
            
            # Right side
            if index < len(values) and values[index] != "None":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1
            
        return root

# --- Complexity Analysis ---
# Time: O(N) for serialize and deserialize.
# Space: O(N) to store values and the processing queue.
