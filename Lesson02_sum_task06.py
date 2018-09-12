num_one = input("Enter first sum: ")
num_two = input("Enter second sum: ")

def get_summ(num_one, num_two):
    try:
        get_summ = int(num_one) + int(num_two)
        print(get_summ)
    except ValueError:
        return "Please, use good types"


get_summ = int(num_one) + int(num_two)
print(get_summ)
