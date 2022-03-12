from re import S


class person:
    def __init__(self,name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate
    
    def sleep(self, hours):
        status="none"
        if(hours == 7):
            status="happy"
        elif(hours > 7):
            status="tired"
        elif(hours < 7):
            status="Lazy"

        return str(status)

    def eat(self, meals):
        status="none"
        if(meals == 3):
            status=f"100% heathy"
        elif(meals == 2):
            status=f"75% heathy"
        elif(meals == 1):
            status=f"50% heathy"
        return status

    def buy(self, items):
        self.money = self.money - (items * 10)
        

    
