# -*- coding: utf-8 -*-
import nltk
import getdata
import re


class MWE: 
    def __init__(self, name):
        self.name = name
        self.reduplication = bool
        
        
    def get_bigrams(tokenized_text):
        bigram_list = list(nltk.bigrams(tokenized_text))
        for bigram in bigram_list:
            if re.match("[^\w\s]", bigram[0]) or re.match("[^\w\s]", bigram[1]):
                bigram_list.remove(bigram)
        return bigram_list


    def find_mwes(tokenized_text):
        mwes = []
        bigram_list = MWE.get_bigrams(tokenized_text)
        for bigram in bigram_list:           
            if bigram[0] == bigram[1]:
                bigram = MWE(" ".join(bigram))
                bigram.reduplication = True
                mwes.append(bigram)
            else:
                bigram = " ".join(bigram)
                data = getdata.get_data(bigram)
                if type(data) == list:
                    bigram = MWE(bigram)
                    mwes.append(bigram)
        return mwes
    
    
    def get_mwesname_list(mwes):
        mwesname_list =  []
        for mwe in mwes:
            mwesname_list.append(mwe.name)
        return set(mwesname_list)
            
    
    
    
    

