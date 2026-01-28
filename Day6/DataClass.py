from dataclasses import dataclass

# @dataclass
# class Person:
#     name:str
#     age:int
#     profession:str

# person1 = Person("krish",17,'SE')
# print(person1)

#-----------------------------------------------------------------

# @dataclass
# class Rectangle:
#     width: int
#     height: int
#     color:str= 'white'

# rectangle1 = Rectangle(12,13)
# rectangle2 = Rectangle(13,14,'red')

# print(rectangle1)
# print(rectangle2)

#----------------------------------------------------------

# @dataclass(frozen=True)
# class Point:
#     x:int
#     y:int
# point = Point(3,4)
# print("Point: ", (point.x), (point.y))

#--------------------------------------------------

# @dataclass
# class Person:
#     name:str
#     age:int

# @dataclass
# class Employee(Person):
#     Employee_id:str
#     depertment:str

# person = Person('krish',31)
# employee = Employee("krish",25,"123","AI")
# print(employee.name)

#-----------------------------------------------------------\

# @dataclass
# class Address:
#     name:str
#     city: int
#     zip:str

# @dataclass
# class Person:
#     name:str
#     age:int
#     address: Address

# address = Address('123Mainstreet',"banglore","12345")
# person = Person("krish",31,address)

# print(person.address.city)

#-----------------------------------------------------------

# @dataclass
# class StudentInfo:
#     name: str
#     roll: int
#     enrollment: str

# @dataclass
# class Marks:
#     mid: int
#     end: int
#     start: int

# @dataclass
# class Interview:
#     communication: str
#     resume: str
#     technical: str

# m = Interview(
#     name="Mannat",
#     roll=101,
#     enrollment="ENR01",
#     mid=25,
#     end=70,
#     internal=15,
#     communication=80,
#     resume="Good",
#     technical="Python"
# )
# def average_score(self):
#     return (self.communication + self.end) / 2

# print(m)
# print("Average (Interview + End Term):", m.average_score())


#----------------------------------------------------------------

