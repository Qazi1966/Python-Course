class SafetyDepositBox():
    def __init__(self):
        self.__code = ""
        self.__state = "Open-NoCode"

    def reset(self):
        self.__code = ""
        
    def SetState(self, NewState):
        self.__state = NewState
        print(self.__state)
        
    def SetNewCode(self, NewCode):
        self.__code = NewCode
        print("New Code Set Is: ", self.__code)
        
    def valid(self, s):
        Digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        Validity = False
        if len(s) == 4:
            if                          # if this condition is true then validity is true
            
            
                Validity = True
            
        return Validity