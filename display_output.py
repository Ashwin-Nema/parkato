class DisplayOutput:
    def check_mode(self, command):
        if command == "1" or command == "2":
            return True
        
        return False
    
    def check_start(self, start):
        start = start.split()
        if len(start) != 2 or start[0] != "create_parking_lot":
            return False
        
        for i in range(len(start[1])):
            if i == 0 and 49 <= ord(start[1][i]) <= 57:
                continue

            elif 48 <= ord(start[1][i]) <= 57:
                continue
            
            else:
                return False
        
        return int(start[1])