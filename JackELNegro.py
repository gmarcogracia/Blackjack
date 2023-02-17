


def countUQLetters(palabra):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    counter=0
    listaLetrasYaAparecidas=[]
    for char in palabra:
        if char in letters and char not in listaLetrasYaAparecidas :
            counter+=1 
            listaLetrasYaAparecidas.append(char)
            
    return counter

def count_char_x(word,charX):
    counter=0
    for char in word:
        if charX==char:
            counter+=1
            
    return counter

def count_multi_char_x(word, x) :
    numb= word.split(x)
    return len(numb)(-1)
    for char in word:
    
        if x in word:
            counter+=1
    return counter
pepe="epep"

def substring_between_letters(word,charInicio,charFinal):
    indiceInicio=word.find(charInicio)
    endex=word.find(charFinal)
    
    if indiceInicio !=-1 and endex!=-1:
        return word.split(indiceInicio,endex)
        
    return word

def x_length_words(sentence,length):
    separate=sentence.split(" ")
    for word in separate:
        if len(word)< length:
            return False
    return True  

def check_name(sentence,name):
    
    splitses=sentence.upper().split()
    for word in splitses:
     if name.upper == word:
         return True
    
    return False

def every_other_letter(word):
    other=""
    i=0
    for char in word:
        i+=1        
        if i%2!=0:
         other+=char 
    return other

def reverse (stringa):
    reverse=""

    for char in range(len(stringa)-1):
        reverse+=char
        
    return reverse

def make_spoonerism(word1,word2):
    tempCHar1=word1[0]
    
    word1.replace(word1[0],word2[0])
    word2.replace(word2[0],tempCHar1)
    return 

def add_exclamation(string):
    string2=""
    while(len(string)-1<=20):
        string2+="!"
    
    return string2

def sum_values(my_dictionary):
    counter=0
    for value in my_dictionary.values():
        counter+=value
        
    return counter

def sum_even_keys(my_dictionary):
    counter=0
    i=0
    for key in my_dictionary.keys():
        if i%2==0:
            counter+=key
        
    return key

class Node:
    def __init__(self,value,link=None):
        self.value=value
        self.link=link
        return self
    
    
