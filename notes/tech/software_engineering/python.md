# Python
## Grammar
* dictionary.pop(key[, default])
```py
a = {'name': 'alice'}
print(a.pop('name', 'bob'))
# alice
a = {}
print(a.pop('name', 'bob'))
# alice
```

* `my_dict.setdefault(key, []).append(new_value)`
…is the same as running…
``` python
if key not in my_dict:
	my_dict[key] = []
	my_dict[key].append(new_value)
```

…except that the latter code performs at least two searches for key—three if it’s not found—while setdefault does it all with a single lookup.


## Python Best Practices
* Import modules instead of specific objects. If the name of the module conflicts with the variables in the current module, just use "from .. import .. as .." to avoid it.
* Import one module per line.
* The constructors should always have docstring describing the Args.
* In long if statements, to line break, avoid using "\", but use "if (a and b and c)" and directly line break after each "and".
* When override a method of the parent class, to avoid the duplication of the code, we can try to do the new things in the override functions and do the old things by calling the super function.
* When calling a function with many arguments, use the argument names to call to avoid errors.
* Although we can avoid duplicate code by using the kwargs in the subclass and pass it to super().__init__(), but we sometimes can explicitly list the args in the subclass for readability.
* If the subclass don't support all the args in the super().__init__(), we can remove the kwargs from the subclass and list all the supported ones explicitly.
* Two reasons to extract a function: code reuse, or readability.
* We don't really need requirements.txt when we have everything in setup.py. We can use  `pip install .`  to install the dependencies.
* In setup.py, we don't specify the version of a dependency package the feature we use from it exists in all versions. If the feature only exists later than a certain version, we just put ">=" to specify the version. Using "==" is not a good practice since it may mess up the dependencies of other packages which depends on the same package.
* The comments to a if statement should be above it. The same for the else clause.
* To test if an exception is correctly thrown, assert 'This is broken' in str(context.exception).
