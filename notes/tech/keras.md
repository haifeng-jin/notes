# Keras Source Code
**什么人需要读源码？**

想提升自己的程序员：阅读一个高质量的项目源代码是新手程序员快速提高自己的好方法。我从学到了很多很好的工程实践技巧，比如文件结构，代码结构，测试，文档等等。

Keras的用户：读源码可以让你从一个普通用户升级为专家用户。理解背后的运行原理能让你写的代码高效，稳定，且准确。

潜在的代码贡献者：网上大多数分析Keras源代码的文章都是针对Keras仓库中多后端的旧版本的。近几年开发的新版本的Keras一直在TensorFlow的仓库中作为tf.keras推出。然而，最近Keras又有了新动向，对Keras仓库进行了大规模更新，试图将TensorFlow仓库下的tf.keras的代码提取出来，放在其单独的仓库中，以减少工程整体的编译和测试运行时间，降低外来开源贡献者的门槛。
所以，很快Keras将开始号召开源贡献者们贡献代码，以推进项目开发进度。想要成为著名开源项目的贡献者吗？本文将帮你做好准备工作，为抓住这个机会打好基础。

**学习目标**

* 理解Keras的若干核心工作流背后的运行机制，包括：建模、训练、存储。
* 理解Keras整体的代码结构。
* 理解Keras所调用的TensorFlow的接口的作用和效果。

**学习方式**

* 我会以简单的Keras应用代码示例为线索对Keras代码进行阅读，这样能让读者更好的抓住所读代码的作用，所读代码皆是完成Keras的常用功能，浅显易懂。以防止代码细节读懂了，但却搞不清楚在全局中所起的作用。
* 对于每个示例，则是以一个纯新手的视角，以一种从已知内容出发，逐步深入探索的形式。这样可以确保学习曲线足够平滑，不会一次性涉及大量代码结构，或者突然跳转到一些未知区域。
* 本文章的内容讲采取贴核心源代码，并配合讲解的形式带大家一起阅读。
* 同时会及时讲解涉及到的TensorFlow中的重要概念和用法。

**关于作者**

我叫金海峰，是一名即将加入谷歌Keras团队的小小程序员一枚。曾在谷歌Keras团队实习一年时间，其间曾为Keras贡献代码。同时，我也是AutoKeras的作者，入职后将主要负责AutoKeras和Keras Tuner两个项目。
对于我个人来说，读源码是我入职的准备工作。

**正文开始**

## 从Sequential开始

```py
import keras

model = keras.Sequential()
model.add(keras.layers.Dense(input_shape=(10,), units=10, activation='relu'))
model.add(keras.layers.Dense(units=1))
```

### 主要的类
继承链
Sequential -> Functional -> Model -> Layer -> Module
分析之前先讲文件位置，engine，以 layers为例。
这个继承链从高到底讲，每次增加了什么功能
Module属于tf，可以追踪变量，有自己的name_scope。
为啥要追踪变量?存储和计算.

### Layer的工作原理

Layer很好理解，就是神经网络的层，变量集合，并使用这些变量构建局部计算图。
有几个函数比较重要，所有层都要重载实现它们，init build call.
init容易理解。
这几个函数是如何被调用的？

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

以Dense层为例进行讲解。

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
