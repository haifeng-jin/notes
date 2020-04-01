# Unit Testing
#tech/software engineering#
## Mockito
Car car = new Car();
car.manager = mock(Manager.class);
when(manager.getServerPermission()).thenReturn(true);
in startEngine() will call getServerPermission()
car.startEngine();
veryfy(car.manager).getServerPermission();
car.setMiles(4);
assert(4, car.getMiles());

## JUnit
```
@Test(expected = IndexOutOfBoundsException.class) 
public void empty() { 
     new ArrayList<Object>().get(0); 
}
```
For DAO layer classes, we may want to create a super class or interface for it.
When testing any other classes that calls DAO, we just mock the DAO by implementing its interface.
How to test DAO layer:
[http://howtodoinjava.com/best-practices/how-you-should-unit-test-dao-layer/](http://howtodoinjava.com/best-practices/how-you-should-unit-test-dao-layer/)
A very good example involves mock and anonymous class:
[http://stackoverflow.com/questions/5577274/testing-java-sockets](http://stackoverflow.com/questions/5577274/testing-java-sockets)