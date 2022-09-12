# CS-4395-Natural-Language-Processing-Portfolio
Repository for the course CS 4395 (Natural Language Technologies) at UTD 

## Overview of NLP
This is a document that provides a quick rundown of what NLP is and my personal interest in the concept. You can see that document here: [overview document](Overview_of_NLP.pdf) 

## Assignment 1: Text Processing with Python

This assignment was a basic **text processing** assignment that was about formatting employee information. This assignment used **Python** as the programming language and utilized sysargs, various string functions (split(), capitalize(), strip(), etc), regular expression, the dictionary data structure, a class, and pickle files. 

The program written for this assignment ([program](Homework1/Homework1_jao180007.py)) reads an input file [data.csv](Homework1/data/data.csv), processes the text to standardize it, creates an object for each person with corrections from the user, and outputs each person's information.

The user will need to set a system argument as the pathname of the data file, should be "data/data.csv", which the progam confirms. After which the user will be prompted to correct any errors in the information from the input file by typing in new information into the terminal. After all of the information matches the specified format the program prints a list of all the corrected employee information. 

### The Specified Formatting

The original documentation specifies a format for the correct employee information:

1. The first and last name of the employee shoudl be capital case
2. The middle initial should exist and be a single uppercase letter 
3. The employee id should follow the format of 2 letters then 4 digits
4. The phone number should follow the format 3 digits, a dash, 3 digits, a dash, and then 4 digits (XXX-XXX-XXXX)

### Python Text Processing Strengths and Weakness 

The strengths and weaknesses of Python in terms of text processing generally align with the overall strengths and weaknesses of Python. The strengths, in my opinion would be the vast library support provided by the open source nature of python which make processing easier, along with the ease of readability simplifiying a lot of the complicated tasks that come with text proessing. The same follows for weaknesses, many of the weaknesses come from the way Python is built. It is not a particularly fast in terms of execution speed due to being dynamically typed, and not particularly memory efficient either. Both of these can make working with lots of data in text processing teedious but did not have an effect in this assignment since the data I worked with was so small. 

### What I Learned from this Assignment

I did not have much experience working in Python so much of what was done in this assignment was my first time doing it. It was an excellent step into development with pyhton and the common structures and functions we'll be using in the NLP course. To pinpoint one thing specifically I learned was how to use regular expression again, which was something I had not even thought about since high school.

## NLTK Exploration
This [notebook](NLTK-Exploration.pdf) is a brief exploration into some of the common methods and topics used in the nltk tool kit that we'll be using in this NLP course (CS 4395).