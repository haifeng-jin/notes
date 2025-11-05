# Move constructor

What it does is to copy the data and nullify the source.
We mark it as [`noexcept`](noexcept.md), so that it would not fall back to the copy
constructor of the vector.
The move constructor is featured by the `&&` rvalue reference.
When use `move`, it picks the correct constructor among others.

```cpp
#include <iostream>
#include <utility> // For std::move

/**
 * @brief A strictly Move-Only class that manages a heap-allocated resource.
 */
class UniqueData {
private:
    int* data_ptr_;
    size_t size_;

public:
    // 1. Constructor: Allocates the resource
    UniqueData(size_t s) : size_(s) {
        data_ptr_ = new int[size_];
        std::cout << "-> Resource allocated at " << data_ptr_ << std::endl;
        // Initialize for demonstration
        for (size_t i = 0; i < size_; ++i) {
            data_ptr_[i] = i;
        }
    }

    // 2. Destructor: Releases the resource
    ~UniqueData() {
        if (data_ptr_ != nullptr) {
            std::cout << "<- Resource at " << data_ptr_ << " released." << std::endl;
            delete[] data_ptr_;
        }
    }

    // --- ENFORCE MOVE-ONLY SEMANTICS (DELETE COPY OPERATIONS) ---

    // 3. Delete the Copy Constructor
    // Prevents: UniqueData obj2 = obj1;
    UniqueData(const UniqueData& other) = delete; 

    // 4. Delete the Copy Assignment Operator
    // Prevents: obj2 = obj1;
    UniqueData& operator=(const UniqueData& other) = delete;

    // --- DEFINE MOVE OPERATIONS ---

    // 5. Define the Move Constructor
    // Handles initialization from a temporary or std::move()
    UniqueData(UniqueData&& other) noexcept 
        : data_ptr_(other.data_ptr_), size_(other.size_) {
        
        // Null out the source's pointer to prevent its destructor from deleting the resource
        other.data_ptr_ = nullptr;
        other.size_ = 0;
        std::cout << "  [Move Constructor] Ownership transferred from " 
                  << data_ptr_ << " to " << this << std::endl;
    }

    // 6. Define the Move Assignment Operator
    // Handles assignment from a temporary or std::move()
    UniqueData& operator=(UniqueData&& other) noexcept {
        if (this != &other) {
            // 1. Release our own existing resource first
            delete[] data_ptr_; 
            
            // 2. Steal the resource from 'other'
            data_ptr_ = other.data_ptr_;
            size_ = other.size_;
            
            // 3. Null out 'other's pointer
            other.data_ptr_ = nullptr;
            other.size_ = 0;
            std::cout << "  [Move Assignment] Ownership transferred to " 
                      << this << std::endl;
        }
        return *this;
    }

    // Utility function to show the data
    void print_data() const {
        if (data_ptr_ != nullptr) {
            std::cout << "Data: [";
            for (size_t i = 0; i < size_; ++i) {
                std::cout << data_ptr_[i] << (i == size_ - 1 ? "" : ", ");
            }
            std::cout << "] (Size: " << size_ << ")" << std::endl;
        } else {
            std::cout << "Data: EMPTY (Resource moved away)" << std::endl;
        }
    }
};

int main() {
    std::cout << "--- Initializing Objects ---" << std::endl;
    UniqueData source(5); // Calls Constructor
    source.print_data();

    std::cout << "\n--- TEST 1: Move Constructor (Initialization) ---" << std::endl;
    // Creates 'dest1' by moving the resource from 'source'
    UniqueData dest1 = std::move(source); 
    dest1.print_data();
    source.print_data(); // 'source' is now empty

    std::cout << "\n--- TEST 2: Move Assignment Operator ---" << std::endl;
    UniqueData dest2(3); // Calls Constructor
    
    // Creates a temporary object, moves the resource from that temporary to 'dest2'
    dest2 = UniqueData(7); // Calls Constructor for temporary, then Move Assignment
    dest2.print_data();

    std::cout << "\n--- TEST 3: Attempting Copy (Compile-Time Error) ---" << std::endl;
    // The following lines would cause a COMPILATION ERROR 
    // because the copy constructor and copy assignment are deleted:
    // UniqueData invalid_copy = dest1; // Fails
    // dest2 = dest1;                   // Fails
    std::cout << "-> Copying is prevented at compile time." << std::endl;
    
    std::cout << "\n--- End of Program (Destructors Run) ---" << std::endl;
    return 0;
}
```
