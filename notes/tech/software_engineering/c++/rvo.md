# Return Value Optimization (RVO)

Return Value Optimization (RVO) and Named Return Value Optimization (NRVO).
They are compiler optimizations to void unnecessary copy/move of the return value of a function in certain scenarios.

Let's look at the following code:

```cpp
MyClass createObject() {
    return MyClass(); // RVO likely happens here
}
```

```cpp
MyClass createAndModifyObject() {
    MyClass obj;
    // ... modify obj ...
    return obj; // NRVO likely happens here
}
```

At first glance, the local objects in the functions should be created in the
stack memory and returned by copying it back as an
[rvalue](lvalue_vs_rvalue.md).
However, RVO & NRVO happen here to help optimize that.
The compiler directly constructs the objects in the caller's memory location.
This means no copy and no move actually happen.
