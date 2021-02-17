from car import Car
from parking_lot import ParkingLot
from execution import Execution
from slots import Slots
from display_output import DisplayOutput


print("Please select the mode of input") 

print()

print("Press 1 for providing input through command prompt based shell where commands can be typed in ")

print("Press 2 to accept a filename as a parameter at the command prompt and read the commands from that file")

print()

mode = input()


print()

screen = DisplayOutput()

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