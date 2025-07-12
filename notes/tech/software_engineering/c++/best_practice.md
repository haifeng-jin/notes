# Best Practices

This note is to put the knowledge we learned about C++ building to application.
They are just some inferences from the knowledge.

## Do not define non-inline functions in headers

Even with the header guards, it will still result in an error.
For example, you have a file `a.h` with a function implementation of `int A()` within the header guard.
And you have `a.cpp` and `b.cpp` both includes `a.h`.
So, you will get two translation units for the `.cpp` files.
Each of them would compile the function separately.
So, if you ever need to link them into one executable, it results in an linking
error because it violates the ODR.

However, inline functions are OK since they do not remain a function as they
are compiled, they are simply copy and pasted into the functions calling them.

## Do not use unnamed namespace in headers

Similarly, if you use unnamed namespace in headers, it will also be compiled multiple times.
However, it will not results in an linking error because the functions in the
unnamed namespace are only visible to the translation unit that uses it.
However, if you ever want to use the variables in the namespace, you will face a problem.
Every translation unit has its own version of the same variable. They do not share the same variable.
So, it is bug-prone.
