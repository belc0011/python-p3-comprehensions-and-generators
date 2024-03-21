#!/usr/bin/env python3

def return_evens(num_list):
    return_evens_list = [element for element in num_list if element%2 == 0]
    return return_evens_list

def make_exclamation(sentence_list):
    make_exclamation_list = [sentence_list + '!' for sentence_list in sentence_list]
    return make_exclamation_list