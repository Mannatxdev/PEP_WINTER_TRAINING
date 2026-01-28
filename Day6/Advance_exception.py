from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_no: str
    enrollment: str


@dataclass
class Interview(Student):
    resume: int
    technical: int
    gd: int

    def average_score(self):
        return (self.resume + self.technical + self.gd) / 3


@dataclass
class Marks(Interview):
    start: int
    mid: int
    end: float = 0.0

    def __post_init__(self):
        self.end = self.average_score()

    def result(self):
        try:
            if self.end == 0:
                raise ValueError("Absent")
            elif self.end > 70:
                return "Passed"
            else:
                return "Failed"
        except ValueError as e:
            return str(e)

students = [
    Marks("Sunny", "101", "ENR1", 85, 80, 75, 60, 70),
    Marks("Amit", "102", "ENR2", 60, 55, 65, 50, 55),
    Marks("Ravi", "103", "ENR3", 0, 0, 0, 0, 0)
]
for s in students:
    print(f"{s.name} ({s.roll_no}) → {s.result()} | End Marks: {s.end}")