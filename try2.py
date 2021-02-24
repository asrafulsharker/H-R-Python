start = 'start'
stop = 'stop'
quit = 'quit'

enter = str(input('Please Enter your command: '))


if(enter == start):
    print("Your car is ready to start!")

elif(enter == stop):
    print("Your Car is stopped!")

elif(enter == quit):
    print("Your Car is stopped!")
    break
else:
    print("I cant understand your command !")       