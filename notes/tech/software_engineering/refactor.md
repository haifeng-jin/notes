# Refactor
#tech/software engineering#
**Day 1:**

Creating Instance:
If the instance requires a lot of code to be created, do not create it using the constructor.
The constructors should be short.
Create it with a Creation method, which is a static method that returns an instance of the class.

When there are multiple constructors that overlap each other, we should write a general purpose constructor.
The general constructor should be called in other constructors by writing "this(...)" in the first line.

Extracting methods:
Local variables sometimes have the same use as a extracted function.
The key factor deciding whether to use a local variable or extract a function is whether it would make the code more readable.
Local variables should be final. Since it is not wise to change the value of a local variable.
If you need to calculate a value in several steps, create temporary variables for each step, so that every variable name is meaningful as the assigned value to it.

**Day 2:**

Use exceptions for switch to make sure the arguments are legal.
switch (a) {
case ...
case ...
default:
throw IllegalArgumentException("Invalid ...");
}

Use java reflection to do Factory design pattern.
return (Customer) Class.forName(name).newInstance();

Use java reflection to do Singleton design pattern when you have multiple classes are singleton.
Class[] params = Class[]{String.class, Integer.class}
Method method = Class.forName(singleton).getMethod(methodName, params}.
method.invoke(null, new Object[]{"", 0});
[http://www.newthinktank.com/2013/01/code-refactoring-5/](http://www.newthinktank.com/2013/01/code-refactoring-5/)

**Day 3:**

We can use the strategy pattern to extract a part of the class.
If we have different salary strategies for different employees.
Several types of employees may share the same salary strategy.
The subclasses of Employee should not just override a function of calculateSalary(), but have a member of PayType which is an interface.
Then we have different classes implementing the interface for different calculation for salaries.
[http://www.newthinktank.com/2013/01/code-refactoring-7/](http://www.newthinktank.com/2013/01/code-refactoring-7/)

Template pattern is used to simplify the code for several classes has common operations, but some of them may omit some steps of the operations.
[http://www.newthinktank.com/2013/01/code-refactoring-8/](http://www.newthinktank.com/2013/01/code-refactoring-8/)

If we have an instance of the subclass, call a function of the superclass g(). The superclass function g() call a override function f(). The f() would be the one in the subclass instead of in the super class.
But if f() is not a function but a member int f, the superclass function g() can never access the int f in the subclass.

**Day 4:**

Composite pattern
There should be an abstract class as the superclass for the leaf and normal nodes in the tree.
[http://www.newthinktank.com/2013/01/code-refactoring-9/](http://www.newthinktank.com/2013/01/code-refactoring-9/)

Builder Pattern
There is a Sandwich which has a lot of attributes.
The Builder has a bunch of methods, each of which set one of the attributes.
Builder is an abstract class. There should be different kinds of builder extending the Builder class.
Each kind of builder is used to make a specific kind of sandwich.
The subBuilder would implement the methods to set a specific value to the sandwich attributes.
There should be an Artist class which calls the Builder's methods in order to make the sandwich.
[http://www.newthinktank.com/2013/01/code-refactoring-10/](http://www.newthinktank.com/2013/01/code-refactoring-10/)  

The difference between Builder and Template is as follows.
Builders are subclasses extending the sandwich builder class to set different values to variables in Sandwich.
Templates need a bunch of subclasses of Sandwich each of which override the functions of Sandwich to set the values.
In one word, Builder is for more complicated objects.

There is also a way to use Builder pattern to build Composite pattern.

Using builder pattern is also a way to decouple the unit tests from he constructor of the classes.
The most typical case is like this.
One class is representing one row of data in the database table, whose constructor takes all the parameters to fill in
each column of the row.
The database is subject to change. So the constructor is subject to change.
If we use the constructor in unit tests, when we wanna change the database schema, it is not easy to do, because we need to change all the unit tests which used that class.
In stead of using the constructor we should use builder pattern.

The builder pattern can also return "this" for every set operation.
[http://www.javaworld.com/article/2074938/core-java/too-many-parameters-in-java-methods-part-3-builder-pattern.html](http://www.javaworld.com/article/2074938/core-java/too-many-parameters-in-java-methods-part-3-builder-pattern.html)
[http://rdafbn.blogspot.com/2012/07/step-builder-pattern_28.html](http://rdafbn.blogspot.com/2012/07/step-builder-pattern_28.html)
This is also know as the step-builder.