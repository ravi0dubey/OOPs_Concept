class student:
    def __init__(self, name, year_of_birth, sex, place, *courses):
        self.course_list = []
        self.name = name
        try:
            self.year_of_birth = year_of_birth
        except Exception as e:
            print("Incorrect year of Birth", e)
        self.sex = sex
        self.place = place
        for i in courses:
            self.course_list.append(i)

    def __str__(self):
        return "This class is used to define student class"

    def age(self, current_year):
        try:
            return current_year - self.year_of_birth
        except Exception as e:
            print("Entered year of Birth is not numeric", e)

    def print_name(self):
        if type(self.name) == list:
            for i in range(len(self.name)):
                print(self.name[i])
        else:
            return self.name

    def course_print(self):
        print(self.course_list)


stud1=student("Ravi",1983,"Male","Noida",["Data Science","Data Analytics","Java"])
stud2=student("Astha",1986,"Female","Bengaluru",["Statitics","NLP","Computer Vision"])
print(stud2.name)
print(stud2.course_list)
stud2.course_print()
stud3=student("Illisha",2015,"Female","Pune",)
print(stud3.name)
print(stud3.course_list)
stud3.course_print()
stud4=student("Lika",2019,"FeMale","Patna",["Statistics"])
stud5=student(["Jaanu","Chumpu","Dolu","Liku"], [1983,1988,2015,2019],["Male","Female","Female","Female"],["Canada","Patna","Paris","USA"],["Data Science","Data Analytics","Java","Statitics","NLP","Computer Vision"])
print(stud5.name)
print(stud5.course_list)
stud5.course_print()