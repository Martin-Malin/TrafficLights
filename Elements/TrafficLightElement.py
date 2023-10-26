from . import StringElement


class TrafficLightElement:
    __hasCar: bool = False
    __type: str
    RedLightValue = "R"
    OrangeLightValue = "O"
    GreenLightValue = "G"
    Timer: int

    def IsTrafficLight(self) -> bool:
        return True

    def IsGround(self) -> bool:
        return False

    def IsCar(self) -> bool:
        return self.__hasCar == True

    def SetIsCar(self, isCar: bool) -> None:
        self.__hasCar = isCar

    def IsGreenLight(self) -> bool:
        return self.__type == TrafficLightElement.GreenLightValue

    def __init__(self, __type: str) -> None:
        if __type not in [TrafficLightElement.RedLightValue, TrafficLightElement.OrangeLightValue, TrafficLightElement.GreenLightValue]:
            raise Exception(f"__type {__type} not allowed.")

        self.__type = __type
        self.initTimer()

    def Cycle(self) -> None:
        self.Timer -= 1
        
        if self.Timer == 0:
            self.setNext__type()
            self.initTimer()

    def initTimer(self) -> None:
        if self.__type in [TrafficLightElement.RedLightValue, TrafficLightElement.GreenLightValue]:
            self.Timer = 5
        else:
            self.Timer = 1

    def setNext__type(self) -> None:
        match self.__type:
            case self.GreenLightValue:
                self.__type = TrafficLightElement.OrangeLightValue
            case self.OrangeLightValue:
                self.__type = TrafficLightElement.RedLightValue
            case self.RedLightValue:
                self.__type = TrafficLightElement.GreenLightValue

    def GetValue(self) -> str:
        if self.__hasCar:
            return StringElement.StringElement.CarValue
        else:
            return self.__type
