
# To practice:

# -List comprehension

# -Dictionary comprehension
new_dict = {new_key:new_value for (key,value) in dict.items() if test}



# List/Dictionary comprehension
import random
import pandas as pd
names = ['a','b','c','d','e']
names_dict = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student, score) in names_dict.items() if score >= 20}


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence_list = sentence.split(' ')
sentence_dict = {word:len(word) for word in sentence.split(' ')}


weather_c = {
    'Mon': 12,
    'Tue': 14,
    'Wed': 15,
    'Thur': 14,
    'Fr': 21,
    'Sat': 22,
    'Sun': 24
}

weather_f = {day:(temp*9/5)+32 for (day,temp) in weather_c.items()}


nato = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index,row) in nato.iterrows()}
word = input('Provide the word: ').upper()
word = [letter for letter in word]
print([nato_dict[letter] for letter in word])






# - *args
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,5,10,100))


# - **kwargs
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)



class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get('make') #get won't give an error when one of kwargs not specified
        self.model = kwargs.get('model')

my_car = Car(make = 'nissan', model='micra')
my_car = Car(make = 'nissan')
print(my_car.model)