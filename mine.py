
class person:
    Name = "Abdullah"
    age = 18
    def is_adult(self):
        if person >=18:
            print("You have too much responsibilities")
        else:
            print("Lucky you")    



    def __init__(self, name, age):
        self.name = name 
        self.age = age 



    def __str__(self):
        return f"My name is John and I am 22 years old"
    
first_person = person("Abdallah", 18)
print(first_person)    