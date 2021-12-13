from person import Professor
from field import Field
from person import Student

class Classroom:
    classroomID: int
    professorID: Professor
    fieldID: Field
    studentquantity: int

    def __init__(self, classroomID, professorID, fieldID, studentquantity) -> None:
        super().__init__()
        self.classroomID = classroomID
        self.professorID = professorID
        self.fieldID = fieldID
        self.studentquantity = []

    def getstudentquantity(self, num: Student):
        return self.studentquantity.append(num)

    def gerstudentquantity(self) -> len(list[Student]):
        return self.studentquantity

    def getprofessorID(self) -> Professor:
        return self.professorID

    def getfieldID(self) -> Field:
        return self.fieldID

    def printinfo(self) -> str:
        result = f"ClassroomID: {self.classroomID}, ProfessorID: {self.professorID}, fieldID: {self.fieldID}, Student: {self.studentquantity}"
