# Handy Reference

This list is intended to provide awareness and jog your memory.
For details, refer to the official documentation as needed.

Many of these functions expect you to pass in some parameters!  
**They are not shown here** so that you get practice at looking up
these kinds of details as needed.

Functions starting with a period, i.e. `.split()`, are _methods_
of a specific type of object. Methods can only be invoked against
an object of that type using the dot operator.  For example:

```
  fruits = "apples,bananas,cherries"
  fruits.split()
```

### Built-in Functions

* `input()`
* `len()`
* `min()`
* `max()`
* `sorted()`
* `type()`
* `id()`
* `isinstance()`
* `dir()`

You can use the _membership operator_ `in` to test for element existence in a collection or sequence:

```
colors = ["red", "purple", "orange"]

if "red" in colors:
  print("That's my favorite color!")
```


### The `__main__` module

It is standard practice for modules that can run as a
main script to use the special variable `__name__` to check
to see if the current module is being executed as the main program,
rather than being imported as a module.

```
...
...

if __name__ == '__main__':
  # Running as the main program ...
  statements
  ...
```

### `str`

* .split()
* .upper()
* .lower()
* .strip()
* .replace()
* .startswith()
* .endswith()
* .find()

Remember, there is no `.length()` method. Use the built-in function `len()` to get the length of a string.


### `list`

* .append()
* .insert()
* .remove()
* .sort()
* .pop()

You can also use the built-in function `del` to remove an element by position index.

### Files

* `open()`
* `.read()`
* `.readline()`
* `.write()`
* `.close() `


Modern Python style uses the `with...as...` construct instead of manually calling
.close`:

```
# Reads an entire file into the variable 'data'
with open("myfile.txt", "r") as f:
  data = f.read()
```

To process an entire file one line at a time:

```
with open("myfile.txt", "r") as f:
  for line in f:
      # do something with line
```


### Loops

```
while (some_condition):
  # do something here
```

```
for var in collection:
  # do something with var
```
