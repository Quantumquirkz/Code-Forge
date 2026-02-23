#include <vector>
#include <cstddef>

/**
 * Memory Pool for fixed-size block allocation.
 */
class MemoryPool {
private:
    struct Block {
        Block* next;
    };

    size_t blockSize;
    size_t numBlocks;
    void* pool;
    Block* freeList;

public:
    MemoryPool(size_t blockSize, size_t numBlocks) 
        : blockSize(blockSize < sizeof(Block) ? sizeof(Block) : blockSize), 
          numBlocks(numBlocks) {
        
        pool = operator new(this->blockSize * numBlocks);
        freeList = reinterpret_cast<Block*>(pool);

        // Initialize free list by linking each block to the next
        Block* current = freeList;
        for (size_t i = 0; i < numBlocks - 1; ++i) {
            current->next = reinterpret_cast<Block*>(reinterpret_cast<char*>(current) + this->blockSize);
            current = current->next;
        }
        current->next = nullptr;
    }

    ~MemoryPool() {
        operator delete(pool);
    }

    void* allocate() {
        if (!freeList) return nullptr;

        void* result = freeList;
        freeList = freeList->next;
        return result;
    }

    void deallocate(void* ptr) {
        if (!ptr) return;

        Block* block = reinterpret_cast<Block*>(ptr);
        block->next = freeList;
        freeList = block;
    }
};

/**
 * Complexity Analysis:
 * Time: O(1) for allocate and deallocate.
 * Space: O(N * S) where N is the number of blocks and S is the size of each block.
 */
