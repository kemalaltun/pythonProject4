class Student:
    name = "Kemal"

print(Student.name)

s1 = Student()
s2 = Student()
s2.name = "Mustafa"
print(s1.name,"Ve",s2.name)

class Personel:
    def __init__(self,name,job,age):
        self.name=name
        self.job=job
        self.age=age
p1 = Personel("Kemal","QA Tester",23)
print(p1.name,p1.job,p1.age)

class Library:
    def __init__(self,name,author,field):
        self.name = name
        self.author = author
        self.field = field

    def __str__(self):
        return f"Kitap adı :{self.name}\nYazar :{self.author}\nAlan :{self.field}"

lib1 = Library("Test Yöntemleri","Mustafa Kemal ALTUN","Tarih")
print(lib1)