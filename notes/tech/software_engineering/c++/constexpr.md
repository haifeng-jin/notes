# The `constexpr` keyword

The `constexpr` keyword is to tell the compiler to compute the value of the
constant variable at compile time instead of runtime.

If it is a `constexpr` function, the return value of the function calls could
be computed at compile time if all the args could be computed at compile time.

Following are some examples.

```cpp
#include <iostream>

constexpr int multiply(int a, int b) {
    return a * b;
}

int main() {
    // Computed at compile time.
    constexpr int a = 10;
    constexpr int b = 10 * 20;
    constexpr int c = multiply(5, 10);
    int d = multiply(5, 10);
    int arr[multiply(2, 3)];

    // Computed at runtime.
    int user_num;
    std::cin >> user_num;
    int runtime_result = multiply(7, user_num);

    // This would be an error, as the array size must be a compile-time constant
    // int another_arr[multiply(4, user_num)]; // ERROR!

    return 0;
}
```
