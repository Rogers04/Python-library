text =  'Python'


'''i = 0


size_string = len(text)


while i < size_string:
    print(text[i],i)


    i += 1
'''
text_new = ''


for letters in text:
    text_new += f'*{letters}'
    #print(letters)
print(text_new + '*')



