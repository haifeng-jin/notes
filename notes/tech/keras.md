# Keras Source Code
**为啥要读源码？**

对于普通人来讲，阅读这个项目的源码可以帮你提升Python软件工程能力，提升对代码结构的掌控力，完成从小型项目到中型乃至大型项目的跨越。提升对深度学习使用场景的理解。

网上大多数分析Keras源代码的文章都是针对Keras仓库中多后端的旧版本的。近几年开发的新版本的Keras一直在TensorFlow的仓库中作为tf.keras推出。然而，最近Keras又有了新动向，对Keras仓库进行了大规模更新，试图将TensorFlow仓库下的tf.keras的代码提取出来，放在其单独的仓库中，以减少工程整体的编译和测试运行时间，降低外来开源贡献者的门槛。

所以，很快Keras将开始号召开源贡献者们贡献代码，以推进项目开发进度。想要成为著名开源项目的贡献者吗？本文将帮你做好准备工作，为抓住这个机会打好基础。

**学习目标**

* 理解Keras的若干核心工作流背后的运行机制，包括：建模、训练、存储。
* 理解Keras整体的代码结构。
* 理解Keras所调用的TensorFlow的接口的作用和效果。

**学习方式**

* 我会以简单的Keras应用代码示例为线索对Keras代码进行阅读，这样能让读者更好的抓住所读代码的作用，所读代码皆是完成Keras的常用功能，浅显易懂。以防止代码细节读懂了，但却搞不清楚在全局中所起的作用。
* 对于每个示例，则是以一个纯新手的视角，以一种从已知内容出发，逐步深入探索的形式。这样可以确保学习曲线足够平滑，不会一次性涉及大量代码结构，或者突然跳转到一些未知区域。
* 本文章的内容讲采取贴核心源代码，并配合讲解的形式带大家一起阅读。

**关于作者**

我叫金海峰，是一名即将加入谷歌Keras团队的小小程序员一枚。在谷歌实习期间曾为Keras贡献代码，并参与了很多内部讨论。同时，我也是AutoKeras的作者，入职后将主要负责AutoKeras和Keras Tuner两个项目。
对于我个人来说，读源码是我入职的准备工作。

**正文开始**

从Sequential开始
```py
import keras

model = keras.Sequential()
model.add(keras.layers.Dense(input_shape=(10,), units=10, activation='relu'))
model.add(keras.layers.Dense(units=1))
```

继承链
Sequential -> Functional -> Model -> Layer -> Module
分析之前先讲文件位置，engine，以 layers为例。
这个继承链从高到底讲，每次增加了什么功能
Module属于tf，可以追踪变量，有自己的name_scope。
为啥要追踪变量?存储和计算.
Layer很好理解，就是神经网络的层，变量集合，并使用这些变量构建局部计算图。
有几个函数比较重要，所有层都要重载实现它们，init build call.
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
 add_weight。干了啥？

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
这里涉及到了一些tf概念,eager, graph.
graph与variable的关系.
tf接口:tf.executing_eagerly()
get_graph干了啥?
