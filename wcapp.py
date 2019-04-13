#!/usr/bin/python

# Takes input for yearly salary
def take_input1():
    inputData1 = input("Ka du tjen i året? ")

    # Check if input was int
    try:
        inputData1 = int(inputData1)

    # If not int then prompts user
    except ValueError:
        print("Bruk tall, du tjen ikke bokstava. ")

        # And tries again
        inputData1 = take_input1()
    return inputData1

# Takes input for yearly salary
def take_input2():
    inputData2 = input("Kor lenge va du på dass? (minutta) ")

    # Check if input was int
    try:
        inputData2 = int(inputData2)

    # If not int then prompts user
    except ValueError:
        print("Bruk tall, kan du ikke klokka? ")

        # And tries again
        inputData2 = take_input2()
    return inputData2

# Puts salary from variable
salary = take_input1()

# Puts time from variable
time = take_input2()

# Joins it together and tells you how much you earned
shitMoney = int((salary / 1850) / 60 * time)

# And prints it
#print('You earned '(shitmoney)' while sitting on the throne.')
print('Du tjent {} krona mens du satt å dreit.'.format(shitMoney))