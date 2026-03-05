class Automobile:
    pass

class Car(Automobile):

    __name = None

    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name
