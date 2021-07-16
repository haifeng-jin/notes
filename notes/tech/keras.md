# Keras Source Code
**为什么要读源码？**

2021年，Keras进行了大规模更新，将TensorFlow仓库下的tf.keras的代码提取出来，放在其[单独的仓库中](https://github.com/keras-team/keras)，现在几分钟就能在本地把测试全部跑完，贡献代码变得十分简单。
所以，很快Keras将开始号召开源贡献者们贡献代码，以推进项目开发进度。
想要成为著名开源项目的贡献者吗？本文将帮你解析最新版本的Keras源码，做好准备工作，为抓住这个机会。
如果你不打算贡献代码，这也是一份能帮你提升Python深度学习工程能力，成为Keras和TensorFlow专家的教程。

**学习目标**

* 理解Keras的若干核心工作流背后的运行机制，包括：建模、训练、存储。
* 理解Keras整体的代码结构。
* 理解Keras所调用的TensorFlow的接口的作用和效果。

**学习方式**

* 以简单的Keras的API为线索来进行阅读，了解平时用Keras的时候背后发生了什么。
* 采取贴核心源代码，并配合讲解的形式。

**关于作者**

我叫金海峰，是谷歌Keras团队的一个中国小哥。是AutoKeras和KerasTuner的项目负责人。
对于我个人来说，读源码是我入职的准备工作。

**正文开始**

在阅读本文之前，建议先阅读[新版Keras快速教程](https://zhuanlan.zhihu.com/p/380472423)，以了解Keras的基本用法。

## 从Sequential开始
Sequential API是Keras最简洁的建模接口。
如下代码帮我们建立了一个两层由全连接层组成的神经网络。
```py
import keras

model = keras.Sequential()
model.add(keras.layers.Dense(input_shape=(10,), units=10, activation='relu'))
model.add(keras.layers.Dense(units=1))
```
接下来我们就试图搞清楚这段代码在运行过程中发生了什么。

### 主要的类
`Sequential`是一个比较高级的类，它继承了基类，基类又有基类。组成了一个继承链条。
主要涉及到了如下五个类：

`Sequential -> Functional -> Model -> Layer -> Module`

其中，箭头表示类之间的继承关系。
接下来我们按照从基类到子类的顺序来讲解，看看每个子类在基类的基础上增加了什么，这个链条也就清晰了。

我们先来看最基的基类Module。([源码链接](https://github.com/tensorflow/tensorflow/blob/v2.5.0/tensorflow/python/module/module.py#L35))

它是TensorFlow中的一个很核心的类，可以看成是一个`Variable`的容器。
`tf.tf.Variable`是TensorFlow用来存储张量的一个类，通常用来存储神经网络的权重。
关于`tf.Variable`类后文我们还会讲到。
这个容器的一种常见用法就是用来构建一个神经网络的层。
我们可以使用`tf.Module`的`name_scope`属性给属于这个容器的`tf.Variable`一个命名空间。
这样所有这些`tf.Variable`都会以这个`Module`的名字作为前缀。

```py
import tensorflow as tf

constant_tensor = tf.constant([10, 20, 30])
class MyModule(tf.Module):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    with self.name_scope:  # 开启命名空间
      self.variable = tf.Variable(constant_tensor, name="my_variable")  # 在空间中建立变量

print(MyModule(name="my_module").variable)  # 发现变量名为"`Module`名字/`Variable`名字:计数"的形式
```
输出：
```
<tf.Variable 'my_module/my_variable:0' shape=(3,) dtype=int32, numpy=array([10, 20, 30], dtype=int32)>
```

`tf.Module`类上面还继承了`tf.Trackable`类，可以用来追踪容器里面的所有变量。
在我们想把模型保存到硬盘的时候，方便进行存储。

### Layer的工作原理

在我们讲解Layer的工作原理之前，我们先来看看所有Layer相关的类的代码都放在哪些文件里。
分析之前先讲文件位置，engine，以 layers为例。
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
