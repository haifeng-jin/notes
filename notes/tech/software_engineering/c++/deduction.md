# Deduction

In C++, deduction refers to the process by which the compiler automatically
determines the type of a variable, function template argument, or class
template argument based on the context of its use. It saves you from explicitly
specifying types, making code more concise and flexible.

See the following example.
The argument and the return type of a function can both be `auto`.
And the template type is also a deduction.

```cpp
// Function template with argument type deduction, and an 'auto' argument
template <typename T>
auto process_data(const std::vector<T>& data, auto operation) { // 'data' type deduced, 'operation' type is deduced
    auto sum = T();

    for (const auto& item : data) {
        sum += operation(item); // Apply the 'operation' to each item
    }

    return sum;
}
```
