class Subject:
    subjectName: str
    mark: float

    def __init__(self, subjectName, mark) -> None:
        super().__init__()
        self.subjectName = subjectName
        self.mark = mark

    def printinfo(self) -> str:
        result = f"SubjectName: {self.subjectName}, Mark: {self.mark}"
        return result
