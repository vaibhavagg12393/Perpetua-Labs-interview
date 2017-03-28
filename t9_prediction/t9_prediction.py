from itertools import product
from Bio import trie

t=trie.trie()
dictionary = [word.strip() for word in open("dictionary.txt","rb")]

for word in dictionary:
    t[word]=len(word)

t9Map = {1:[""],
       2:["a","b","c"],
       3:["d","e","f"],
       4:["g","h","i"],
       5:["j","k","l"],
       6:["m","n","o"],
       7:["p","q","r","s"],
       8:["t","u","v"],
       9:["w","x","y","z"]}

print "Enter a number:"
input = input()
strings=[]

for char in str(input):
    strings.append(t9Map[int(char)])

result = []
for all in product(*(x for x in strings)): #makes all possible combinations of words from given alphabets
    possible = ''.join(all) #joins alphabets to form a word
    if possible in t: #looks for that word in trie
        result.append(possible)

print result