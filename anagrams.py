# Codewars Challenge: Write a function that will find all the anagrams of a word from a list. 
# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
# You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. Example:
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
def anagrams(word, words):
    x = []
    for i in words:
        if(sorted(i) == sorted(word)):
            x.append(i)
    return x
