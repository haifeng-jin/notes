# The `optional` keyword

It can contain a value or nothing.
The typical use cases are:
* Function parameters.
* Function return values.
* Member variables.

## Function parameters

```cpp
void log(const std::string& message, std::optional<int> severity) {
    // has_value() checks if it has a value.
    if (severity.has_value()) {
        // Use the severity value.
        std::cout << "[Severity " << severity.value() << "] ";
    }
    std::cout << message << std::endl;
}

// Usage
log("Application started.", 1);
log("Something happened.", std::nullopt);
```

## Function return values

```cpp
std::optional<std::string> find_name(const std::map<int, std::string>& users, int id) {
    auto it = users.find(id);
    if (it != users.end()) {
        return it->second; // Return the found string.
    }
    return std::nullopt; // Return an empty optional.
}
```

## Member variables

```cpp
class UserProfile {
public:
    std::string first_name;
    std::optional<std::string> middle_name;
    std::string last_name;
};
```


## Example usages

```cpp
#include <iostream>
#include <optional>
#include <string>

// A function that returns an optional string.
std::optional<std::string> get_user_name(int id) {
    if (id == 1) {
        return "Alice";
    }
    return std::nullopt; // The empty state.
}

int main() {
    // Case 1: The optional has a value.
    std::optional<std::string> user1 = get_user_name(1);

    // Check if a value exists using has_value() or in a boolean context.
    if (user1.has_value()) { // Same as: if (user1)
        std::cout << "User 1 found: " << *user1 << std::endl;
        std::cout << "Using value() member: " << user1.value() << std::endl;
    }

    // Use value_or() to get the value or a default.
    std::string name_or_default = user1.value_or("Guest");
    std::cout << "User 1 (with value_or): " << name_or_default << std::endl;

    // Case 2: The optional is empty.
    std::optional<std::string> user2 = get_user_name(2);

    if (!user2.has_value()) { // Same as: if (!user2)
        std::cout << "User 2 not found." << std::endl;
    }

    // Using value_or() on an empty optional returns the default.
    name_or_default = user2.value_or("Guest");
    std::cout << "User 2 (with value_or): " << name_or_default << std::endl;

    // --- Dangerous usage ---
    // Calling .value() on an empty optional will throw an exception.
    try {
        std::cout << user2.value() << std::endl;
    } catch (const std::bad_optional_access& e) {
        std::cout << "Caught exception: " << e.what() << std::endl;
    }

    // Using reset() to make a non-empty optional empty.
    user1.reset();
    if (!user1.has_value()) {
        std::cout << "User 1 has been reset." << std::endl;
    }

    return 0;
}
```
