from validation import isValidEmail
from personClass import person


class employee(person):

    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.__id = id
        self.__car = car
        self.__email = email
        self.__salary = salary
        self.__distanceToWork = distanceToWork

    def get_salary(self):
        return self.__salary
   

    
    def set_salary(self, _salary):
        if _salary < 1000:
            self.__salary = 0
        if _salary > 1000:
            self.__salary = _salary

    def work(self, hours):
        status="none"
        if(hours == 8):
            status="happy"
        elif(hours > 8):
            status="tired"
        elif(hours < 8):
            status="Lazy"

        return str(status)

   
    def get_email(self):
        return self.__email

    
    def set_email(self):
        _email = isValidEmail()
        self.__email = _email

    def get_healthRate(self):
        return self.healthRate

    def set_healthRate(self, health):
        if health >= 0 and health <=100:
            self.healthRate = health

    def drive():
        pass

    def refuel():
        pass

    def send_mail():
        pass


  
# p = employee("ahmed", 3000, "any", 100, 1, "fiat", "any", 3000, 20)

