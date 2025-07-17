# The `static` keyword

There are 5 different ways of using the `static` keyword in total.

* Defining a variable in a function.
* Defining member variable.
* Defining a global variable.
* Defining a member function.
* In anonymous union. (less common)

## Defining a variable in a function.

```cpp
#include <iostream>

void counter() {
    static int count = 0; // Initialized only once
    count++;
    std::cout << "Count: " << count << std::endl;
}

int main() {
    counter(); // Count: 1
    counter(); // Count: 2
    counter(); // Count: 3
    return 0;
}
```

## Defining member variable.

If we define a member variable of a class with the `static` keyword,
it belongs to the class instead of any object, and shared among all the objects.

You have to separate the declaration and definition/initialization. This is due to the memory allocation.
The static member variable is not created with any object but with the class.

It can be accessed with class name: `MyClass::objectCount`.

It is not recommended to access it from a object, like `obj1.objectCount`.
It would not error out, but it is confusing.

```cpp
#include <iostream>

class MyClass {
public:
    static int objectCount; // Declaration

    MyClass() {
        objectCount++;
    }

    ~MyClass() {
        objectCount--;
    }
};

// Definition and initialization of the static member variable
int MyClass::objectCount = 0;

int main() {
    std::cout << MyClass::objectCount << std::endl; // Access via class name

    MyClass obj1;
    MyClass obj2;
    std::cout << MyClass::objectCount << std::endl;

    {
        MyClass obj3;
        std::cout << MyClass::objectCount << std::endl;
    } // obj3 goes out of scope and is destroyed

    std::cout << MyClass::objectCount << std::endl;

    return 0;
}
```

## Defining a global variable.

Now, we use the `static` keyword outside any function or class.
The defined variable is only visible in that file.
This is similar to using a unnamed namespace.

```cpp
static int globalStaticVar = 10; // Only visible in this file.
```

## Defining a member function.

It is similar to Python's static method.
It cannot access `this` pointer, so no object's members access.

```cpp
#include <iostream>
#include <string>

class Logger {
public:
    static void logMessage(const std::string& message) {
        std::cout << "[LOG] " << message << std::endl;
    }

private:
    // This would be inaccessible from a static member function
    std::string privateData;
};

int main() {
    Logger::logMessage("Application started."); // Call via class name
    Logger::logMessage("Processing data...");
    // Logger myLogger;
    // myLogger.logMessage("This also works but is less common for static functions.");

    return 0;
}
```
