# A little tutorial for the python logging module

In this exercise we will discover a little how the python logging module is working.
We will learn about 
 - logger hierachy
 - handlers
 - formatters
 


### Exercise 2 getting our first logger + handler

1. To get a logger we call `logging.getLogger(name_of_logger)`. This will return a logger, with the given name. Open `Exercise_2.py` and create a logger. Just leave the name of the logger empty, it is optional. The logger will be named `root`. Note that the level of logging has to be explicitly set after the logger is created by calling e.g. `setLevel(logging.INFO)` on the logger `INFO` can be replaced by any of the other 4 log levels.

2. On the new created logger we can call now the different methods corresponding to the 5 log levels. Log your first message on the info level, call `.info(message)` on the instance of your logger and run the script. What do you observe?

3. Correct, Nothing happens. This is because the logger does not know what to do with the message. Therefor you need to attach a handler. A handler takes the message and sends it somewhere, this can be a print in the console, a file, the cloud, ... Lets attach a handler to the logger. 

4. The first thing we need to do is to create a handler. The first handler we get to know is the `StreamHandler`. We can use this handler to print for instance to the console. Use the following line in the script to create the handler and attach it to the logger by calling `addHandler(stream)` on the newly created logger.
The stream we will use is `sys.stdout`. 
```python
console_handler = logging.StreamHandler(sys.stdout)
```

5. Run the script again. Nothing happens, but why? (Hint: Part 1 of this exercise).
Which line is missing. Add the missing line of code and run the program again. Now the log message should appear in your console


### Exercise 1 - logger hierarchy


> Each logger has a name, and they are conceptually arranged in a hierarchy by their names using dots (periods) as separators. For example, a logger named ‘scan’ is the parent of loggers ‘scan.text’, ‘scan.html’ and ‘scan.pdf’. Logger names can be anything you want, and indicate the area of an application in which a logged message originates.
>
>[src] https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial

This tutorial will show you a way to automatically set up a logger hierarchy with the help of `__name__`.

1. Print the value of the variable `__name__` by running the script `Exercise_1.py`. Variables like this `__name__` are already assigned when the program starts. 
Note down the value of  `__name__`.

2. Now import the module `fancy_ai_app/component_0.py` into `Exercise_1.py` and run it. What is the value of `__name__` in the imported file? Note, you should always look into the source code of the executed files. 

3. Assume we would use the value of `__name__` as the name of the logger in each imported file.  How would we have to name the logger in `Exercise_1.py` so it becomes a parent of all other loggers from our package fancy_ai_app?


### Exercise 3 Formatter

What is missing now is the formatter. This is giving the log a certain structure. The formatter also allows to add information such as a timestamp.

1. The formatter can be either added to the logger itself or to the handler. This is done by calling `setFormatter(formatter)` on either the logger or the handler. To do that we first need to declare a formatter. Please declare a logger in `Exercise_3.py` and add it to your logger. To declare a logger use 
```python
logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
```
The argument of the formatter defines what how the log messages log like. Attach your new formatter to the logger.

### Exercise 4 Log messages

The last things is maybe a little obvious, but we should still practie a little. Writing Log messages.

1. The first thing to practice is hitting the correct loglevel. We have the 5 standard log levels below available in python. They are in a hierarchical order, meaning if you capture logs on WARNING you also capture logs on ERROR and CRITICAL.

- CRITICAL
Any error that is forcing a shutdown of the service or application to prevent data loss (or further data loss).

- ERROR
The ERROR level should only be used when the application really is in trouble. Users are being affected without having a way to work around the issue. Someone must be alerted to fix it immediately, even if it’s in the middle of the night. There must be some kind of alerting in place for ERROR log events in the production environment.

- WARNING
The WARN level should be used when something bad happened, but the application still has the chance to heal itself or the issue can wait a day or two to be fixed. Like ERROR events, WARN events should be attended to by a dev or ops person, so there must be some kind of alerting in place for the production environment.

- INFO
The INFO level should be used to document state changes in the application or some entity within the application.

- DEBUG
In a nutshell, we want to log any information that helps us identify what went wrong on DEBUG level.

Sort the each of the following scenarios into one log level OR no log at all. 

https://forms.gle/wyGbRHuGpYiZhMNw9

