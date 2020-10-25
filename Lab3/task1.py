#1)
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

#In my opinion, we do not have to use semicolons when we are defining the variables or we are assigning value to 'result' variable.
#The second point is that brackets in if function are redundant.
#This is the right implementation:
x = 2
y = 3
if x > y:
    result = x
else:
    result = y
#2)
for i in "qwerty": if ord(i) < 100: print (i)
#In first look we can see that this code is not compiling, due to the fact that it is not syntactically correct.
#On second view we have to delete white space between print function and brackets. What is more we must move if function to new line under the for loop
#This is the right implementation:
for i in "qwerty":
    if ord(i) < 100:
        print(i)
#3)
for i in "axby": print (ord(i) if ord(i) < 100 else i)
#Code is not precisely correct we must remove white space between print function and move this function to the new line
#Corect:
for i in "axby":
    print(ord(i) if ord(i) < 100 else i)