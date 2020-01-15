from random import randint
"""
    Welcome! This a number guessing game where you will start with 3 lives in
    order to guess a number or numbers between 0-20.
    So you them smartly.Wait... it sounds boring.So, here's the twist.
    If you guessed the number correctly in first attempt, you'll get double
    of your remaining lives.If guessed correctly in second attempt, you'll 1.5
    times your remaining life rounded upto integer.
    Press q to quit.
"""

print(
    """
    Welcome! This a number guessing game where you will start with 6 lives in
    order to guess a number or numbers between 0-20.
    So use them smartly.
    Press q to quit.
    """
    )
k = input("Press any key to start  ").lower()
if k=='q':
    print("You opt to quit the game before starting it")
else:
    number = randint(0,10)
    score_list = []
    life = 6
    points = 0
    while 1:
        user_no = input('Your guess - ')
        if user_no =='q':
            print('Thank You for playing this game!')
            break
        if int(user_no) == number:
            points += 3
            life += 1
            print('Your Points = ' + str(points) ,'Lives left = ' + str(life),sep='\n')
            number = randint(0,10)
            
        else:
            #print(number)
            life -= 1
            print('Lives left = ' + str(life))
        if life == 0:
            break    
    print("Your Score = " + str(points))
#print('Highest Score = ' + str(max(score_list)))
        
        
    
    
    

