class Slots:
    def __init__(self, capacity):
        self.register = [False for i in range(capacity)]
        self.displace = []
        self.slot = 0

    def add(self):
        if all(self.register):
            return False
        
        if self.displace:
            position = self.displace.pop(0)
            self.register[position - 1 ] = True
            return position
        
        else:
            self.register[self.slot] = True
            self.slot += 1
            return self.slot

    
    def remove(self, position):
        if position > len(self.register):
            return position
        
        if self.register[position - 1] == True:
            self.register[position - 1] = False
            self.displace.append(position)
            
            return position

        else:
            return False