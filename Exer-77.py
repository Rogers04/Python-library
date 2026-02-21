# Exercise - question and answer system


quest = [

    {
        'Questions': 'What is 2+2?',
        'Options':['1','3','4','5'],
        'Response': '4',
    },
    {
        'Questions': 'What is 5x5?',
        'Options':['25','30','55','51'],
        'Response':'25',
    },
    {
        'Questions': 'What is 10/2?',
        'Options':['1','3','4','5'],
        'Response':'5',
    },

]

hits = 0

for question in quest:
    print('Questions:', question['Questions'])
    print()

    opt = question['Options']
    for i, option in enumerate(opt):
        print(f'{i})', option)


    choice = input('Choose an option: ')

    right = False
    choice_int = None
    amout_options = len(opt)
    
    if choice.isdigit():
         choice_int = int(choice)

    if choice_int is not None:
        if choice_int >= 0 and choice_int < amout_options:
             if opt[choice_int] == question['Response']:
                 right = True

    if right:
        hits += 1
        print('Correct')
        
    else:
        print('Wrong')

    print()

t = 'Congratulations you got it right:',hits, 'questions'
    
print(*t)    