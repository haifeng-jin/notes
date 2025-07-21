# lvalue vs rvalue

The intuitive understanding is whether they can appear on the left side of the `=` sign.
The more accurate definition is whether they have a persistent memory location.
If they do, they are lvalue, otherwise, rvalue.

Some examples of lvalues:

* Variables: `int x = 10;` (`x` is an lvalue)
* [Dereferenced pointers](pointers.md): `*ptr`
* Function calls (operator override) that return an lvalue reference: `std::cout <<`
* Members of objects that are lvalues.


Some examples of rvalues:

* Literals: `10`, `"hello"`
* Temporary objects created by expressions: `x + y` (the result of the addition is a temporary rvalue)
* Function calls that return by value: `std::string func_returns_string()`
* `std::move`'s return value


You can use `&` for lvalue reference arguments, and `&&` for rvalue arguments.
The following function overload is an example of how the compiler would route
the calls to different functions.

If you do not overload and only have one function, you can pass a rvalue to an
lvalue reference without error, but not an lvalue to an rvalue reference.

```cpp
void process(std::vector<int>& vec) { }

void process(std::vector<int>&& vec) { }

int main() {
    std::vector<int> my_vec = {1, 2, 3};
    process(my_vec);                   // Calls process(std::vector<int>&) - lvalue
    process(std::vector<int>{4, 5, 6}); // Calls process(std::vector<int>&&) - rvalue (temporary object)
    return 0;
}
```
