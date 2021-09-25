# Dive into Keras source code 01

## Foreword

This is a series of articles explaining the source code of [Keras](https://keras.io/).

### Learning goals

* Understand the overall code structures.
* Understand the mechanisms behind the core workflows, including modeling, training, and saving.
* Understand the core concepts and classes in Keras and TensorFlow.
* Understand the important TensorFlow API usages in Keras codebase.

### Prerequisites

You should understand the basic usages of Keras by reading the following two tutorials.

* [Introduction to Keras for Researchers](https://keras.io/getting_started/intro_to_keras_for_researchers/).
* [Introduction to Keras for Engineers](https://keras.io/getting_started/intro_to_keras_for_engineers/).

## Modeling

The modeling API of Keras is responsible for putting the layers or TensorFlow operations together to create a model before training.

### A chain of class inheritance

Here is a simple [Sequential model](https://keras.io/guides/sequential_model/) example,
which creates a model with minimal code.
```py
import keras

model = keras.Sequential()
model.add(keras.layers.Dense(input_shape=(10,), units=10, activation='relu'))
model.add(keras.layers.Dense(units=1))
```

The `Sequential` class is a high-level class,
which has a chain of base classes.
The inheritance chain looks like this:
`tf.Module -> Layer -> Model -> Functional -> Sequential`
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

A [`tf.Variable`](https://www.tensorflow.org/guide/variable) instance is a data structure for storing a mutable tensor in TensorFlow.
The difference between a `tf.Variable` and a [`tf.Tensor`](https://www.tensorflow.org/guide/tensor)
is that
`tf.Variable` is mutable but `tf.Tensor` is not.
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
