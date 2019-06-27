class A:
    def stud_name(self):
        Name = 'Kashyap'
        print(Name)
    def stud_age(self):
        Age = 29
        print(Age)
class B(A):
    def stud_enrolment(self):
        Enrolment = 115400693107
        print(Enrolment)
    
    def stud_marks(self):
        Marks = 50
        print(Marks)
        
#print(issubclass(A,B))

a1 = B()

C = a1.stud_age()
C = a1.stud_name()
C = a1.stud_marks()
print(C)