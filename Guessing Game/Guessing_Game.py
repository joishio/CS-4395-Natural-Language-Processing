import sys
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from random import seed
from random import randint

def preprocess(raw_text):
    '''Preprocessing function
    =============================================================================================
    Does the required preprocessing:
    a.tokenize the lower-case raw text, reduce the tokens to only those that are alpha, not in
    the NLTK stopword list, and have length > 5
    b. lemmatize the tokens and use set() to make a list of unique lemmas

    Does the required part-of-speech tagging:
    c. do pos tagging on the unique lemmas and print the first 20 tagged items

    Sets up and returns lemmatized nouns list and tokens:
    d. create a list of only those lemmas that are nouns
    e. print the number of tokens (from step a) and the number of nouns (step d) 
    f. return tokens (not unique tokens) from step a, and nouns from the function
    ================================================================================================
    parameters: str (raw_text)
    returns: list[str], list (fin_tokens, lem_nouns)
    '''
    if str(raw_text):
        tokens = word_tokenize(raw_text)

        #lowercase text
        lower = [t.lower() for t in tokens]

        #alpha and non-stop word
        in_alpha = [t for t in lower if t.isalpha() and
                    t not in stopwords.words('english')]
        
        #len > 5 
        fin_tokens = [t for t in in_alpha if len(t) > 5]

        #lemmatize
        wnl = WordNetLemmatizer()
        lemmas = [wnl.lemmatize(t) for t in fin_tokens]

        #make unqiue 
        uni_lemmas = list(set(lemmas))

        #pos tagging
        tags  = nltk.pos_tag(uni_lemmas)
        print(tags[:20])

        #noun lemmas
        lem_nouns = []
        for lem, tag in tags:
            if tag[0] == 'N':
                lem_nouns.append(lem)

        print("number of tokens:", len(fin_tokens), "\nnumber of nouns:", len(lem_nouns))

        return fin_tokens, lem_nouns
    else:
        print('not valid input text')


def guess_game(words):
    '''Guessing Game Function
    ===========================================================================================
    a. give the user 5 points to start with; the game ends when their total score is negative, orthey guess ‘!’ as a letter
    b. randomly choose one of the 50 words in the top 50 list (See the random numbers notebook in the Xtras folder of the GitHub)
    c. output to console an “underscore space” for each letter in the word d. ask the user for a letter
    d. ask the user for a letter
    e. if the letter is in the word, print ‘Right!’, fill in all matching letter _ with the letter and add 1 point to their score
    f. if the letter is not in the word, subtract 1 from their score, print ‘Sorry, guess again’
    g. guessing for a word ends if the user guesses the word or has a negative score
    h. keep a cumulative total score and end the game if it is negative (or the user entered ‘!’)
    for a guess
    i. right or wrong, give user feedback on their score for this word after each guess
    =============================================================================================
    parameters: list (words - list of words for guessing game)
    return: N/A
    '''
    if(list(words)):
        score = 5
        guess = ''
        seed(1014)
        print("W E L C O M E  T O  W O R D  G U E S S")
        while score >= 0 and guess != '!':
            word_num = randint(1,50)
            word = words[word_num]

            word_len = len(word)
            word_dict = {}
            current = ''
            for i in range(word_len):
                current += '_ '
            print(current, "| score:", score)

            pos = 0
            for l in word:
                if l not in word_dict:
                    word_dict[l] = [pos]
                else:  
                    word_dict[l].append(pos)
                pos += 1

            guessed = set([])

            #main loop
            while "_" in current and score > -1 and guess != "!":
                print("letters guessed: ", guessed)
                guess = input("guess a letter: ")
                if(guess == '!'):
                    print("G A M E  O V E R")
                    break
                
                if guess in word_dict and guess not in guessed:
                    print("R I G H T!")
                    for p in word_dict[guess]:
                        temp = list(current)
                        temp[p*2] = guess
                        current = "".join(temp)
                    score += 1
                    print(current, "| score:", score)
                    if "_" not in current: 
                        print("C O R R E C T")
                        print("========================================")
                        print("G U E S S  A  N E W  W O R D")
                    guessed.add(guess)
                elif not guess.isalpha():
                    print(guess, "is not a letter, guess again")
                    print(current, "| score:", score)
                elif guess in guessed:
                    print("alredy guessed: ", guess, "guess again")
                    score -= 1
                    print(current, "| score:", score)
                else:
                    score -= 1
                    if(score < 0):
                        print("sorry, score too low to continue")
                        print("G A M E  O V E R")
                        break
                    print("sorry, guess again")
                    print(current, "| score:", score)
                    guessed.add(guess)

    else:
        print("not a valid word list")


if(len(sys.argv) > 1): #check system arguments
    datafile = sys.argv[1]
    #print(datafile)

    with open(datafile , 'r', encoding="utf-8-sig") as f:
        raw_text  = f.read().strip()
    #print(raw_text)

    tokens = word_tokenize(raw_text)
    #print(tokens[:10])

    #lexical diversity 
    uni_tokens = list(set(tokens))
    lex_div = len(uni_tokens) / len(tokens)
    lex_div = "{:.2F}".format(lex_div)
    print(datafile, "has a lexical diversity of", lex_div)

    #pre-processed tokens and list of nouns
    pro_tokens, nouns = preprocess(raw_text)

    #make dictionary of nouns and their counts
    noun_count = {}
    for n in nouns:
        noun_count[n] = pro_tokens.count(n)
    print(len(noun_count))

    #sort the dictionary by word count
    sorted = sorted(noun_count, key=lambda k: (noun_count[k]), reverse=True)

    #print top 50 most common words
    iter = 1;
    common_words = []
    for n in sorted:
        print(iter, "-", n, "with count of", noun_count[n])
        common_words.append(n)
        iter += 1
        if iter > 50:
            break
    
    #start guessing game
    guess_game(common_words)
    
else:
    print("error: not enough args")
