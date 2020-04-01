# Design Patterns
#tech/software engineering#
* Factory.
It generates objects of classes which extend the same class by checking the parameter which is the name of one of the classes. Then, these objects can be used in polymorphic. Note that if you want the factory to generate other objects besides the original ones you need to change the code of the factory.

* Abstract Factory
There is an abstract class which several factories can derive from.
Thus, they can generate different kind of objects extending different classes.

* Singleton
It is a class has only one instance which already be generated.
It can be used to store things which everybody need to access.

* Builder
It assembles different parts to form an object.

* Prototype
It cached the objects which can be load from elsewhere in it.
It serves as an intermediate layer to reduce the number of loading operations.

* Adapter
It allows the user to manage an object with interface B using the function of interface A.

* Bridge
It split a functionality out of a class using a member whose type is an interface so that the classes which implement the interface do not need to extends the original class which require to contain everything. They only need to implement the interface to have that functionality.

* Filter
It lets multiple concrete classes implementing the same filtering interface to filter the list of objects of another class.

* Composite
It uses a class A which has a member of a list of instances of A. We are able to use it as nodes to create a tree like structure.

* Decorator
It allows us to decorate an object of a class using a Decorator class which contains the object of the original class as its member and some methods to decorate the object like set its border color and so on.

* Facade
It hides the complexities of the system and provides an interface to the client using which the client can access the system.

* Flyweight
It help us to get or create the objects we want and reduce the number of objects created, too. It uses a hash-map to check whether the object we are ordering is already exist or not, depend on which the decision of whether to create one is made.

* Proxy
It is a bit like Prototype design pattern. The only difference is that it only keeps the most recent visited object in it.

* Chain of Responsibilities
It has many receivers. Each one contains another to form a chain. When the message is send to the first receiver, it decides whether to handle it or pass it to the next one.

* Command
It wraps a request in an object as a command which is to pass to the invoker. The invoker find a way to executes those command. One way to execute is that all these commands implements the same interface which contains an execute method.