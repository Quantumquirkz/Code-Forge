#include <iostream>

enum Color { RED, BLACK };

struct Node {
    int data;
    Color color;
    Node *left, *right, *parent;

    Node(int data) : data(data), color(RED), left(nullptr), right(nullptr), parent(nullptr) {}
};

class RedBlackTree {
private:
    Node *root;

protected:
    void rotateLeft(Node *&root, Node *&x) {
        Node *y = x->right;
        x->right = y->left;
        if (x->right != nullptr) x->right->parent = x;
        y->parent = x->parent;
        if (x->parent == nullptr) root = y;
        else if (x == x->parent->left) x->parent->left = y;
        else x->parent->right = y;
        y->left = x;
        x->parent = y;
    }

    void rotateRight(Node *&root, Node *&y) {
        Node *x = y->left;
        y->left = x->right;
        if (y->left != nullptr) y->left->parent = y;
        x->parent = y->parent;
        if (y->parent == nullptr) root = x;
        else if (y == y->parent->left) y->parent->left = x;
        else y->parent->right = x;
        x->right = y;
        y->parent = x;
    }

    void fixViolation(Node *&root, Node *&ptr) {
        Node *parent_ptr = nullptr;
        Node *grand_parent_ptr = nullptr;

        while ((ptr != root) && (ptr->color != BLACK) && (ptr->parent->color == RED)) {
            parent_ptr = ptr->parent;
            grand_parent_ptr = ptr->parent->parent;

            /* Case A: ptr's parent is the left child of ptr's grandparent */
            if (parent_ptr == grand_parent_ptr->left) {
                Node *uncle_ptr = grand_parent_ptr->right;
                if (uncle_ptr != nullptr && uncle_ptr->color == RED) {
                    grand_parent_ptr->color = RED;
                    parent_ptr->color = BLACK;
                    uncle_ptr->color = BLACK;
                    ptr = grand_parent_ptr;
                } else {
                    if (ptr == parent_ptr->right) {
                        rotateLeft(root, parent_ptr);
                        ptr = parent_ptr;
                        parent_ptr = ptr->parent;
                    }
                    rotateRight(root, grand_parent_ptr);
                    std::swap(parent_ptr->color, grand_parent_ptr->color);
                    ptr = parent_ptr;
                }
            }
            /* Case B: ptr's parent is the right child of ptr's grandparent */
            else {
                Node *uncle_ptr = grand_parent_ptr->left;
                if ((uncle_ptr != nullptr) && (uncle_ptr->color == RED)) {
                    grand_parent_ptr->color = RED;
                    parent_ptr->color = BLACK;
                    uncle_ptr->color = BLACK;
                    ptr = grand_parent_ptr;
                } else {
                    if (ptr == parent_ptr->left) {
                        rotateRight(root, parent_ptr);
                        ptr = parent_ptr;
                        parent_ptr = ptr->parent;
                    }
                    rotateLeft(root, grand_parent_ptr);
                    std::swap(parent_ptr->color, grand_parent_ptr->color);
                    ptr = parent_ptr;
                }
            }
        }
        root->color = BLACK;
    }

public:
    RedBlackTree() : root(nullptr) {}

    void insert(const int &data) {
        Node *ptr = new Node(data);
        root = insertBST(root, ptr);
        fixViolation(root, ptr);
    }

    Node* insertBST(Node* root, Node* ptr) {
        if (root == nullptr) return ptr;
        if (ptr->data < root->data) {
            root->left = insertBST(root->left, ptr);
            root->left->parent = root;
        } else if (ptr->data > root->data) {
            root->right = insertBST(root->right, ptr);
            root->right->parent = root;
        }
        return root;
    }

    Node* getRoot() { return root; }
};
