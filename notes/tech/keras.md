# Keras Source Code

## Foreword

This is a article explaining the source code of [Keras](https://keras.io/).

### Teaching style

* Guided by some typical Keras workflows, explaining the source code behind the APIs.
* The source code from the codebase are quoted with links and explained.

### Learning goals

* Understand the overall code structures.
* Understand the mechanisms behind the core workflows, including modeling, training, and saving.
* Understand the important TensorFlow API usages in Keras codebase.

### Prerequisites

You should understand the basic usages of Keras by reading the following two tutorials.

* [Introduction to Keras for Researchers](https://keras.io/getting_started/intro_to_keras_for_researchers/).
* [Introduction to Keras for Engineers](https://keras.io/getting_started/intro_to_keras_for_engineers/).

## Modeling

This is the first article of in a series of articles.
In this article, we focus on the modeling API of Keras,
which put the layers or TensorFlow operations together to form a model before training.

### Starting from the Sequential API
We start from a simple Sequential API example,
which creates a model with minimal code.
```py
import keras

model = keras.Sequential()
model.add(keras.layers.Dense(input_shape=(10,), units=10, activation='relu'))
model.add(keras.layers.Dense(units=1))
```
Let's see what happens when running the code.

### A chain of class inheritance

The `Sequential` class is a high-level class,
which has a chain of base classes.
The inheritance chain looks like this:
`tf.Module -> Layer -> Model -> Functional -> Sequential `
The class on the left of an arrow is the base class of the one on the right.

To understand this chain of classes,
we start from the base classes
to see what functionality has been added step-by-step by the subclass down the chain.

### The `tf.Module` class
[[Source](https://github.com/tensorflow/tensorflow/blob/v2.5.0/tensorflow/python/module/module.py#L35)]

The first base class to dive into is the `tf.Module` class,
which is a core class in TensorFlow.
It is used by Keras.
You can think it as a container for `tf.Variable` instances.

A `tf.Variable` instance is a data structure for storing a mutable tensor in TensorFlow,
which will talk more later.
The weight of a layer is a `tf.Variable` instance.

什么是variable？
[tensor](https://www.tensorflow.org/guide/tensor)
vs
[variable](https://www.tensorflow.org/guide/variable)？
Tensor值不可变，而Variable可变。
类似于tuple vs list.

A typical usage of the `tf.Module` class is to group a series of operations on the tensors together,
for example, a neural network layer.
It has an attributed called `name_scope`,
which is used as the prefix for the names of its `tf.Variable` instances.

```py
import tensorflow as tf

constant_tensor = tf.constant([10, 20, 30])
class MyModule(tf.Module):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    with self.name_scope:  # Open the name space.
      self.variable = tf.Variable(constant_tensor, name="my_variable")  # Create in the name space.

print(MyModule(name="my_module").variable)  # The format of the name is "`module_name/variable_name:counter`"
```

Output:

```
<tf.Variable 'my_module/my_variable:0' shape=(3,) dtype=int32, numpy=array([10, 20, 30], dtype=int32)>
```

Because it is not part of the Keras codebase, we will not dive into the implementation of it.
Another feature of the class is that it inherits the `Trackable` class, which tracks all the `tf.Variable` instances in the attributes of the subclasses of `tf.Module`.
When saving the models, all the `tf.Variable` instances inside this container can be found and saved.
The variables are also tracked for optimizing the computational graph.

### The file locations

Before we show how the `Layer` class works,
let's first see where are the code of the base `Layer` class and the subclasses are, like `Conv2D`,
because this is a very typical case for the code locations in Keras.
The base `Layer` class is in `/keras/engine/base_layer.py`,
while the subclasses are in the `/keras/layers` directory.

The base classes,
which builds the Keras overall framework,
are in the `/keras/engine` directory.
The implementation of each of the subclasses are in their own corresponding directory.
The file location logic can You can navigate through the codebase.

### The `Layer` class

[[Source](https://github.com/keras-team/keras/blob/r2.6/keras/engine/base_layer.py#L84)]

The `Layer` class is easy to understand.
It is the base class for the neural network layers in Keras.
Here is a simple example of inheriting the `Layer` class to build a custom layer.

```py
  class SimpleDense(Layer):
    def __init__(self, units=32):
        super(SimpleDense, self).__init__()
        self.units = units
    def build(self, input_shape):
        self.w = self.add_weight(shape=(input_shape[-1], self.units),
                                 initializer='random_normal',
                                 trainable=True)
        self.b = self.add_weight(shape=(self.units,),
                                 initializer='random_normal',
                                 trainable=True)
    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b
```

From this example, we can see that a `Layer` instance is a collection of tensors and computations about the tensors in its attributes and the input tensors.
There are 4 methods worth noting in the example.
They are `__init__`, `build`, `add_weight`, and `call`.
Let's see how they work one by one.

The `__init__` function is easy to understand.
It just records the arguments from the caller with the attributes.

#### `Layer.build` function
[[Source](https://github.com/keras-team/keras/blob/r2.6/keras/engine/base_layer.py#L440)]

The `build` function is to create the `tf.Variable`s in the layer,
which are the weight and bias in the example above.
Because the `tf.Variable`s  are used by the `call` function,
it would have to be created before the `call` function is called.
Moreover, we don't want the variables to be created multiple times.
The question we want to answer here is how the build function is called under the hood.

A lazy mechanism is implemented for `build` with the `Layer._maybe_build()` function,
whose core logic is shown as follows.
The `Layer` instance would use the `self.built` attribute to record
whether `build` has been called.
Any code that would need the layer to be built would call this `_maybe_build` function to ensure 
the layer is built.

```py
def _maybe_build(self, inputs):
  ...
  if not self.built:
    ...
    input_shapes = tf_utils.get_shapes(inputs)
    ...
    self.build(input_shapes)
    ...
  ...
```

The `tf_utils.get_shapes(inputs)` is a function in Keras to get the shapes of the input tensors.

Here is an example of calling `_maybe_build` secretly.
We create a layer.
We call the layer with a tensor without explicity calling `build`.

```py
layer = SimpleDense(4)
layer(tf.ones((2, 2)))
```

Output:

```
<tf.Tensor: shape=(2, 4), dtype=float32, numpy=
array([[ 0.02684689, -0.07216483, -0.04574138,  0.03925534],
       [ 0.02684689, -0.07216483, -0.04574138,  0.03925534]],
      dtype=float32)>
```

The example runs successfully
because the layer call would call the `__call__` function, which
calls the `call` function.
Before calling the `call` function, `__call__` would call `_maybe_build` first to ensure the `tf.Variable`s are created.
The pseudo code is shown as follows.

```py
class Layer(module.Module, ...):
  def __call__(self, inputs, **kwargs):
    ...
    self._maybe_build(inputs)
    ...
    self.call(inputs)
    ...
```
[[Source](https://github.com/keras-team/keras/blob/r2.6/keras/engine/base_layer.py#L1030)]

This lazy pattern appears many times in Keras source code.
When ensuring something is called and don't want it to be called multiple times,
you should use this pattern. 


### `Layer.add_weight` function

[[Source](https://github.com/keras-team/keras/blob/r2.6/keras/engine/base_layer.py#L528)]

We would also like to see how these `tf.Variable` been created in the `add_weight` function.
Here is the pseudo code for the core logic of the `add_weight` function.

It creates the variable and ask the backend to track the variable.
The variable will be append to different lists depending on if it is trainable.

```py
class Layer(module.Module, ...):
  def add_weight(self, ...):
    ...
    variable = ...  # Create the variable.
    backend.track_variable(variable)  # Track the variable.
    if trainable:
      self._trainable_weights.append(variable)
    else:
      self._non_trainable_weights.append(variable)
```

The process for creating the variable is a function call, which is not so different from using `tf.Variable(...)` to directly create the variable.
The code is complicated.
You can refer to the following link for more details.
[[Source](https://github.com/keras-team/keras/blob/r2.6/keras/engine/base_layer.py#L647)]

We need the backend to track the variable for model saving and computation optimization.
Now, the question is how the backend is tracking the variable.
The code is shown as follows.

```py
def track_variable(v):
  """Tracks the given variable for initialization."""
  if context.executing_eagerly():
    return
  graph = v.graph if hasattr(v, 'graph') else get_graph()
  _GRAPH_VARIABLES[graph].add(v)
```

[[Source](https://github.com/keras-team/keras/blob/433eaa00677c08bf01bc14f9767af365bd2a03fc/keras/backend.py#L1072)]

We encountered two important concepts:
[eager mode](https://www.tensorflow.org/guide/eager) and [graph mode](https://www.tensorflow.org/guide/intro_to_graphs).
You can click the link for detailed introductions.

Here is a short explaination.
You can think eager execution as plain Python code execution.
The tensors are all concrete values instead of placeholders.
The operations are read and executed only when we run that line of code in the Python interpreter.

However, in graph mode, all the tensors and operations are collected in advance to build the computational graph
before any actual value is input for computation.
The graph is then optimized for better execution speed.
It is similar to a compiled language, like the C programming language,
which you can turn on various optimization options to make the compiled executable file run faster.

> **_TensorFlow API_** 
`tf.executing_eagerly()` is to check whether TensorFlow is running in eager mode or not.
[[Link](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly)]

By default, everything runs in eager mode.
As shown in the code above,
in eager mode, we don't need to track the variables because it would not compile the computation graph.

graph与variable的关系.
get_graph干了啥? 通过tf接口,获取当前的计算图。
`_GRAPH_VARIABLES`是啥? 是一个dictionary，用来追踪一个graph下面所有的variable。



### call如何被调用

这里我们可以使用layer的另一个使用方法。

```py
import tensorflow as tf
import numpy as np

layer = tf.keras.layers.Dense(input_shape=(10,), units=15)
x = np.random.rand(20, 10)
output = layer(x)
print(output.shape)  # (20, 15)
```

其中`layer(x)`一句实际上是调用了`__call__()`函数，
而`__call__()`一定是调用了`call()`才能让自定义layer也能这样用。
有三种被调用的模式，Keras Tensor, graph, eager.
检查当前是哪种状况。
什么是Keras Tensor?
区别于tf.Tensor。专门用于记录建模过程中的中间输出的相关信息，例如shape。从而让用户建模接口与实际执行，更加低耦合。

graph和eager由当前的context决定，默认都是eager，如果是graph，会把call函数进行转化，转化成graph。
伪代码如下。
```py
class Layer(module.Module, ...):

  def __call__(self, inputs, **kwargs):

    if isinstance(inputs, keras_tensor.KerasTensor):
      inputs = convert_to_tf_tensor(inputs)
      outputs = self.call(inputs)
      return convert_to_keras_tensor(outputs)

    if isinstance(inputs, np.ndarray):
      inputs = tf.Tensor(inputs)

    if context.executing_eagerly():
      return self.call(inputs)
    else:
      call_fn = convert_to_tf_function(self.call)
      return call_fn(inputs)
```
tf.function就是将function编译成graph的过程。

### Model怎样组织了这些layer
