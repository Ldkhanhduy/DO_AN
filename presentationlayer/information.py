from businesslayer.management import Studentmanage

class Viewer:
    def inputinfo(self):
        print("Student list: ")
        for i in range(1):
            print(i + 1)
            name = input("Name: ")
            phonenumber = input("Phonenumber: ")
            studentID = int(input("StudentID: "))
            birth = input("Day od birth: ")
            email = input("Email: ")
            result = Studentmanage.inputinfo(self, name, phonenumber, studentID, birth, email)
            mark = input("Mark: ")
            rank = input("Rank: ")
            scholarship = input("ScholarshiP: ")
            checkname = input("Name: ")
