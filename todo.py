#!/usr/bin/env C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe
import sys
import os

def fileSetup():
    if not os.path.isdir('./plans'):
        os.mkdir('./','./plans')
        
    if not os.path.isfile('./plans/todo.txt'):
        try:
            file = open('./plans/todo.txt','a')
        except OSError as error:
            sys.stdout.write(error)
            setup = 'No'
        finally:
            file.close()
            setup = 'Yes'
            
    if not os.path.isfile('./plans/done.txt'):
        try:
            file = open('./plans/done.txt','a')
        except OSError as error:
            sys.stdout.write(error)
            setup = 'No'
        finally:
            file.close()           
       

def add():  
    if setup == 'Yes':
        with open('./plans/todo.txt','r+') as file:
            task.append(file.readlines())
        sys.stdout.write(task)
        if (sys.argv[2] in task):
            sys.stdout.write("Task already exists")
            sys.stdout.write(task)
        else:
            sys.stdout.write("writing")
            with open('./plans/todo.txt','w') as file:                
                file.write(sys.argv[2])
        
def ls():
    if (setup == 'Yes'):
        if os.getsize('./plans/todo.txt'):
            with open('./plans/todo.txt','r') as file:
                task.append(file.readlines())
            for ls in task:
                sys.stdout.write(ls)
            task.clear()
        else:
            sys.stdout.write("no tasks for now")
    else:
        sys.stdout.write("The setup is not proper")

def delete():
    if setup == 'Yes':
        try:
            file = open('./plans/todo.txt','r+')
            task.append(file.readlines())
            
            if sys.argv[2] == 'done':
                with ('./plans/done.txt','w') as file:
                    file.write(task[int(sys.argv[3])])
                    
            del task[int(sys.argv[3])]
            file.write(task)
            file.close()
            sys.stdout.write(task)
        except OSError as error:
            sys.stdout.write(error)
    
def done():
    if setup == 'Yes':
        delete()
        

def myHelp():
    print("""
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
""")

def report():
    print("report")



mydict = {
            "add":add,
            "ls":ls,
            "del":delete,
            "done":done,
            "help":myHelp,
            "report":report
        }

fileSetup()

if len(sys.argv) == 1:
    print("""
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
""")

task = []
setup = ''

if len(sys.argv)>1:
    func = mydict[sys.argv[1]]
    func()
    task.clear()
