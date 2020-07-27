# Python
## Gramma
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

## Testing
* pytest: [Pytest Course - YouTube](https://www.youtube.com/playlist?list=PLJsmaNFr5mNqSeuNepT3IaMrgzRMm9lQR)
* Mock classes
You cannot directly mock a class, e.g. `class ClassA`, if it contains a line of `super(ClassA, self).__init__()` since `super` does not allow to be called with a mock object. So you have to mock the functions instead of the entire class. For example, `mock.patch('ClassA.__init__')`.
* Assert mocked function calls
```py
@mock.patch('ClassA.foo')
@mock.patch('ClassA.bar')
def test_add_early_stopping(bar, foo): # Remember they are in reversed order in args.
	ClassA.some_function_which_calls_foo_inside()
  assert foo.called	
	foo.assert_called_with(x=1, y=2)s
	args, kwargs = foo.call_args_list[0] # 0 means the first time that foo is called. 1 means the second time.
	assert kwargs['x'] == 1
```

## Python Best Practices
* Import modules instead of specific objects. If the name of the module conflicts with the variables in the current module, just use "from .. import .. as .." to avoid it.
* Import one module per line.
* The constructors should always have docstring describing the Args.
* The keywords in constructor should be accessible with the instance. (i.e. the constructor keywords should also be attributes or properties)
* In long if statements, to line break, avoid using "\", but use "if (a and b and c)" and directly line break after each "and".
* If the parent class and the sub class share some args, the required arguments should be documented again in the sub class even they are the same. The arguments in kwargs can be not documented. For the ones not required and not in the kwargs, we should also document them even they are repeated in some other classes.
* When override a method of the parent class, to avoid the duplication of the code, we can try to do the new things in the override functions and do the old things by calling the super function.
* When calling a function with many arguments, use the argument names to call to avoid errors.
* Although we can avoid duplicate code by using the kwargs in the subclass and pass it to super().__init__(), but we sometimes can explicitly list the args in the subclass for readability.
* If the subclass don't support all the args in the super().__init__(), we can remove the kwargs from the subclass and list all the supported ones explicitly.
* In docstrings of a class, use Args or Arguments to specify the args of init. Use Attributes to specify the attributes which are not init args but publicly accessible.
* Two reasons to extract a function: code reuse, or readability.
* We don't really need requirements.txt when we have everything in setup.py. We can use  `pip install .`  to install the dependencies.
* In setup.py, we don't specify the version of a dependency package the feature we use from it exists in all versions. If the feature only exists later than a certain version, we just put ">=" to specify the version. Using "==" is not a good practice since it may mess up the dependencies of other packages which depends on the same package.
* It is not a good practice for the user to provide a list, whose length is required to be a specific number. The user may easily miss some of the elements and got an error.
* The comments to a if statement should be above it. The same for the else clause.
* To test if an exception is correctly thrown, assert 'This is broken' in str(context.exception).
* Do not use acronym for any API related things exposed to the users unless it is a really well-known acronym.
