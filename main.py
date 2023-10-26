from Elements import StringElement
from Elements import TrafficLightElement


class Road:
    __currentState:list = []

    def __init__(self):
        pass

    def __init__(self, initialState:str) -> None:
        for actor in initialState:
            if actor in [StringElement.StringElement.GroundValue, StringElement.StringElement.CarValue]:
                self.__currentState.append(StringElement.StringElement(actor))
            else:
                self.__currentState.append(TrafficLightElement.TrafficLightElement(actor))


    def ComputeNextCycle(self) -> None:
        for i in reversed(range(0, len(self.__currentState))):
            if self.__currentState[i].IsCar and i == len(self.__currentState)-1:
                self.__currentState[i-1].SetIsCar(False)

            if self.__currentState[i].IsGround():
                self.handleElementIsGround(i)

            if self.__currentState[i].IsTrafficLight():

                self.__currentState[i].Cycle()

                if self.__currentState[i].IsGreenLight():
                    if self.__currentState[i-1].IsCar() and self.__currentState[i+1].IsCar() == False:
                        self.__currentState[i].SetIsCar(True)
                        self.__currentState[i-1].SetIsCar(False)


    def handleElementIsGround(self, i):
        if i == 0:
            return
        
        if (self.__currentState[i-1].IsCar()):
            self.__currentState[i].SetIsCar(True)
            self.__currentState[i-1].SetIsCar(False)
                

    def __str__(self) -> str:
        value:str = ""
        for i in range(len(self.__currentState)-1):
            value += self.__currentState[i].GetValue()

        return value
        


def multipleCars(initialState:str, nbIterations:int):
    print(initialState)
    road = Road(initialState)
    for _ in range(nbIterations):
        road.ComputeNextCycle()
        print(road)


multipleCars("GC0.G...R.C.O....G.", 16)