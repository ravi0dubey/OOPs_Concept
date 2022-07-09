#class Student
class student:
    def __init__(self, name1,course):
        self.course_list = []
        self.name1 = name1
        # for i in course:
        #     self.course_list.append(i)
        self.course = course
    def print_student_details(self):
        print(f"Student Name: {self.name1}")
        print(f"Student courses: {self.course_list}")
        print(f"Student courses: {self.course}")

#class Student_jobs inheriting Class Student
class student_jobs(student):
    def __init__(self,name2,jobs,*courses2):
        super().__init__(name2,*courses2)
        self.job= jobs

    def print_student_job_details(self):
        self.print_student_details()
        print(f"Student job details:{self.job} ")

#class Student_college
class student_college:
    def __init__(self,studname1,studcollege1):
        self.studname1 = studname1
        self.college_name= studcollege1

    def print_student_college_details(self):
        print(f"Student Name in college: {self.studname1}")
        print(f"College Name: {self.college_name}")

# Multiple inheritance
#class student_internship,inheriting student and student_college
class student_intership(student_college,student):
    def __init__(self,year_intership, batchname,name3,studcollege3,studname,cours):
        student_college.__init__(self,studname1 = name3,studcollege1 = studcollege3)
        student.__init__(self,name1=studname,course=cours)
        try:
            self.year_of_internship = year_intership
        except Exception as e:
            print("Incorrect year of internship", e)
        self.batch_name = batchname

    def print_internship_details(self):
        self.print_student_details()
        self.print_student_college_details()
        print(f"Student_year_internship: {int(self.year_of_internship)}")
        print(f"student_batchname: {self.batch_name}")






# student1= student("Ravi","Data Science","Data Analytics","Java")
student1= student("Ravi","Data Analytics")
student1.print_student_details()

# student1_jobs1 = student_jobs("Ravi","Senior Software Engineer","Data Science","Data Analytics","Java")
# student1_jobs1.print_student_job_details()

student_college1= student_college("Ravi Ranjan","CDAC")
student_college1.print_student_college_details()


student_intership1= student_intership("2022","FSDS May 2022","Ravi Ranjan","CDAC","Ravi","Data Science")
student_intership1.print_internship_details()