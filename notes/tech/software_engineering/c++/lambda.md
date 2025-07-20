# Lambda functions

Basic grammar:

```cpp
[capture_list](parameters) -> return_type {
    // function body
}
```

Concrete example:

```cpp
int x = 10;
auto multiply_by_x = [x](int y) {
    return x * y;
};
int result = multiply_by_x(5); // result will be 50 (10 * 5)
x = 20; // Changing x here won't affect the captured x in the lambda
int new_result = multiply_by_x(5); // new_result will still be 50
```

`[x]` captures by value.
If you use `[&x]`, it would be captured by reference.

If you use `[=]`, or `[&]`, they will capture every automatic variable
(variables with automatic storage duration, i.e., local variables, function
parameters) by value or by reference.
