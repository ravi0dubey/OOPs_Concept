#using polymorphism feature for function print_internship_details to print student details and then internship details


class student_intership:
    def __init__(self, name, year_intership, batchname):
        self.name = name
        try:
            self.year_of_internship = year_intership
        except Exception as e:
            print("Incorrect year of internship", e)

        self.batch_name = batchname

    def print_internship_details(self):
        print(f"Student_Name: {self.name}")
        print(f"Student_year_internship: {int(self.year_of_internship)}")
        print(f"student_batchname: {self.batch_name}")


class internship:
    def __init__(self,name, year_intership, batchname, *domain):
        self.domain_list = []
        self.name=name
        try:
            self.year_of_internship = year_intership
        except Exception as e:
            print("Incorrect year of internship", e)

        self.batch_name = batchname
        for i in domain:
            self.domain_list.append(i)

    def print_internship_details(self):
        print(f"Project Details: {self.domain_list}")

s1 = student_intership("Ravi Dubey",2022,"FSDS MAY 2022")
s1.print_internship_details()

s2 = internship("Ravi Dubey",2022,"FSDS MAY 2022","Automative","Banking","E-commerce")
s2.print_internship_details()