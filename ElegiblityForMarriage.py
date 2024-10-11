class Elegible():
    def eligibility():
        gender = str(input("Enter your gender (male/female): "))
        age = int(input("Enter your age: "))
        
        if gender == 'male' and age >= 21:
            print('Eligible')
        elif gender == 'female' and age >= 18:
            print('Eligible')
        elif gender == 'male' and age < 21:
            print('Not Eligible')
        elif gender == 'female' and age < 18:
            print('Not Eligible')
        else:
            print('Invalid input')

