#Chapter 1: Module, Pip, & Comments:

------Module------: 
#A module is a file containing code written by someone else which can be imported used in our program. 
#A python module is like a toolbox filled with special codes.
#With the help of pip we can install any module.
------pip------:
#pip is the package manager for python, we can use pip to install a module on our program.
#syntax: pip instal + our_package_name
#Ex: pip install flask
#Ex: pip install pyjokes
------Comments------:
# (#)is use for single symbol as single line comments.
# (""" """) is used for multiline comments.
#Ex: # This is Oython programming code 
#Ex: """ Hello, Good morning. 
        I hope you are doing awesome.
        This message will find you well.
        Thank you so much for visiting my Github profile."""

#Example:
#This code will print random programmer joke in the console.
#Above we also use the comments too.
import pyjokes
print(pyjokes.get_joke())
