# Python

## Data Model

* `collections.namedtuple` is for classes only with attributes, which is similar to `struct` in C++.
* `__getitem__(self, position)` overrides the `[]` operator.
* `__len__`'s return value is used as the return value for `len(...)`.

```py
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
```

```py
>>> deck = FrenchDeck()
>>> len(deck)
52
>>> deck[0]
Card(rank='2', suit='spades')
```

## Data Structures
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

## Decorators

Decorator `deco` is implemented as a function `deco` that returns a function `inner`.
If `target` is decorated with `@deco`, then `inner` will be executed instead of `target`, when `target` is called.

Following is an easy example.

```py
>>> def deco(func):
...     def inner():
...         print('running inner()')
...     return inner
...
>>> @deco
... def target():
...     print('running target()')
...
>>> target()
running inner()
>>> target
<function deco.<locals>.inner at 0x10063b598>
```

The decorator functions, for example, the `deco` function in the example above, are run at import time instead of when calling `target`.

## Design Patterns
* Functions can be treat as objects in Python.
* The strategy pattern and command pattern can be simplified. Whenever, there are multiple classes implementing the same interface to override a single function, we can simplify these classes into functions and pass them around.

### Rewriting Strategy Pattern

The following code is to get the best promotion on the given order with function `best_promo`.
The decorator `@promotion` will register all these promo functions at the import time to the global variable `promos`.

There are 2 things optimized here.
* The promo functions can just be functions instead of classes implementing the same interface.
* We don't need to mannually construct the `promos` list. Otherwise, everytime we have a new type of promo function, we will have to modify the code in two places, the implementation of the promofunction and the `promos` list.

```py
promos = []  1

def promotion(promo_func):  2
    promos.append(promo_func)
    return promo_func

@promotion  3
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):  4
    """Select best discount available
    """
    return max(promo(order) for promo in promos)
```

## Scopes
The global variables are separated from local variables defined in functions.
If you want to use an global variable in a function, you have to define it with `global variable_name`.
Otherwise the following error would happen.

```py
>>> b = 6
>>> def f2(a):
...     # global b
...     print(a)
...     print(b)
...     b = 9
...
>>> f2(3)
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f2
UnboundLocalError: local variable 'b' referenced before assignment
```

We should uncomment the `global b` to make it correct. 

### Closure

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
