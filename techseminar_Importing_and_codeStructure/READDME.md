# Importing in Python (Exercise)

The exercise consists of different parts in which we will look a little bit into the interior working of the import module.
After this tutorial debugging this error should never been an issue for you again.

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'WTF'
```

The underlying question when importing a file in python is always from where the program is started. This is the folder that is in the list of paths. Let's try it.

### Exercise 1: importing 101 (15 min)

1. Open the terminal at the location of this README file.
2. Enter `python` in order to start an interactive python console.
3. Try importing the class `FileParser` and see what happens. Try to fix the error in two separate ways.
    1. By starting the python console from a different location. Write down the path from which the program runs (hint: `pwd`) and the statements you have used to get there.
    2. By fixing the import statement in line 1 the `FileParser` File. Don't change the location of your python console this time. Note down the new line 1.
4. After the fix in line Import the `FileParser` class in the file `/file_parser/scripts/this_script.py` and run it to check whether it works. The script should run from the `.` folder.

### Exercise 2: sys.path I (15 mins)

One important variable in the importing process is `sys.path`. It stores all the paths in which the import module is searching for a module. 
1. Start python interactive console again at the location of this README file.
2. Import one native module of python (e.g. `unittest`, `collections`).
3. Import the library `sys` and look what's inside the variable sys path (hint: it's a list).
4. From which of the paths are the native modules imported? What does the empty entry in the list `['']` do? In order to answer the question, remove parts of the list `sys.path` and try to import the modules. 

### Exercise 3: Modify `sys.path` (15 mins)

In exercise 1- 3.1 we changed the location of the python console. With the newly gained knowledge about the variable `sys.path` we modify it in a way that we can run the file `FileParser_Ex3.py` from the location of this readme.

1. Open a console at the location of README.md.
2. Import sys and modify the list in `sys.path` in a way that we can run file parser. (Hint: use absolute paths here)
3. try to import the FileParser from `FileParser_Ex3.py` in your python console. 

### Exercise 4: pip  (15 mins)

1. Install the module cookiecutter via pip. ( `pip install cookiecutter`)
2. Run a terminal and repeat exercise 4 and find out which of the entries in the list is needed to find the module cookiecutter. In your python console you can use the line `import cookiecutter``
3. Go into the location which you identified as the relevant for the input of cookiecutter in your finder or explorer. (Shortcut for mac users: use `open <your-path>`).
4. Now you should see a finder windows with all the packages which you have later installed with pip. One of them should be `cookiecutter`. 

