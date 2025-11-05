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

#include <iostream>
#include <string>
#include <absl/status/status.h>
#include <absl/status/statusor.h>
#include <absl/strings/str_format.h>

// --- Mock Status Macros (for demonstration) ---
// In a real project, these would be in a status_macros.h file.

// 1. RETURN_IF_ERROR
// If 'expr' returns a non-OK status, immediately returns that status.
#define RETURN_IF_ERROR(expr) \
  do { \
    const absl::Status _status = (expr); \
    if (ABSL_PREDICT_FALSE(!_status.ok())) { \
      return _status; \
    } \
  } while (false)

// 2. ASSIGN_OR_RETURN
// Calls 'expr', and if it succeeds, assigns the value to 'lhs'.
// If it fails, returns the status from the current function.
#define ASSIGN_OR_RETURN(lhs, expr) \
  ASSIGN_OR_RETURN_IMPL( \
      STATUS_MACROS_CONCAT_NAME(_status_or_value, __COUNTER__), lhs, expr)

#define ASSIGN_OR_RETURN_IMPL(statusor_val, lhs, expr) \
  absl::StatusOr<std::remove_reference<decltype(lhs)>::type> statusor_val = (expr); \
  if (ABSL_PREDICT_FALSE(!statusor_val.ok())) { \
    return statusor_val.status(); \
  } \
  lhs = std::move(statusor_val.value());

// Helper for macro name concatenation
#define STATUS_MACROS_CONCAT_NAME(x, y) STATUS_MACROS_CONCAT_NAME_IMPL(x, y)
#define STATUS_MACROS_CONCAT_NAME_IMPL(x, y) x##y

// --- Core Logic ---

// Function 1: Returns a simple absl::Status (Error Propagator)
// Simulates checking if a file is readable before processing.
absl::Status CheckFilePermissions(const std::string& filename, bool fail_check) {
    if (fail_check) {
        return absl::PermissionDeniedError(
            absl::StrFormat("Cannot read file '%s': Permission denied.", filename));
    }
    std::cout << "  [SUCCESS] Permissions checked for " << filename << std::endl;
    return absl::OkStatus();
}

// Function 2: Returns absl::StatusOr<T> (Value Extractor)
// Simulates parsing configuration data from a source.
absl::StatusOr<int> ParseConfigValue(const std::string& config_data, bool fail_parse) {
    if (fail_parse) {
        return absl::InvalidArgumentError(
            absl::StrFormat("Config '%s' is invalid: Failed to parse integer.", config_data));
    }
    // Simulate successful parsing
    std::cout << "  [SUCCESS] Config parsed successfully. Value is 42." << std::endl;
    return 42;
}

// Function 3: The high-level function that ties everything together.
// This function uses both RETURN_IF_ERROR and ASSIGN_OR_RETURN.
absl::Status ProcessDataFlow(bool permissions_fail, bool parsing_fail) {
    std::cout << "\n>>> Starting ProcessDataFlow..." << std::endl;

    // Use RETURN_IF_ERROR: Check status of function that returns absl::Status
    RETURN_IF_ERROR(CheckFilePermissions("config.txt", permissions_fail));
    std::cout << "  -> File check passed." << std::endl;

    // Use ASSIGN_OR_RETURN: Get value from function that returns absl::StatusOr<T>
    // If ParseConfigValue fails, this function immediately returns the error.
    int config_value;
    ASSIGN_OR_RETURN(config_value, ParseConfigValue("DATA_123", parsing_fail));
    std::cout << "  -> Config value obtained: " << config_value << std::endl;
    
    // Simulate final step using the extracted value
    if (config_value != 42) {
        return absl::InternalError("Unexpected config value.");
    }

    std::cout << ">>> ProcessDataFlow completed successfully." << std::endl;
    return absl::OkStatus();
}

// --- Main Execution ---

int main() {
    // --- SCENARIO 1: All Success ---
    absl::Status status1 = ProcessDataFlow(/*permissions_fail=*/false, /*parsing_fail=*/false);
    std::cout << "\n[RESULT 1] Final Status: " << status1.message() << "\n\n" << std::endl;

    // --- SCENARIO 2: Permission Failure (Fails at RETURN_IF_ERROR) ---
    absl::Status status2 = ProcessDataFlow(/*permissions_fail=*/true, /*parsing_fail=*/false);
    std::cout << "\n[RESULT 2] Final Status: " << status2.message() << "\n\n" << std::endl;

    // --- SCENARIO 3: Parsing Failure (Fails at ASSIGN_OR_RETURN) ---
    absl::Status status3 = ProcessDataFlow(/*permissions_fail=*/false, /*parsing_fail=*/true);
    std::cout << "\n[RESULT 3] Final Status: " << status3.message() << "\n\n" << std::endl;

    return 0;
}