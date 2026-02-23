#include <iostream>

/**
 * Implementation of a smart pointer with reference counting.
 */
template <typename T>
class CustomSharedPtr {
private:
    T* ptr;
    int* refCount;

    void release() {
        if (refCount) {
            (*refCount)--;
            if (*refCount == 0) {
                delete ptr;
                delete refCount;
            }
        }
    }

public:
    // Constructor
    explicit CustomSharedPtr(T* p = nullptr) : ptr(p) {
        if (p) {
            refCount = new int(1);
        } else {
            refCount = nullptr;
        }
    }

    // Copy constructor
    CustomSharedPtr(const CustomSharedPtr& other) {
        ptr = other.ptr;
        refCount = other.refCount;
        if (refCount) {
            (*refCount)++;
        }
    }

    // Assignment operator
    CustomSharedPtr& operator=(const CustomSharedPtr& other) {
        if (this != &other) {
            release();
            ptr = other.ptr;
            refCount = other.refCount;
            if (refCount) {
                (*refCount)++;
            }
        }
        return *this;
    }

    // Destructor
    ~CustomSharedPtr() {
        release();
    }

    T& operator*() const { return *ptr; }
    T* operator->() const { return ptr; }
    int use_count() const { return (refCount) ? *refCount : 0; }
    T* get() const { return ptr; }
};

/**
 * Complexity Analysis:
 * Time: O(1) for all operations (assignment, copy, access).
 * Space: O(1) additional for each instance (pointer to data and pointer to counter).
 */
