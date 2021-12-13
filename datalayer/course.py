from classroom import Classroom

class Course:
    courseID: int
    courseName: str
    coursequantity: int

    def __init__(self, courseID, courseName) -> None:
        self.courseID = courseID
        self.courseName = courseName
        self.coursequantity = []

    def getcoursequantity(self, num: Classroom):
        return self.coursequantity.append(num)

    def getcoursequantity(self) -> len(list[Classroom]):
        return self.coursequantity