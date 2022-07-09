class course:
    def __init__(self):
        self._instructor = "Ravi Dubey"
        self.batch_strength = 20

    def __str__(self):
        return "****************This is default string function for course class**********"

    def course_setup(self,course_name,batchname,instructor,fee):
        self.course_name = course_name
        self.__batch= batchname
        if instructor:
            self._instructor=instructor  #protected variable
        else:
            self._instructor= "Ravi Dubey"
        self.fee= fee


    def course_print(self,):
        print("course_name :" + self.course_name )
        print("batchname : "+ self.__batch)
        print("instructor name : " + self._instructor)
        print(f"Fee structure :  {self.fee}" )
        print(f"Batch Strength : {self.batch_strength}")


c1 = course()
c1.course_setup("Data Science","July 2022", "Sudhanshu", 17700)
c1.course_print()

#changing protected variable instructor using class object and instructor variable
c1._instructor= "Deva"
print(c1._instructor)

# changing protected variable instructor using class name and  instructor variable
course_instructor ="Raja Babu"
print(course_instructor)

c1.course_course_name ="Python"
print(c1.course_course_name)

#changing private variable batch using class object and instructor variable
c1.__batch= "June 2022"
print(c1.__batch)

#changing private variable instructor using class object and instructor variable
c1.course__batch= "May 2022"
print(c1.course__batch)

print(c1)

c2= course()
c2.course_name= "Data Analytics"
c2._course__batch = "August 2022"
c2.fee= 4000
c2.course_print()
print(c2)