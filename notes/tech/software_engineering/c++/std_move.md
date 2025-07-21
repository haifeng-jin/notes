# The `move` function

To understand move you will first need to understand [lvalue and rvalue](lvalue_vs_rvalue.md).
You will also need to understand [Return Value Optimization](rvo.md).

It is to create an rvalue from the given argument.
The given argument would be left in a valid but unspecified state.
For example, a string would become an empty string, a vector would become an empty vector.

It is useful in a `return` statement when the RVO does not apply.
For example:

```cpp
std::vector<int> func(std::vector<int> data) {
    ...
    return std::move(data);
}
```
Actually, in the case above, the `std::move` may be redundant.
Since, it triggers the [move constructor](move_constructor.md) by default.

It is also useful when we just want to move the resource.

```cpp
moved_string = std::move(large_string); // Moves the content
```

It is also useful to create an rvalue to trigger the rvalue reference function.

```cpp
void process_data(std::vector<int>&& data_to_process) {...}

std::vector<int> my_active_data = {10, 20, 30};

// process_data(my_active_data); // COMPILE ERROR! Cannot bind lvalue to rvalue reference.
process_data(std::move(my_active_data)); // OK! Explicitly say you're done with my_active_data.
```
