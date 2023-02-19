# Chromatimer
A simple python decorator that can be used to easily measure and output function execution time (with minimal extra code).  
Usage:
```
from chromatimer import chromatimer

@chromatimer()
def some_function():  
  time.sleep(0.17515731)
```

When the function *'somefunction()'* is executed, the decorator will output:
```
Function 'some_function' took 0.175s.
```

The decorator timer also has two optional parameters: *'interval'* and *'decimals'*.  
The parameter *'interval'* changes the time interval the decorator outputs.  
Available inputs for interval include: ["s", "ms", "µs", "ns"].  
Usage:
```
@chromatimer(interval='ms')
def some_function():  
  time.sleep(0.17515731)
```
Would change the previous output to:
```
Function 'some_function' took 1751.573ms.
```
The parameter *'decimals'* changes the number of decimal places the decorator outputs.  
Usage:
```
@chromatimer(decimals=5)
def some_function():  
  time.sleep(0.17515731)
```
Would change the previous output to:
```
Function 'some_function' took 0.17516s.
```
