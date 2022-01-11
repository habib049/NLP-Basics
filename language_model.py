from collections import defaultdict
from nltk.corpus import brown
from nltk import trigrams
import random

corpus_sents = [' '.join(sent) for sent in brown.sents()]

bi_gram_data = []
tokenized_text = []
language_model = defaultdict(lambda: defaultdict(lambda: 0))

for sentence in brown.sents():
    for word1, word2, word3 in trigrams(sentence):
        language_model[(word1, word2)][word3] += 1

for word1_word2 in language_model:
    total_count = float(sum(language_model[word1_word2].values()))
    for word3 in language_model[word1_word2]:
        language_model[word1_word2][word3] /= total_count

#
#
# predict the next word of I am
predicted_dict = dict(language_model['I', 'am'])
print("Next predicted work of I am is : ", max(predicted_dict, key=predicted_dict.get), "\n\n")

#
#
# generating sentences using ngram
max_sentence_length = 10
sentence_count = 10

first_word = 'I'
second_word = 'am'

print("Generated sentences\n")
for _ in range(sentence_count):
    sentence = first_word + ' ' + second_word + ' '
    for _ in range(max_sentence_length):
        predicted_dict = dict(language_model[first_word.strip(), second_word.strip()])
        if len(predicted_dict) > 0:
            random_word = random.randint(0, len(predicted_dict) - 1)
            predicted_dict_keys = list(predicted_dict)
            predicted_word = predicted_dict_keys[random_word] + " "
            sentence += predicted_word
            first_word = second_word
            second_word = predicted_word

    print(sentence)
    first_word = 'I'
    second_word = 'am'
