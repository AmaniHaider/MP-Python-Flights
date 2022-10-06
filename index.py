class Person:
    def __init__(self, name, age, passport_number):
        self.name = name
        self.age = age
        self.passport_numbers = passport_numbers

class Passenger(Person):
    def __init__(self, name, age, passport_number, number_of_bags, destination):
        super().__init__(name, age, passport_number)
        self.number_of_bags = number_of_bags
        self.destination = destination

    def get_bag_weight(self):
        return(self.number_of_bags* 23)

    def __str__(self):
        return(f"name{self.name}, age{self.age}, passport_number{self.passport_number}, number_of_bags{self.number_of_bags}, destination{destination}")

    
class Captain(Person):
    def __init__(self, name, age, passport_number, experience_years, salary):
        super().__init__(name, age, passport_number)
        self.experience_years = experience_years
        self.salary = salary

    def get_bonus(self):
        exp = 1/100
        for exp in experience :
            print('experience years/100, * self.salary')

    def __str__(self):
        return(f"name{self.name}, age{self.age}, passport_number{self.passport_number}, experience_years{self.experience_years}, salary{self.salary}")


        list = []
        list.append(Passenger('Amani', 35))

        list1 = []
        list1.append(Captain('Ahmad', 4))

    def get_options():
        returns["1.show persons", "2.Show captions", "3.Add person", "4.Add caption"]

    def get_user_options(options):
        show_options(options)
        chosen_options = [input("Choose a number:")]
        return[options[int(selected) - 1] for selected in chosen_options]

    def main():
        print("Welcome to CODED Airline, Please Answer the following questions:")
        
        options = get_options()
        if options == 1:
            print(self.Passenger)

        elif option == 2:
            print(self.Captain)

        elif option == 3:

            user1 = input("please enter your name:")
            age1 = input("please enter your age:")
            return(user1, age1)

        elif option == 4:
            user2 = input("please enter your name:")
            years2 = input("please enter your experience years:")
            return(user2, years2)

         
            
    
        





    
        
