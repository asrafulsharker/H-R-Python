command = ""
started = False
while command != "quit":
    command = input("Enter your command: ").lower()
    if command == "start":
        if started:
            print("Car Already Started")
        else:
            started = True
            print("Your car is ready to start! ")

    elif command == "stop":
        if not started:
            print("Your car already stopped!")
        else:
            started = False    
            print("Your Car is stopped")

    elif command == "say":
        break
    else:
        print("Your are type in wrong keyword !")        