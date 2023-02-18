# PythonTimerDecorator
A simple python decorator that can be used to easily time your functions (with minimal extra code).  
Usage:
```
from decoratortimer import decorator_timer

@decorator_timer()
def some_function():  
  ...
```

When the function *'somefunction()'* is executed, the decorator will output:
```
Function 'some_function' took 2.175s.
```

The decorator timer also has the optional parameter 'interval', which changes the time interval the decorator outputs.  
Available inputs for interval include: ["s","ms","µs","ns"]
