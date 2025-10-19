###UPC code check. Alisa Dzhoha. This program asks the user to type a UPC number and then figures out if it’s a good one or not by checking the last number. It uses the UPC A way to do the math and tells if the barcode works or not. 10/18/2025


def find_UPC(barcode):
    totalNumber = 0
    i = 0
    while i < 11:
        number = int(barcode[i])
        if i % 2 == 0:
            totalNumber = totalNumber + (number * 3)
        else:
            totalNumber = totalNumber + number
        i += 1

    remainder = totalNumber % 10
    check_digit = 10 - remainder

    if check_digit == 10:
        check_digit = 0
    return check_digit

user_input = input("Please input your barcode UPC number: ")

valid = True

for character in user_input:
    if character >= '0' and character <= '9':
        valid = True
    else:
        valid = False
    if valid == False:
        break

if len(user_input) == 12 and valid:
    
    result = find_UPC(user_input)
    last_digit = int(user_input[-1])

    if result == last_digit:
        print("Your UPC code is vaild")
    else:
        print("Your UPC code is invalid")

else:
    print("Sorry, your barcode is incorrect. Please try again")


