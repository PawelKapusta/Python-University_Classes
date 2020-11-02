X = "qwerty"

def func():
    print X

func()

#Missing () in function print, so it will print error in console, if we fix this, it will print "qwerty"

X = "qwerty"

def func():
    X = "abc"

func()
print X

#As in before task, missing () in function print, so it will print error in console, if we fix this, it will print "qwerty"

X = "qwerty"

def func():
    global X
    X = "abc"

func()
print X

#As in before task, missing () in function print, so it will print error in console, if we fix this, it will print "abc"