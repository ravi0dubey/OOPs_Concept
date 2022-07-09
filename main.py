class car:
    def __init__(self,body1,engine1,tyre1):
        self.body = body1
        self.engine= engine1
        self.tyre1 = tyre1
    def print_mileage(self,mileage):
        self.mileage = mileage
        print("Mileage of this car " + str(self.mileage))


class hyundai(car):
    def print_car_Details(self):
        print(self.body)


car1=car("steel","1.2l","bigsize")
car1.print_mileage(21)
car2=hyundai("steel1","1.4l","bigsize1")
car2.print_car_Details()


#multilevel inheritance
class bank:
    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("This will show you your account open status")
    def deposit(self):
        print("this will show your deposited amount")

class HDFC_bank(bank):
    def HDFC_to_ICICI(self):
        print("This will show you all transaction happened to ICICI through HDFC")
    def test(self):
        print("test_HDFC")

class ICICI(HDFC_bank):
    pass

#multiple inheritance
class KOTAK:
    def kotak_print(self):
        print("inside kotak")
    def test(self):
        print("test_KOTAK")

class YES:
    def yes_print(self):
        print("inside YES")
    def test(self):
        print("test_YES")

class NEW_BANK(KOTAK,HDFC_bank,YES):
    def new_bank_account_opening(self):
        print("opening a new bank account under multiple inheritance")


#Testing multilevel Inheritance
bank1= ICICI()
bank1.transaction()
bank1.HDFC_to_ICICI()

#Testing multiple Inheritance
bank2=KOTAK()
bank3=NEW_BANK()
bank3.HDFC_to_ICICI()
bank3.new_bank_account_opening()
bank3.test()


class student1:
    def __init__(self,name1,age1):
        self.name = name1
        self.age = age1
    def student1(self):
        print("details of all the students")
    def achievers(self):
        print("details of all the achievers")
    def hall_of_fame(self):
        print("details of  everyone from hall of fame")

class student_vision(student1):
    def __init__(self,name1,age1,subject1):
        super().__init__(name1,age1)
        self.subject = subject1

    def student1(self):
        print("Name " + self.name)
        print("Age" + str(self.age))
        print("Subject " + self.subject)

stud1 = student1("Ravi",39)

stud1.student1()
stud2 = student_vision("Astha",35, "Physics")
stud2.student1()

