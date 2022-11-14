# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''
Function below takes two sentences and finds words that are in both

'''

def words_in_both(sentence1, sentence2):
    newsentence1=sentence1.lower()
    newsentence2=sentence2.lower()
    string_array1=newsentence1.split()
    string_array2=newsentence2.split()
    words=[]
    for i in range(0,len(string_array1)-1):
            if string_array1[i] in string_array2:
                words.append(string_array1[i])
    return words

print(words_in_both("hello my honey", "hello world"))




