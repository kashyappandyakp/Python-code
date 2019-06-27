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
        
class C(B):
    def stud_dev(self):
        Devi = "B"
        print(Devi)
        
d = C()
e = d.stud_age()
e = d.stud_name()
e = d.stud_marks()
e = d.stud_dev()
print(e)
