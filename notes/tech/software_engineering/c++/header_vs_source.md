# Header vs Source

In general only [declarations](../declaration_and_definition) should be put into the header files (`.h` files),
the definitions should all go into source files (`.cpp` files).
This is to obey the ODR.
We want each [translation unit](../translation_unit) to be aware of everything declared but not keep a
separate copy of the object in memory. Then, they link to the same object.

There are a few exceptions.

## Inline functions

They are not compiled as separate functions at compile time.
They are just copied and pasted into the functions calling them.
So, they have no declaration or definition. It is OK to have them in the header files.


## Class?
## Templates
