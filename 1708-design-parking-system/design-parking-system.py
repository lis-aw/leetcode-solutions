class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = {1: big, 2: medium, 3: small}

        #obj = ParkinSystem(1,1,0) <-one big, one medium, zero small
        #obj.add(1)
        

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] is not 0:
            self.slots[carType] -= 1
            return True
        else: return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)