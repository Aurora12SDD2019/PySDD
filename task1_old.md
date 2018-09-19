Lets start with the traditional `hello world` program.
In python this couldn't be simpler. Type

`print("hello world")`

and then click run.

`print()` is a *function*, and this is indicated in python by the parentheses. We will come to functions later but essentially they perform a task using the information or 'argument' supplied in the parentheses. Notice that it doesn't actually print anything just sends output to the screen.

`hello world` is a *data type* called a *string* or *str* which stands for
 a string of characters.  Characters are just letters or numbers or
 punctuation marks - things corresponding to keys on your keyboard.
 In python, strings and characters are identified by placing them in quotation marks, but the quotation marks themselves don't print.

Predict the output of the following code


Different data types can be used in different ways so it is important to know what data types you are using. You can use the function type() to determine an object's data type.

Predict the output of the following code

print(type(901))

print(type('twas brillig and the slithy toves'))

print(type(3.14159))

print(type(True))

Run the script to check your prediction.

Note: in this example we are nesting a function within a function.  We use the type() funtion to tell what the data type of each object is, then we use the print() function to show the result.

Variables
Most programming tasks involve the manipulation of variables, which are names that refer to a value, but this value can change

Predict the output of the following code

msg = 'Hello World'

print(msg)

print(type(msg))

Run the script to check your prediction.

In this example whenever you use the variable message it is exactly equivalent to using the string 'Hello World'.

Predict the output of the following code

n = 2

n = 2 * n

print(n)

Run the script to check your prediction.

Here we assign a variable, then we manipulate it  by multiplying by 2 before sending it to the print function. What differences do you predict would occur if you started the sequence above with the assignment statement

n = 2.5

Try it!

Numerical Operators
In the example above we used the operator * to multiply n by 2.  Other operands used by Python are:

    + for addition
    - for subtraction
    / for division
    ** for exponentiation.
    % for remainder or modulo


For example the statement 2**3 evaluates to 8 which is 2 cubed (2 raised to the power of 3).

Predict the output of the following code

i = 5

j = 2


print(i + j)

print(i - j)

print(i * j)

print(i / j)

print(i**j)

print(i % j)

Run the script to check your prediction.

When more than one operator appears in a statement, Python uses the normal rules of mathematical precedence PEDMAS. Parentheses Exponentiation Division & Multiplication Addition & Subtraction.


Predict the output of the following code

print(6 + 4 / 2)

Run the script to check your prediction.

String Operators
You cannot perform mathematical operations on strings, but there are two string operators.

    + for concatenation or joining together
    * for repetition


Predict the output of the following code

str = 'Spam ' #note the space after the word

str = str + str

print(str)

str = str * 3

print(str)

Run the script to check your prediction.

Variable Names
You should take the time to make your variable names meaningful so that you or anyone else reading you code can easily determine what the variable refers to. For example, if you wanted a variable to refer to a customers address it should have a name something like customerAddress. Notice that by convention the variable name starts with a lower case letter, and upper case letters are used to indicate a new word. This type of naming is called 'camel case'.

Variable names cannot contain spaces. Variable names can be arbitrarily long. They can contain both letters and numbers, but they have to begin with a letter.

Keywords
Variable names cannot be one of Python’s keywords. The interpreter uses keywords to recognise the structure of the program, and they cannot be used as variable names.

To see all of Python's keywords import the module keywords then use the command
 then at the help prompt type keywords. To leave the help function type quit.

keyword.iskeyword(s) which will return True if s is a Python keyword.

keyword.kwlist will return a list containing all the keywords defined for the interpreter.

Try this code:

import keyword


print(keyword.iskeyword("class"))


print(keyword.kwlist)


To see what happens if you try to assign a keyword to a variable name type

class = "Year 11 SDD"



</html>