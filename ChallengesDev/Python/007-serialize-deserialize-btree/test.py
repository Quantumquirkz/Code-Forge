import unittest
from solucion import Codec, TreeNode

class TestCodec(unittest.TestCase):
    def test_basic_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        
        codec = Codec()
        serialized = codec.serialize(root)
        deserialized = codec.deserialize(serialized)
        
        self.assertEqual(deserialized.val, 1)
        self.assertEqual(deserialized.left.val, 2)
        self.assertEqual(deserialized.right.val, 3)
        self.assertEqual(deserialized.right.left.val, 4)
        self.assertEqual(deserialized.right.right.val, 5)

    def test_empty_tree(self):
        codec = Codec()
        self.assertEqual(codec.serialize(None), "")
        self.assertIsNone(codec.deserialize(""))

    def test_single_node(self):
        root = TreeNode(1)
        codec = Codec()
        serialized = codec.serialize(root)
        self.assertEqual(codec.deserialize(serialized).val, 1)

if __name__ == '__main__':
    unittest.main()
