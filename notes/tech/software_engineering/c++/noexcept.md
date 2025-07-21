# The `noexcept` keyword

`noexcept` in C++ is a specifier that indicates whether a function is guaranteed
not to throw an exception. If a function marked `noexcept` does throw an
exception, the program's execution is immediately terminated by calling
`std::terminate`.

It would also change the behavior of the std containers, like `std::vector`.
If you garantee there is no exception throw, the vector knows that it move
process would not be interrupted to leave the vector in an corrupted status, it
can do the move without making copies to prevent the corruption.

This is why we want to use `noexcept` to the [move contructor](move_constructor.md).
