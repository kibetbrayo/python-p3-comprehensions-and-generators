#!/usr/bin/env python3

def return_evens(num_list):
    return[num for num in num_list if num % 2 == 0]

even_elements = return_evens([0, 1, 3, 5, 7, 8, 9])
print(even_elements)

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]

exclamated_sentence = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(exclamated_sentence)