# Move constructor

What it does is to copy the data and nullify the source.
We mark it as [`noexcept`](noexcept.md), so that it would not fall back to the copy
constructor of the vector.
The move constructor is featured by the `&&` rvalue reference.
When use `move`, it picks the correct constructor among others.

```cpp
class MyVectorWrapper {
public:
    // Move Constructor (Shallow Copy + Nullify Source)
    MyVectorWrapper(MyVectorWrapper&& other) noexcept : data_(other.data_), size_(other.size_) {
        std::cout << "Move Constructor: Moving " << size_ << " ints.\n";
        other.data_ = nullptr; // Crucial: Nullify the source's pointer
        other.size_ = 0;       // Crucial: Reset source's size
    }


private:
    int* data_;
    size_t size_;
};

int main() {
    MyVectorWrapper moved_wrapper = std::move(original_wrapper); // Calls Move Constructor
    return 0;
}
```
