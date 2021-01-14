# Livedemo of the python import 

Start an interactive python console and run line by line and observe the output.

```python
import sys
# This is the path which the importer is searching through.
print(sys.path)
# Try to import a native library -> it works.
import collections
# Remove all path information sys.path.
temp_path = sys.path
sys.path = []
# Collections does not throw an error ...
import collections
# ... since it is already in sys.modules.
print(sys.modules)
# When we try to import another module we get an error.
import logging
```

If we do the same procedure the other way around, we don't get an error. WHY? Open a new console and try it out

```python
import sys
# This is the path which the importer is searching through.
print(sys.path)
# First we import logging -> it works.
import logging
# Remove all path information sys.path.
temp_path = sys.path
sys.path = []
# Collections does not throw an error ...
import logging
# ... since it is already in sys.modules.
print(sys.modules)
# BUT we also don't get an error with collections, WHY?
import collections
```

Let's try something else:

```python
import sys
# Check which modules have already been imported
print(sys.modules)
# enum is in the dict but we can not acces it yet 
enum
# If a module is already loaded we can just give it the variable name
enum = sys.modules['enum']
# now we can use the library as if we would have used import enum
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
# Try the new class
print(repr(Color.RED))
```
