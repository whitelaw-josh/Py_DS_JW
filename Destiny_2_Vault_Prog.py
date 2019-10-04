'''
Welcome to The Vault
'''

print('Welcome to The Vault! Please follow the prompts as they appear and enter what is required.')
print('Enter "clear" to reset everything to round 1 \n')
#print('Enter "reset" to reset the round you are currently in')

empty_answers_dict = { 'STAIRS':'', 'ROCK':'', 'TREES':'' }
empty_loc_answers_list = ['STAIRS', 'ROCK', 'TREES']
loc_acceptable_answer_list = ['stairs', 's', 'rock', 'r', 'trees', 't']
loc_lr_acceptable_answer_list = ['left', 'l', 'right', 'r']

for i in range(1, 4) :
    round_answers_dict = empty_answers_dict.copy()
    locations_left_list = empty_loc_answers_list.copy()
    answer_count = 0

    def pen_ant(direction):
        if direction == 'left' or direction == 'l':
            return 'PEN'
        else:
            return 'ANT'

    print('\n******************************')
    print('ROUND ' + str(i) + ':')
    print('******************************\n')

    while answer_count != 3 :
        answer = str(input('Which plate are you recording? (Stairs = stairs, s | Rock = rock, r | Trees = trees, t): ')).lower()
        
        if answer == 'clear':
            round_answers_dict = empty_answers_dict.copy()
            locations_left_list = empty_loc_answers_list.copy()
            answer_count = 0
        elif answer in loc_acceptable_answer_list:
            loc_answer = str(input('Is it on the left or right? (Left = left, l | Right = right, r):')).lower()
            
            while not loc_answer in loc_lr_acceptable_answer_list:
                if loc_answer == 'clear':
                    round_answers_dict = empty_answers_dict.copy()
                    locations_left_list = empty_loc_answers_list.copy()
                    answer_count = -1
                else:
                    print('Please enter a correct response given in the prompt.')
                    loc_answer = str(input('Is it on the left or right? (Left = left, l | Right = right, r):')).lower()
            
            if answer_count != -1:
                print(pen_ant(loc_answer))
                if answer == 'stairs' or answer == 's':
                    round_answers_dict['STAIRS'] = pen_ant(loc_answer)
                elif answer == 'rock' or answer == 'r':
                    round_answers_dict['ROCK'] = pen_ant(loc_answer)
                else:
                    round_answers_dict['TREES'] = pen_ant(loc_answer)

            answer_count += 1
        else:
            print('Please enter a correct response given in the prompt.')

    print('\n******************************')
    print('ROUND ' + str(i) + ' RECORDINGS:')
    print('******************************\n')
    
    for key, value in round_answers_dict.items():
        print('{0:7} => {1:6}'.format(key, value))

    print('\n')

        


#Stairs answer
#Rock answer
#Trees answer

#Loop for user to decide on what is left

#-----Loop to beginning and start round over-----#