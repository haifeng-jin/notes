# Keras

This is a note about developing Keras.

## Tracing

## Static values in tf_function
All statics will remain constant in `tf_function`.
Any example?
`Tensor.shape` are statics.
The TF operations are dynamic.
Usually looks like `tf.some_operation()`.
For example, `tf.shape()` is dynamic.

## Testing
The testing infra is a good practice that can be applied to other projects as well.

```py
from keras.testing_infra import test_combinations
from keras.testing_infra import test_utils

# test_combinations.TestCase is a class in Keras for testing.
# It extends the tf.test.TestCase and absl.testing.parameterized.TestCase
class SomeTest(test_combinations.TestCase):
  @test_combinations.run_with_all_model_types
  def test_model_instrumentation(self):
    layers = [
        layers_module.Dense(10, dtype=np.float64),
        layers_module.Dense(10, dtype=np.float64)
    ]
    model = test_utils.get_model_from_layers(layers, input_shape=(1,))
```

```py
# Keras style for run all modes. (Recommended)
# It runs the test three times.
# Once in TF 1 mode.
# For TF 2 modes, it run with `test_utils.should_run_eagerly` equal to `True` and `False`.
@test_combinations.run_all_keras_modes
def some_test(self):
    ...
    model.compile(..., run_eagerly=test_utils.should_run_eagerly)
# Use args to skip TF1 or TF2 modes.
@test_combinations.run_all_keras_modes(always_skip_v1=True)
@test_combinations.run_all_keras_modes(always_skip_eager=True)

# Only run twice in TF1 and TF2.
# The graph mode is the TF1 legacy mode.
# No args needed for the test method.
@test_combinations.generate(test_combinations.combine(mode=['graph', 'eager']))
def some_test(self):
    pass

# Only run once in TF2.
@test_utils.run_v2_only
```

```py
@test_combinations.run_all_keras_modes(always_skip_v1=True)
```

```py
@parameterized.parameters("h5", "tf")
def test_keras_saving_functional(self, save_format):
    ...
    model.save(path, save_format=save_format)
```

```py
# Use tuple if you have multiple args.
@parameterized.parameters(
    ("h5", 0),
    ("tf", 1))
def test_keras_saving_functional(self, save_format, arg2):
    ...
    model.save(path, save_format=save_format)
```

```py
# Giving names to the tests with different params.
# parameters() would use the param value in the tests names.
@parameterized.named_parameters(("name1", "h5"), ("name2", "tf"))
def test_keras_saving_functional(self, save_format):
    ...
    model.save(path, save_format=save_format)
```

```py
# Exhaust all combinations of the values.
@test_combinations.generate(test_combinations.combine(
      ragged_query=[True, False],
      ragged_value=[True, False],
      ragged_key=[True, False]))
def test_ragged_tensor(self, ragged_query, ragged_value, ragged_key):
    ...
```

```py
# If you want to save the model.
def some_test(self):
    ...
    path_string = self.get_temp_dir()
    model.save(os.path.join(path_string, 'my_model'))
```
