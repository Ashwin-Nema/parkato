from car import Car
from parking_lot import ParkingLot
from execution import Execution
from slots import Slots
from display_output import DisplayOutput

screen = DisplayOutput()

print("Do you want to earn money through your your parking lot?")
print()
print("If yes, then type YES")
print()
print("If not, then type NO")
print()
money = input()
print()

if screen.check_money(money):
    if money == "YES":
        print("Enter amount you want to charge each customer:", end = " ")
        amount = input()
        check_amount = screen.check_amount(amount)
        if check_amount:
            amount = int(amount)
            print()

        else:
            print("Invalid Input")
            print()


else:
    print("Invalid Input")
    print()

print("Do you want to know how many cars were parked in your parking lot?")
print()
print("If yes, then type YES")
print()
print("If not, then type NO")
print()
count = input()
print()

if not(screen.check_count(count)):
    print("Invalid Input")
    print()

print("Please select the mode of input") 

print()

print("Press 1 for providing input through command prompt based shell where commands can be typed in ")

print("Press 2 to accept a filename as a parameter at the command prompt and read the commands from that file")

print()

mode = input()


print()



if not(screen.check_mode(mode)):
    print("Invalid Input")


if mode == "1":
    command = input()

    start = screen.check_start(command)

    if not(start):
        print("Invalid Input")
    
    else:
        print(f"Created a parking lot with {start} slots")
        print()

        if money == "YES" and check_amount:
            user = Execution(start, amount)
        
        else:
            user = Execution(start)


        while command != "exit":
            command = input().strip()

            if command != "exit":
                enter = user.execute(command)
                
                if type(enter) == str or type(enter) == int:
                    print(enter)
                
                elif command == "status":
                    print("Slot No. Registration No Colour")
                    
                    for i in enter:
                        print(*i)
                
                else:
                    print(*enter, sep = ", ")

                print()
            
        print()
        if money == "YES" and check_amount:
            print("Total income = ", end="")
            print(user.spots.income)
            print()
        
        if count == "YES":
            print("Total number of vehicles that were parked in the parking lot = ", end="")
            print(user.spots.count)
        

elif mode == "2":
    print("Please enter the source of file:", end=" ")
    source = input()

    print()

    file = open(f"./{source}")
    output = 1

    for content in file:
        if output == 1:
            start = screen.check_start(content)

            if not(start):
                print("Invalid Input") 
            
            else:
                print(f"Created a parking lot with {start} slots")


                if money == "YES" and check_amount:
                    user = Execution(start, amount)
                
                else:
                    user = Execution(start)

            output += 1
        
        elif start:
            content = content.strip()
            enter = user.execute(content)

            if type(enter) == str or type(enter) == int:
                print(enter)
            
            elif content == "status":
                print("Slot No. Registration No Colour")
                
                for i in enter:
                    print(*i)
            
            else:
                print(*enter, sep = ", ")

    file.close()
    print()
    if money == "YES" and check_amount:
        print("Total income = ", end="")
        print(user.spots.income)
        print()
    
    if count == "YES":
        print("Total number of vehicles that were parked in the parking lot = ", end="")
        print(user.spots.count)