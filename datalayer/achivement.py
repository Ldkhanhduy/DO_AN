from .subject import Subject

class Achivement:
    avMark: list[Subject]
    rank: str
    scholarship: str

    def __init__(self, rank, scholarship) -> None:
        super().__init__()
        self.avMark = []
        self.rank = rank
        self.scholarship = scholarship

    def getavMark(self, mark: Subject):
        self.avMark.append(mark)

    def getavmark(self) -> list[Subject]:
        return self.avMark

    def printinfo(self) -> str:
        result = f"Avmark: {self.avMark}, Rank: {self.rank}, Scholarship: {self.scholarship}"
        return result

