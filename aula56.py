'''
split the join with list the str
split - split a string
join - unites one string
'''

phrase = 'Look at thatm interesting thing'
list_words_raw = phrase.split(' ')

list_words = []
for i, phrase in enumerate(list_words_raw):
    list_words.append(list_words_raw[i].strip(''))

'''print(list_words_raw)
print(list_words)
'''

phrase_united = '-'. join(list_words)
print(phrase_united)