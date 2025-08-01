# Abseil

The Abseil library is an open-source collection of C++ libraries developed and
used extensively at Google. It's not a single, monolithic library but a set of
utilities designed to augment and modernize the C++ standard library.

## Nullability

A lot of bugs are caused in C++ because of wrong handling of the null pointers.
`absl_nullable` and `absl_nonnull` provides a way to annotate the pointers to
be nullable or not.  When annotated, the compiler will warn when the pointers
are used in a unsafe way.

```cpp
// The annotation tells static analysis tools that 'data' is never null.
void ProcessData(Data* absl_nonnull data) {
  // We can immediately and safely use data without a null check.
  data->DoSomething();
}

// Correct usage:
Data my_data;
ProcessData(&my_data);

// Incorrect usage:
ProcessData(nullptr); // Static analysis tools will flag this as an error.
```

```cpp
// The annotation tells us that 'error' might be null.
void LogMessage(const std::string& message, ErrorInfo* absl_nullable error) {
  // The annotation reminds us to check for nullness.
  if (error != nullptr) {
    error->Log();
  }
  std::cout << message << std::endl;
}

// Correct usage:
ErrorInfo my_error;
LogMessage("An error occurred.", &my_error);
LogMessage("Everything is fine.", nullptr); // Valid to pass nullptr.
```

```cpp
class DataProcessor {
public:
  DataProcessor(Cache* absl_nullable cache) : cache_(cache) {}

  void Process(const std::string& key) {
    if (cache_ != nullptr) {
      // It's safe to check and use the cache if it exists.
      if (cache_->Get(key)) {
        // ... use cached data
        return;
      }
    }
    // ... calculate data and potentially add to cache
  }

private:
  // The annotation indicates that a 'cache' is optional.
  Cache* absl_nullable cache_;
};
```

```cpp
class Dependency {};

class MyClass {
public:
  // The constructor must ensure 'dependency_' is initialized with a valid object.
  // Using a member initializer list is the standard and safest way.
  MyClass(Dependency* absl_nonnull dep) : dependency_(dep) {}

  void UseDependency() {
    // We can safely dereference 'dependency_' without a null check.
    dependency_->SomeMethod();
  }

private:
  // The 'absl_nonnull' annotation ensures this pointer is always valid.
  Dependency* absl_nonnull dependency_;
};

// ...
Dependency my_dep;
MyClass my_object(&my_dep); // This is correct.
// MyClass another_object(nullptr); // Static analysis will flag this as an error.
```

## Status

`StatusOr` provides an alternative way for error handling, other than throw.
The developer must explicity checking if an error is returned from the function
before using its value.

```cpp
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include <iostream>
#include <string>

// A function that might succeed or fail.
absl::StatusOr<std::string> FindUserByID(int id) {
  if (id == 123) {
    return "Alice"; // Success: returns a string value.
  }
  // Failure: returns a status with an error code and message.
  return absl::NotFoundError("User not found with the given ID.");
}

int main() {
  // --- Case 1: Successful operation ---
  absl::StatusOr<std::string> success_result = FindUserByID(123);

  // Use 'ok()' to check for success.
  if (success_result.ok()) {
    // If ok(), it's safe to access the value.
    std::cout << "Success! Found user: " << success_result.value() << std::endl;
    // The dereference operator '*' also works.
    std::cout << "Dereferencing gives: " << *success_result << std::endl;
  } else {
    // This block won't be executed in this case.
    std::cout << "Error: " << success_result.status().message() << std::endl;
  }

  std::cout << "\n----------------------------------\n" << std::endl;

  // --- Case 2: Failing operation ---
  absl::StatusOr<std::string> failure_result = FindUserByID(456);

  if (failure_result.ok()) {
    // This block won't be executed in this case.
    std::cout << "Success! Found user: " << failure_result.value() << std::endl;
  } else {
    // If not ok(), get the error status.
    std::cout << "Error! Status: " << failure_result.status() << std::endl;
  }

  // A common, dangerous mistake is to access the value without checking ok().
  // This line would crash the program if uncommented:
  // std::cout << "Trying to access value directly: " << failure_result.value() << std::endl;

  return 0;
}
```
