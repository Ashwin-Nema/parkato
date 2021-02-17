from car import Car
class ParkingLot:
    def __init__(self):
        self.slot_number = {}
        
        self.color_to_registration_number = {}

        self.color_to_slot_number = {}

        self.registration_number_to_slot_number = {}

        
    
    def add(self, slot, Vehicle):
        if Vehicle.color not in self.color_to_registration_number:
            
            self.slot_number[slot] = [Vehicle.registration_number, Vehicle.color ]
            
            self.color_to_registration_number[Vehicle.color] = [Vehicle.registration_number]
            
            self.color_to_slot_number[Vehicle.color] = [slot]

            self.registration_number_to_slot_number[Vehicle.registration_number] = slot

        else:
            self.slot_number[slot] = [Vehicle.registration_number, Vehicle.color ]
            
            self.color_to_registration_number[Vehicle.color].append(Vehicle.registration_number)
            
            self.color_to_slot_number[Vehicle.color].append(slot)

            self.registration_number_to_slot_number[Vehicle.registration_number] = slot
            
    
    def remove(self, slot):
        self.color_to_registration_number[ self.slot_number[slot][1]   ].remove( self.slot_number[slot][0]   )
        
        self.color_to_slot_number[ self.slot_number[slot][1] ].remove(slot)

        self.registration_number_to_slot_number.pop( self.slot_number[slot][0]  )

        self.slot_number.pop(slot)