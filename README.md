The AirBnB Project
    Description
    ===========
The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won't implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
A website (the front-end) that shows the final product to everybody: static and dynamic
A database or files that store data (data = objects)
An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

   Steps-
You won't build this application all at once, but step by step.

Each step will link to a concept:

1-The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction My  How they are stored and . This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

2-Web static
learn HTML/CSS
create the HTML of your application
create template of each object

3-MySQL storage
replace the file storage by a Database storage
map your models to a table in database by using an O.R.M.

4-Web framework - templating
create your first web server in Python
make your static HTML file dynamic by using objects stored in a file or database

5-RESTful API
expose all your objects stored via a JSON web interface
manipulate your objects via a RESTful API

6-Web dynamic
learn JQuery
load objects from the client side by using your own RESTful API

     THe command interpreter - Description
The CMD module makes it easy to make command line interfaces in your programs. These line-oriented command interpreters are often useful for test harnesses, administrative tools and prototypes that will later be wrapped in a more sophisticated interface.

Starting the interpreter-
Once you have defined your own interpreter class, the only thing left to do is to create an instance and to call the mainloop method:

interpreter = MyCmdInterpreter()
interpreter.cmdloop()
In python 2.1 and 2.2 (and possibly some older, as well as future releases?) mainloop() has been renamed to cmdloop()

Using the Interpreter-
The interpreter uses a loop to read all lines from its input, parse them, and then dispatch the command to an appropriate command handler. Input lines are parsed into two parts. The command, and any other text on the line. If the user enters a command foo bar, and your class includes a method named do_foo(), it is called with "bar" as the only argument.

The end-of-file marker is dispatched to do_EOF(). If a command handler returns a true value, the program will exit cleanly. So to give a clean way to exit your interpreter, make sure to implement do_EOF() and have it return True.
Run the interpreter interactively.

Example- This simple example program supports the command:

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, line):
        print "hello"
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()