# Portfolio Python Documentation
This Repo stores Python projects I've used to learn the Python scripting language.

The main reference for learning Python can be [found here](https://www.python101.pythonlibrary.org/intro.html).

# Table of Contents
* [Python Classes](#python-classes)
  * [Class](#class)
  * [Generator](#generator)
  * [Enumerator (Enum)](#enumerator)
* [Installing Packages](#installing-packages)

# Python Classes
Classes are bundles of data and functionality.

## Class
To make it available, define a class:
```
class MyClass:
    """A simple example class"""
    i = 12345

    def function(self):
        return 'hello world'
```

Define `__init__()` to automatically invoke code/allow class inputs upon class instantiation:
```
class MyClass:
    """A simple example class"""
    def __init__(self, name):
        self.name = name # Allow inputs to the class during instantiation

    self.date = [] # This will only ever be [], not set during instantiation
    calender = "version_1.0" # This will be shared across all class instances 

    def function(self):
        return 'hello world'
```

To use it, instantiate the class:
```
instanceOfMyClass = MyClass()
```

To obtain or change the stored value `i` above, access the int attribute of the class:
```
print(instanceOfMyClass.i)

# Output: 12345

instanceOfMyClass.i = 10
print(instanceOfMyClass.i)

# Output: 10
```

To use the method named `function` above:
```
instanceOfMyClass.f()

# Output: hello world
```

## Generator

## Enumerator


# Installing Packages

## Pip
Package management system used to install and manage software packages.

## Python Egg Files
[Python 101: Python Egg](https://www.python101.pythonlibrary.org/chapter38_eggs.html)

**NOTE:** Python Egg's are being replaced with [Python Wheel's](#python-wheel).

A 'Python Egg' is a logical structure embodying the release of a specific version of a Python
project, comprising its code, resources, and metadata. Multiple formats to encode them. A key
principle of a Python Egg is that it should be easily discoverable and importable. That is,
it should be possible for a Python application to easily and efficiently find out what eggs are
present on the system and ensure contents are importable.

## Python Wheel
[Python 101: Python Wheel](https://www.python101.pythonlibrary.org/chapter39_wheels.html)

They are a nice way to create a local repository of dependencies for your project(s) that you can install quickly.
You could create several different wheel repositories to easily switch between different version sets for testing purposes.
When combined with virtualenv, you have a really easy way to see how newer versions of dependencies could affect your project without needing to download them multiple times.