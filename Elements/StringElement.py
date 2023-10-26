class StringElement:
    __element:str = ""
    CarValue:str = "C"
    GroundValue:str = "."
    
    def IsTrafficLight(self) -> bool:
        return False
    
    def IsGround(self) -> bool:
        return self.__element == self.GroundValue

    def IsCar(self) -> bool:
        return self.__element == self.CarValue
    def SetIsCar(self, isCar:bool) -> None:
        if isCar:
            self.__element = self.CarValue
        else:
            self.__element = self.GroundValue

    def __init__(self, __element:str) -> None:
        self.__element = __element

    def GetValue(self) -> str:
        return self.__element