# Dive into Keras source code 03

### The `Model` class

[[Source](https://github.com/keras-team/keras/blob/v2.6.0/keras/engine/training.py#L103)]

The `Model` class is a subclass of `Layer`.
In the following workflow,
the `Model` class is not so different from the `Layer` class if you see it as a way to group layers together to build a computational graph.

```py
class MyModel(tf.keras.Model):
  def __init__(self):
    super(MyModel, self).__init__()
    self.dense1 = tf.keras.layers.Dense(4, activation=tf.nn.relu)
    self.dense2 = tf.keras.layers.Dense(5, activation=tf.nn.softmax)
    self.dropout = tf.keras.layers.Dropout(0.5)
  def call(self, inputs, training=False):
    x = self.dense1(inputs)
    if training:
      x = self.dropout(x, training=training)
    return self.dense2(x)
```

However, it add a set of functions and attributes that related to training, for example. `compile()`, `fit()`, `evaluate()`, `predict()`, `optimizer`, `loss`, `metrics`,
which we would go into more details when we introduce the training APIs.
In summary, a `Model` can be trained by itself, but a `Layer` cannot.


### The `Functional` class

There is another way of using the `Model` class besides subclassing it,
which is the functional API as shown in the following example.

```py
inputs = tf.keras.Input(shape=(3,))
x = tf.keras.layers.Dense(4, activation=tf.nn.relu)(inputs)
outputs = tf.keras.layers.Dense(5, activation=tf.nn.softmax)(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

Although it looks like it is still using the `Model` class, it is actually using the `Functional` class.
In `Model.__new__()`, it creates a `Functional` instance if using the functional API.
The source code looks like this.

```py
class Model(Layer):
  def __new__(cls, *args, **kwargs):
    if is_functional_model_init_params(args, kwargs) and cls == Model:
      return functional.Functional(skip_init=True, *args, **kwargs)
```
[[Source](https://github.com/keras-team/keras/blob/v2.6.0/keras/engine/training.py#L189)]

Now, let's see how `Functional` is tracking these layers and intermediate outputs in the computational graph.

#### `KerasTensor`

`keras.Input()`, which looks like a class, but acutally is a function, which returns a `KerasTensor` object.

```py
print(type(keras.Input(shape=(28, 28, 1))))
```

Outputs:

```
<class 'keras.engine.keras_tensor.KerasTensor'>
```

`KerasTensor` is a class just to represent the intermediate output tensors of the layers in a Keras model,
which has some useful property like `shape` and `dtype`.

```py
class KerasTensor(object):
  @property
  def shape(self):
    ...
  @property
  def dtype(self):
    ...
```
[[Source](https://github.com/keras-team/keras/blob/v2.6.0/keras/engine/keras_tensor.py#L30)]

It is passed to each of the layers by calling them as shown in the functional API example.
The purpose is for the layers to create the weights using the shape and type information of the input tensor.
That is also why we have a special judge to see if the input tensor is a `KerasTensor` in `Layer.__call__()` as we introduced before.

```py
class Layer(module.Module, ...):
  def __call__(self, inputs, **kwargs):
    if isinstance(inputs, keras_tensor.KerasTensor):
      inputs = convert_to_tf_tensor(inputs)
      outputs = self.call(inputs)
      return convert_to_keras_tensor(outputs)
```

From the source code above, we can see if we call a layer with a `KerasTensor`, the return value is also a `KerasTensor`,
which will be used to call the next layer.

