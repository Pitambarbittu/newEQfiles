#Create class OOPS and implement all oops concept in that.

class Student:
    # static variable
    school = "clg"" ""="" ""ADAMAS"
    company = "company"" ""="" ""cloudEQ"

    def __init__(self,aa,bb,cc):
        self.aa = aa
        self.bb = bb
        self.cc = cc

    def avg(self):
        return (self.aa + self.bb + self.cc)/3



    @classmethod
    def info(cls):
        return cls.school
        
    @classmethod
    def info1(cls):
        return cls.company
    
    def info2():
        print("this is static method..")



b1 = Student(12,32,44)
b2 = Student(44,75,66)

print(b1.avg())
print(b2.avg())
print(Student.info())
print(Student.info1())
print(Student.info2())



