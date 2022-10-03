import nltk
from nltk import word_tokenize
from nltk import ngrams
import pickle

def calc_prob(text, unigram_dict, bigram_dict, V):
    test_unigram = word_tokenize(text)
    test_bigram = list(ngrams(test_unigram, 2))

    p_laplace = 1

    for bigram in test_bigram:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        p_laplace = p_laplace * ((n + 1) / (d + V))
    
    return p_laplace


#read in pickle files
eng_bigram = pickle.load(open('eb.p', 'rb'))
eng_unigram = pickle.load(open('eu.p', 'rb'))
frn_bigram = pickle.load(open('fb,p', 'rb'))
frn_unigram = pickle.load(open('fu.p', 'rb'))
itl_bigram = pickle.load(open('ib.p', 'rb'))
itl_unigram = pickle.load(open('iu,p', 'rb'))

#calculate probabilities for each line in file
testfile = "ngram_files/LangId.test"

vocab_size = len(eng_unigram) + len(frn_unigram) + len(itl_unigram)

results = []

with open(testfile , 'r', encoding="utf-8-sig") as f:
    lineno = 1
    for line in f:
        text = line.strip()
        eng_prob = calc_prob(text, eng_unigram, eng_bigram, vocab_size)
        frn_prob = calc_prob(text, frn_unigram, frn_bigram, vocab_size)
        itl_prob = calc_prob(text, itl_unigram, itl_bigram, vocab_size)

        probs = (eng_prob, frn_prob, itl_prob)
        highest_prob = max(probs)
        index = probs.index(highest_prob)
        language = 'italian'

        if index == 0:
            language = 'english'
        elif index == 1:
            language = 'french'

        #print(lineno, language)
        result = str(lineno) + ' ' + language

        results.append(result)

        lineno += 1

f.close()

#write results to a file 
with open('test-result.txt', 'w') as f:
    f.write(results[0])
    for result in results[1:]:
        f.write('\n'+result)

f.close()

#compare solution results to test results 
correct_class = []

with open('ngram_files/LangId.sol' , 'r', encoding="utf-8-sig") as f:
    for line in f:
        line = line.strip()
        correct_class.append(line.lower())

f.close()

lineno = 0;
correct_count = 0;
incorr_linenos = []
for result in results:
    if result != correct_class[lineno]:
        incorr_linenos.append(lineno + 1)
    else:
        correct_count += 1
    lineno += 1

#print accuracy and incorrect lines
print('accuracy:', correct_count / len(correct_class))
print('list of incorrectly classified lines:', incorr_linenos)