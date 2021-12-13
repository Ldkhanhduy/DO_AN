from datalayer.person import Student, Professor
from datalayer.achivement import Achivement
import pickle

class Studentmanage:
    def inputinfo(self, name: str, phonenumber: str, studentID: int, dayofbirth: str, email: str):
        stu = Student(name, phonenumber, studentID, dayofbirth, email, Achivement)
        result = []
        result.append(vars(stu))
        file1 = open("D:/tep.txt", 'wb')
        pickle.dump(result, file1)
        file1.close()
        file1 = open("D:/tep.txt", "rb")
        studentlist = pickle.load(file1)
        for i in studentlist:
            print(i)
        

    def search(self, studentlist: list[Student], name: str) -> list[Student]:
        result = []
        for i in range(len(studentlist)):
            if studentlist[i].name == name:
                result.append(studentlist[i])
        return result

class Professormanage:
    def inputinfo(self, name: str, phonenumber: str, professorID: int, email: str):
        prof = Professor(name, phonenumber, professorID, email)
        return prof

    def search(self, proflist: list[Professor], name: str) -> list[Professor]:
        result = []
        for i in range(len(proflist)):
            if proflist[i] == name:
                result.append(proflist[i])
        return result