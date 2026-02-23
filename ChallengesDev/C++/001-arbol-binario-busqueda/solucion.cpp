#include <iostream>

/**
 * Solution to Challenge 001: Binary Search Tree (BST)
 * Efficient implementation of insertion, search, and deletion.
 */

struct Node {
    int key;
    Node *left, *right;
    Node(int item) : key(item), left(nullptr), right(nullptr) {}
};

class BST {
public:
    BST() : root(nullptr) {}

    void insert(int key) {
        root = insertRec(root, key);
    }

    bool search(int key) {
        return searchRec(root, key);
    }

    void remove(int key) {
        root = deleteNode(root, key);
    }

    // Time Complexity Analysis:
    // - Search: O(h) where h is the tree height.
    // - Insertion: O(h)
    // - Deletion: O(h)
    // In a balanced tree h = log(n), in the worst case h = n.

private:
    Node* root;

    Node* insertRec(Node* node, int key) {
        if (node == nullptr) return new Node(key);
        if (key < node->key)
            node->left = insertRec(node->left, key);
        else if (key > node->key)
            node->right = insertRec(node->right, key);
        return node;
    }

    bool searchRec(Node* node, int key) {
        if (node == nullptr) return false;
        if (node->key == key) return true;
        if (key < node->key) return searchRec(node->left, key);
        return searchRec(node->right, key);
    }

    Node* minValueNode(Node* node) {
        Node* current = node;
        while (current && current->left != nullptr)
            current = current->left;
        return current;
    }

    Node* deleteNode(Node* root, int key) {
        if (root == nullptr) return root;

        if (key < root->key)
            root->left = deleteNode(root->left, key);
        else if (key > root->key)
            root->right = deleteNode(root->right, key);
        else {
            // Node with only one child or no child
            if (root->left == nullptr) {
                Node* temp = root->right;
                delete root;
                return temp;
            } else if (root->right == nullptr) {
                Node* temp = root->left;
                delete root;
                return temp;
            }

            // Node with two children: get in-order successor (the smallest on the right)
            Node* temp = minValueNode(root->right);
            root->key = temp->key;
            root->right = deleteNode(root->right, temp->key);
        }
        return root;
    }
};
