# -*- coding: utf-8 -*-
import snowballstemmer
from nltk import word_tokenize
from nltk import FreqDist
from word import Word
import textcleaner
from mwe import MWE
import getdata


def create_objects(lemmas):
    lemma_objects = []
    for lemma in lemmas:
        received_data = getdata.get_data(lemma)
        if type(received_data) == list:
            lemma = Word(lemma)
            lemma_objects.append(lemma)
            data = received_data[0]
            setattr(lemma, "pos", getdata.get_pos(data))
            setattr(lemma, "feature", getdata.get_feature(data))
            setattr(lemma, "valency", getdata.get_valency(data))
            setattr(lemma, "lang", getdata.get_language(data))
            setattr(lemma, "senses", getdata.get_senses(data))
    return lemma_objects


def get_specifiedlist (lemma_objects, key, lemma_type):
    type_list = []
    for lemma in lemma_objects:
       if lemma_type == getattr(lemma, key):
           type_list.append(lemma.name)
    return textcleaner.get_vocab(type_list)
        
        
#raw_text = TextCleaner.read_file("sonkuslar.txt")
raw_text = "hızlı hızlı Kış, Ada’nın her ulvi tarafında yerleşebilmek fdshs için rüzgârlarını poyraz, Yıldız poyraz"
tokenized_text = word_tokenize(textcleaner.clean_text(raw_text))


mwes = MWE.find_mwes(tokenized_text)
print(MWE.get_mwesname_list(mwes))


stemmer = snowballstemmer.stemmer('turkish')
print(FreqDist(stemmer.stemWords(tokenized_text)).most_common(50))
print(FreqDist(stemmer.stemWords(tokenized_text))["ada"])
lemmas = textcleaner.get_vocab(stemmer.stemWords(tokenized_text))


lemma_objects = create_objects(lemmas)
lemmaname_list = []
for obj in lemma_objects:
    lemmaname_list.append(obj.name)
print(textcleaner.get_vocab(lemmaname_list))


print(get_specifiedlist(lemma_objects, "pos", "n"))
print(get_specifiedlist(lemma_objects, "lang", "ar"))
print(get_specifiedlist(lemma_objects, "feature", "old"))
print(get_specifiedlist(lemma_objects, "senses", "4"))
print(get_specifiedlist(lemma_objects, "valency", "dat."))


sense_numbers = {}
for lemma in lemma_objects:
    sense_numbers[lemma.name] = int(lemma.senses)
print(sorted(sense_numbers.items(), key=lambda x: x[1], reverse = True))

    