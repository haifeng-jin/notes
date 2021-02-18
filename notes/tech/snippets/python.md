# Python

* If some modules only work with certain versions of dependencies,
we should enclose the `import` statement in a `try` clause.

```python
try:
    from .augment import HyperEfficientNet
except ImportError:
    HyperEfficientNet = None
```
