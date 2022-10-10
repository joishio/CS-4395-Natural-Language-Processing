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

## Lemmatized Noun Guessing Game
Using some [raw text](Guessing-Game/anat19.txt) a word guessing game akin to hangman or jeopardy was created. The raw text was converted to tokens, lemmatized, and had a part of speech (POS) tagger applied to it in order to classify the 50 most common nouns in the body of text. Which is then used in the [guessing game](Guessing-Game/Guessing_Game.py) as the list of possible words. 

### Pre-processing Steps:

1. tokenize the lower-case raw text, reduce the tokens to only those that are alpha, not in
the NLTK stopword list, and have length > 5
2. lemmatize the tokens and use set() to make a list of unique lemmas
3. do pos tagging on the unique lemmas and print the first 20 tagged items 
4. create a list of only those lemmas that are nouns
5. print the number of tokens (from step 1) and the number of nouns (step 4) 
6. return tokens (not unique tokens) from step a, and nouns from the function

### Game Functions:
1. give the user 5 points to start with; the game ends when their total score is negative, orthey guess ‘!’ as a letter
2.  randomly choose one of the 50 words in the top 50 list (See the random numbers notebook in the Xtras folder of the GitHub)
3. output to console an “underscore space” for each letter in the word d. ask the user for a letter
4. ask the user for a letter
5. if the letter is in the word, print ‘Right!’, fill in all matching letter _ with the letter and add 1 point to their score
6. if the letter is not in the word, subtract 1 from their score, print ‘Sorry, guess again’
7. guessing for a word ends if the user guesses the word or has a negative score
8. keep a cumulative total score and end the game if it is negative (or the user entered ‘!’) for a guess
9. right or wrong, give user feedback on their score for this word after each guess

## WordNet Overview
This [document](WordNet-Overview.pdf) provides a rundown on the organizational hierarchy WordNet and its implementation through nltk with various examples and explanations on the functions and algorithms related to WordNet.

## N-grams Language Modeling
N-grams are an interesting part of NLP that allows for the creation of a language model by taking the probabilities of words appearing in sequence and comparing those n length sequences to a body of text. Read more about n-grams [here](n-grams/N-grams.pdf) in an short overview of their uses and definition. 

Working with n-grams to build a language model can be a very time consuming operation so for this language modeling project it was split into two parts: [part one](n-grams/program-1.py) which sets up our test data and creates the dictionaries of unigrams and bigrams to their count in the text and then pickles them, and [part two](n-grams/program-2.py) which does the language model calculations and compares the results to the correct solution. When looking at part two the use of Laplace smoothing was implemented but still led to some zeroing out due to too small of values, so the final results reflect that in its bias towards 'english' as the selected language when ties occur (such as a tie for zero between the three languages).

## Web Crawler
This [project](Web-Crawler/webcrawler.py) is a web crawler that uses the key term 'Pie' in a google search to grab 15 relevant urls and then scrape the text from those pages. The text was cleaned and used to build a knowledge base built on terms ordered by their frequencies and relevancy that is composed of a few context sentences for each word as described [here](Web Crawler/Web_Crawler_Report.pdf). 

The document above goes in detail about how the words were selected and how the knowledge base is defined, as well as some sample dialog for a chatbot built upon the knowledge base. 

### Insructions to Run Code

The [file](Web-Crawler/webcrawler.py) needs to be nested in a folder called 'Web-Crawler' which has two folders, 'htmldata' and 'sentdata' (used for storing file data) nested in it as well. 'Web Crawler' is the main folder with the two data folders and 'webcrawler.py' at the same level.