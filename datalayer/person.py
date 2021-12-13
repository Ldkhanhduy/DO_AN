from .achivement import Achivement

class Location:
    number: str
    street: str
    city: str

    def __init__(self, number, street, city) -> None:
        super().__init__()
        self.number = number
        self.street = street
        self.city = city

    def printinfo(self) -> str:
        result = f"Address: {self.number}, {self.street}, {self.city}"
        return result

class Person:
    name: str
    phonenumber: str

    def __init__(self, name, phonenumber) -> None:
        super().__init__()
        self.name = name
        self.phonenumber = phonenumber

    def printinfo(self) -> str:
        result = f"Name: {self.name}, Phone: {self.phonenumber}"
        return result

    def live(self, location: Location):
        result = "Address:" + location.printinfo()
        return result

class Student(Person):
    studentID: int
    dayofbirth: str
    email: str
    achivement: Achivement

    def __init__(self, name, phonenumber, studentID, dayofbirth, email, achivement) -> None:
        Person.__init__(self, name, phonenumber)
        self.studentID = studentID
        self.dayofbirth = dayofbirth
        self.email = email
        self.achivement = achivement

    def getachivement(self) -> Achivement:
        return self.achivement

'''    def printinfo(self) -> dict:
        result = f"Name: {self.name}, Phonenumber: {self.phonenumber}, StudentID: {self.studentID}, Dayofbirth: {self.dayofbirth}, Email: {self.email}"
        return result'''

class Professor(Person):
    professorID: int
    email: str

    def __init__(self, name, phonenumber, professorID, email) -> None:
        Person.__init__(self,name, phonenumber)
        self.professorID = professorID
        self.email = email

    def printinfo(self) -> str:
        result = f"ProfessorID: {self.professorID}, Email: {self.email}"
        return result

