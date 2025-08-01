# Pointers

`shared_ptr` and  `unique_ptr` are parts of the C++ standard library.  They
provide a safer way to manage pointers.  The dynamically allocated objects will
be destroyed when these pointers goes out of scope.

## `nullptr`

`nullptr` was introduced to solve the ambiguity of `NULL` and `0`.
It is a `prvalue`, a pure rvalue. It can only exist as an rvalue.
It is of type `std::nullptr_t`.

It provides type safety. So, there is no ambiguity when you call a overloaded function with it.
However, if you call it with `0` or `NULL`, the could be either `int` or `char`.

## `unique_ptr`

```cpp
// A function that returns a unique_ptr to a newly created object.
std::unique_ptr<MyClass> createMyClass() {

    // Use make_unique to create one.
    std::unique_ptr<MyClass> ptr1 = std::make_unique<MyClass>();

    // std::unique_ptr<MyClass> ptr2 = ptr1; // This would cause a compile-time error
    std::unique_ptr<MyClass> ptr2 = std::move(ptr1); // Ownership is moved

    // ptr1 becomes nullptr.
    if (ptr1 == nullptr) {
        std::cout << "ptr1 is now null" << std::endl;
    }

    // Create another object ptr3.
    std::unique_ptr<MyClass> ptr3 = std::make_unique<MyClass>();

    // Do not use std::move when returning. The ownership is automatically
    // transferred.
    return ptr2;
    // MyClass is destroyed when ptr3 goes out of scope
}
```

When passing a `unique_ptr` as a parameter to a function, you either need to
pass by reference, or using `std::move`.
However, if using `std::move`, the object will be destroyed at the end of the
function if you don't return it back.

## `shared_ptr`

`shared_ptr` is much simpler, it allows multiple pointers to point to the same object.
So, no `std::move` is needed. It uses `std::make_shared<MyClass>();` to create.

Dereferenced pointers: referring to the value that a pointer is pointing to.
