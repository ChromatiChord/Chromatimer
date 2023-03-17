# Chromatimer
A simple python decorator that can be used to easily measure and output function execution time (with minimal extra code).  
Usage:
```
from chromatimer import chromatimer

@chromatimer()
def some_function():  
  time.sleep(0.17515731)
```

When the function *'some_function()'* is executed, the decorator will output:
```
Function 'some_function' took 0.175s.
```

The decorator timer also has the optional parameters: *'interval'*, *'decimals'*, *'output'*, and *'history'*.  


## Interval
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


## Decimals
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


## Output
Decorator output can be disabled completely using the *'output'* argument.
```
@chromatimer(output=False)
def some_function():  
  ...
```


## History
If a dictionary is provided within the *'history'* argument, any time recorded by the decorator will be added to that dictionary.  
Example:
```
history_dict = {}
time_quantity = 1.1

@chromatimer(output=False, history=history_dict)
def some_function():  
  time.sleep(time_quantity)
  
some_function()
time_quantity = 2.3
some_function()
```
When the function(s) has been executed, the *history_dict* variable will be set to:
```
{
  some_function: {
    'interval': 's',
    'times': [1.1, 2.3]
  }
}
```
