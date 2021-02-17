from slots import Slots
from parking_lot import ParkingLot
from car import Car

class Execution:
    def __init__(self, capacity):
        self.spots = Slots(capacity)
        self.parking = ParkingLot()

    
    def execute(self, command):

        command = command.split() 
        assign = {"park" : self.park(command), "leave" : self.leave(command), "status" : self.status(command), "registration_numbers_for_cars_with_colour" : self.registration_numbers_for_cars_with_colour(command), "slot_numbers_for_cars_with_colour"  : self.slot_numbers_for_cars_with_colour(command), "slot_number_for_registration_number" : self.slot_number_for_registration_number(command)}

        if assign.get(command[0]) == None or assign.get(command[0]) == False:
            return "Invalid Input"
        
        return assign[command[0]]
    


    def park(self, command):
        if command[0] != "park" or len(command) != 3:
            return False

        if self.parking.registration_number_to_slot_number.get(command[1]) == None:
            check = self.spots.add()
            
            if check:
                Vehicle = Car(command[1], command[2])
                self.parking.add(check, Vehicle)
                return "Allocated slot number " + str(check)
            
            else:
                return "Sorry, parking lot is full"
        
        else:
            return "Sorry, car of this registration number is already parked"
    

    def leave(self, command):
        if command[0] != "leave" or len(command) != 2:
            return False
        
        for i in range(len(command[1])):
            if i == 0 and 49 <= ord(command[1][0]) <= 57:
                    continue

            elif 48 <= ord(command[1][i]) <= 57:
                continue

            else:
                return False

        slot = int(command[1])
        check = self.spots.remove(slot)

        if check > len(self.spots.register):
            return False

        if check:
            self.parking.remove(check)
            return "Slot Number " + str(check) + " is free"
        
        else:
            return "Slot Number " + str(check) + " was already free"
    

    def status(self, command):
        if command[0] != "status" or len(command) != 1:
            return False

        result = list()
        for key in self.parking.slot_number.keys():
            result.append([key, self.parking.slot_number[key][0], self.parking.slot_number[key][1]])
        
        if result:
            return result
        
        else:
            return "Parking lot is empty"
    

    def registration_numbers_for_cars_with_colour(self, command):
        if len(command) != 2 or command[0] != "registration_numbers_for_cars_with_colour":
            return False
        
        value = self.parking.color_to_registration_number.get(command[1])

        if value == None or value == []:
            return "Not found"
        
        return value
    

    def slot_numbers_for_cars_with_colour(self, command):
        if command[0] != "slot_numbers_for_cars_with_colour" or len(command) != 2:
            return False
        
        value = self.parking.color_to_slot_number.get(command[1])

        if value == None or value == []:
            return "Not found"
        
        return value
    
    def slot_number_for_registration_number(self, command):
        if len(command) != 2 and command[0] != "slot_number_for_registration_number":
            return False
        
        value = self.parking.registration_number_to_slot_number.get(command[1])

        if value == None  or value == []:
            return "Not found"
        
        return value