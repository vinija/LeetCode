class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigSpot = big
        self.mediumSpot = medium
        self.smallSpot = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.bigSpot>0:
            self.bigSpot -=1
            return True
        elif carType == 2 and self.mediumSpot>0:
            self.mediumSpot -=1
            return True
        elif carType == 3 and self.smallSpot>0:
            self.smallSpot -=1
            return True
        
        return False
            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)