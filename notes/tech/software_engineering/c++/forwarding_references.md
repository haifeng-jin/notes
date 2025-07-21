# Forwarding References

We know [rvalue references](lvalue_vs_rvalue.md).
The forwarding references is about passing lvalue to rvalue reference
arguments.

You have to use template even you only want to use it with int.
This is a grammar requirement.

The `std::forward<T>` would forward the type (lvalue or rvalue) to the function
called. So, it routes to the corresponding overloaded function.

```cpp
#include <utility> // For std::forward and std::move
#include <iostream>

// A template function using a forwarding reference
template <typename T>
void wrapper_function(T&& arg) {
    // std::forward maintains the original value category
    // If arg was an lvalue, it's forwarded as an lvalue.
    // If arg was an rvalue, it's forwarded as an rvalue.
    some_other_function(std::forward<T>(arg));
}

void some_other_function(int& lref) {
    std::cout << "some_other_function called with lvalue reference: " << lref << std::endl;
}

void some_other_function(int&& rref) {
    std::cout << "some_other_function called with rvalue reference: " << rref << std::endl;
}

int main() {
    int a = 10;
    wrapper_function(a);          // a is an lvalue, T deduces to int&, T&& becomes int&
    wrapper_function(20);         // 20 is an rvalue, T deduces to int, T&& becomes int&&

    return 0;
}
```
