# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''
Function below takes two sentences and finds words that are in both

'''

def words_in_both(sentence1, sentence2):
    newsentence1=sentence1.lower()
    newsentence2=sentence2.lower()
    string_array1=newsentence1.split(" ")
    string_array2=newsentence2.split(" ")
    par_list=[]
    par_list.append(sentence1)
    for i in range(0,len(string_array1)-1):
            if string_array1[i] not in string_array2:
                del string_array1[i]
    if len(string_array1) < len(sentence1.split(" ")):
       return string_array1
    elif len(string_array1) == 1 and string_array1[0] in string_array2:
        return string_array1
    else:
        print("no words in common")
print(words_in_both("in", "from if to in"))





