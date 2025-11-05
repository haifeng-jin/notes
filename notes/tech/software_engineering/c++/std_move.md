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
If the function is overloaded, in the following case, it would correctly pick
the rvalue reference function.

```cpp
void process_data(std::vector<int>&& data_to_process) {...}

std::vector<int> my_active_data = {10, 20, 30};

// process_data(my_active_data); // COMPILE ERROR! Cannot bind lvalue to rvalue reference.
process_data(std::move(my_active_data)); // OK! Explicitly say you're done with my_active_data.
```

It is also widely used in the "pass by value and move" pattern.
We call the constructor by passing by values not by references, and move the value to the member variables.

```cpp
class MyClass {
public:
    // The vector is passed by value, then moved into the member variable.
    MyClass(std::vector<int> data) : m_data(std::move(data)) {
        // 'data' is now in a valid but unspecified state.
        // It's a "moved-from" object.
    }

private:
    std::vector<int> m_data;
};

```

Also, the `std::move` is widely used in the implementation of [move-only class](move_only_class.md).

Another important use case is to move the [`unique_ptr`](pointers.md) since they cannot be copied.
