from classroom import Classroom

class Field:
    fieldID: int
    fieldName: str
    classquantity: list[Classroom]

    def __init__(self, fieldID, fieldName) -> None:
        super().__init__()
        self.fieldID = fieldID
        self.fieldName = fieldName
        self.classquantity = []

    def getquantity(self, num: Classroom):
        return self.classquantity.append(num)

    def getquantity(self) -> list[Classroom]:
        return self.classquantity
