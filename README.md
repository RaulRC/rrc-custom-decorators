# rrc-custom-decorators
Custom decorators for projects

## Installation
```bash
cd rrc-custom-decorators
pip install . 
```

## Usage

### `ttime` decorator
```python
from custom_decorators import ttime

@ttime
def my_function():
    pass

my_function()
```

The output should be:

```bash
Time my_function: 0.0 s.
```

### `cache` decorator
```python
from custom_decorators import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

@ttime
def execute():
    print(fib(350))

execute()
```
```bash
6254449428820551641549772190170184190608177514674331726439961915653414425
Time execute: 0.0 s.

```
You can also ask for help:

```
import custom_decorators as cd
cd.help()
```

```bash 
 Available decorators:
    @ttime: prints the time it took to execute the function
    @cache: caches the function's result
    @loginfo: logs the function's execution
```

## License
[BSD-3-Clause](https://choosealicense.com/licenses/bsd-3-clause/)