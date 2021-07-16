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
It is just records the arguments from the caller in the attributes.

### build如何被调用
以lazy方式来执行，通过`_maybe_build()`。
例如，当call被调用的时候，build必须先被调用。因为会用到里面的变量。

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

### add_weight。干了啥？

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
建立变量的过程稍有点复杂,但是和直接用`tf.Variable`建立的区别不大.此处省略.
tf问题:变量建立过程.
backend如何track?

```py
def track_variable(v):
  """Tracks the given variable for initialization."""
  if context.executing_eagerly():
    return
  graph = v.graph if hasattr(v, 'graph') else get_graph()
  _GRAPH_VARIABLES[graph].add(v)
```
这里涉及到了一些tf概念,
[eager](https://www.tensorflow.org/guide/eager),
[graph](https://www.tensorflow.org/guide/intro_to_graphs).
默认都是eager。load model 是特殊情况，之后会讲。
类似于Python和C语言。解释语言于编译。

graph与variable的关系.
tf接口:
[tf.executing_eagerly()](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly)
get_graph干了啥? 通过tf接口,获取当前的计算图。
`_GRAPH_VARIABLES`是啥? 是一个dictionary，用来追踪一个graph下面所有的variable。
什么是variable？
[tensor](https://www.tensorflow.org/guide/tensor)
vs
[variable](https://www.tensorflow.org/guide/variable)？
Tensor值不可变，而Variable可变。
类似于tuple vs list.



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
