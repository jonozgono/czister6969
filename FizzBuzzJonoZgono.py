# parzyste = 0
# i = 0
# for i in range(0,4):
#     i +=1
#     parzyste +=2
#     print (parzyste)
# print("liczb parzystrych:",i)



# def print_name(first_name, last_name, age):
#     print(f"Twoje imie to: {first_name} {last_name} of age: {age}")
#
# print_name("bartek", age=13, last_name="draczyn")



# def greet(name):
#     print(f"Hi {name}")
#     return True
# print(greet("czister"))



# def multiply(*numbers):
#     print(numbers)
# multiply(2,3,4,5)



# def save_user(**user):
#     print(user)
# save_user(id = 1, name = "stasiek")



# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
# print(multiply(1,3,4,5))



def FizzBuzz():
    l=0
    for i in range(1,101):

        if (i %3==0 and i %5==0):
            return("FizzBuzz")
            l+=1
        elif (i %3 ==0):
            return("Fizz")
            l+=1

        elif (i %5 ==0):
            return("Buzz")

        else: return(i)

    print("liczby podzilne przez 3 wystapily", l ,"razy")

print(FizzBuzz())