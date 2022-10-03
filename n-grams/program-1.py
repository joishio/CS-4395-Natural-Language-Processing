import nltk
from nltk import word_tokenize
from nltk import ngrams
import pickle

def processing(filename):
    if str(filename):
        #open file and remove newlines
        with open(filename , 'r', encoding="utf-8-sig") as f:
            raw_text  = f.read().strip()

        #tokenize text
        tokens = word_tokenize(raw_text)

        #create bigrams list
        bigrams = list(ngrams(tokens, 2))

        #create unigrams list
        unigrams = tokens

        #create bigram dictionary
        bigram_dict = {t : bigrams.count(t) for t in set(bigrams)}

        #create unigram dictionary 
        unigram_dict = {t :unigrams.count(t) for t in set(unigrams)}

        return bigram_dict, unigram_dict
    else:
        print("invalid file name")

#get unigram and bigram dictionaries
eng_bigram, eng_unigram = processing("ngram_files/LangId.train.English")
frn_bigram, frn_unigram = processing("ngram_files/LangId.train.French")
itl_bigram, itl_unigram = processing("ngram_files/LangId.train.Italian")

#pickle dictionaries to save time in program-2
pickle.dump(eng_bigram, open('eb.p', 'wb'))
pickle.dump(eng_unigram, open('eu.p', 'wb'))
pickle.dump(frn_bigram, open('fb,p', 'wb'))
pickle.dump(frn_unigram, open('fu.p', 'wb'))
pickle.dump(itl_bigram, open('ib.p', 'wb'))
pickle.dump(itl_unigram, open('iu.p', 'wb'))

