# Python

## Pytest
* pytest: [Pytest Course - YouTube](https://www.youtube.com/playlist?list=PLJsmaNFr5mNqSeuNepT3IaMrgzRMm9lQR)
* Mock classes
You cannot directly mock a class, e.g. `class ClassA`, if it contains a line of `super(ClassA, self).__init__()` since `super` does not allow to be called with a mock object. So you have to mock the functions instead of the entire class. For example, `mock.patch('ClassA.__init__')`.

* Assert mocked function calls
```py
import mock


@mock.patch('ClassA.foo')
@mock.patch('ClassA.bar')
def test_add_early_stopping(bar, foo): # Remember they are in reversed order in args.
	ClassA.some_function_which_calls_foo_inside()
    assert foo.called
	foo.assert_called_with(x=1, y=2)

	args, kwargs = foo.call_args_list[0]  # 0 means the first time that foo is called. 1 means the second time.
	assert kwargs['x'] == 1

    foo.return_value = mock.Mock()  # Change the return value of the mock object.
```

## Version Compatibility

If some modules only work with certain versions of dependencies,
we should enclose the `import` statement in a `try` clause.

```python
try:
    from .augment import HyperEfficientNet
except ImportError:
    HyperEfficientNet = None
```
