# Internal vs External Linkage

This internal vs external linkage concept is referring to the [translation
unit](./translation_unit.md) at compile time. It describes if an entity has its
own copy in a translation unit or link to one from another translation unit.

If a function is declared in the header and implemented in the source file, it
would create a external linkage.  Every translation unit gets the same copy of
the function.

If the function is defined directly in the header, it would create an internal
linkage. Every translation unit would get a separate copy.

There is also a concept called "no linkage".  For example, a type has no
linkage. A class or a template is a type definition. They have no linkage.  So,
put them in the header would not violate the ODR as they do not link.
