# -*- coding: utf-8 -*-
import re


tr_alphabet = ["a", "â", "b", "c", "ç", "d", "e", "ê", "f", "g", "ğ", "h", "ı", "i", "î", "j", "k", "l", "m", "n", "o", "ö", "ô" , "p", "r", "s", "ş", "t", "u", "ü", "û", "v", "y", "z"]


def read_file(directory):
    file = open(directory, encoding='utf-8-sig') 
    raw_text = file.read()
    return raw_text


def clean_text(raw_text):
    raw_text = raw_text.lower()
    for ch in raw_text:
        if re.match("[^\w\s]", ch):
            raw_text = raw_text.replace(ch, " ")
    return raw_text

     
def alphabetical_order(word): 
    order = []
    for ch in word:
        if re.match("[^$]", ch):
            order.append(tr_alphabet.index(ch))
    return order
            
                    
def get_vocab(tokens):     
    return sorted(set(tokens), key = alphabetical_order)