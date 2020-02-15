#klasa EMployee
#
# class Employee:
#     def __int__(self, imie, nazwisko, stawka, time):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.stawka = stawka
#         self.pay = stawka * time
#     def __str__(self):
#         return f"Employee: {self.imie}, {self.nazwisko}, {self.stawka}, {self.pay}"
#     def register_time(self):
#         print(f"Employee")


class TestEmployee:
    def __int__(self, f_name, l_name, rph):
        self.first_name = f_name
        self.last_name = l_name
        self.rate_per_hour = rph
        self. _worked_normal_hours = 0
        self._worked_overhours = 0

    def register_time_(self, hours):
        if hours > 8:
            self._worked_normal_hours +=8
            self._worked_overhours += hours - 8
        else:
            self._worked_normal_hours += hours


    def pay_salary(self):
        to_pay = self._worked_hours * self.rate_per_hour + self._worked_overhours * 2* self.rate_per_hour
        self.__worked_hours = 0
        self._worked_overhours = 0
        return to_pay


def test_init(self):
    employee = Employee("Jan", "Nowak", 100.0)
    assert employee.first_name == "Jan"
    assert employee.last_name == "Nowak"
    assert employee.rate_per_hour == 100.0

def test_register_time(self):
    employee = Employee("Jan", "Nowak", 100.0)
    employee.register_time(5)
    assert employee._worked_normal_hours == 5

def test_pay_salary_when_no_worked_hours(self):
    employee = Employee("Jan", "Nowak", 100.0)
    assert employee.pay_salary() == 0

def test_pay_salary_with_worked_hours(self):
    employee = Employee("Jan", "Nowak", 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 5*100
    assert employee.pay_salary() == 0

def test_pay_salary_overhours(self):
    employee = Employee("Jan", "Nowak", 50)
    employee.register_time(10)
    assert employee.pay_salary() == 8 * 50 + 2*2*50
    assert employee.pay_salary() == 0