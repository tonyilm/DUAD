

def sum(current_number,second_number):
    return current_number + second_number


def subtract(current_number,second_number):
    return current_number - second_number

def multiply(current_number,second_number):
    return current_number * second_number

def divide(current_number,second_number):
    return current_number / second_number


def main():
    result = 0
    while True:
        print(f"Current result: {result}")
        try:
            operation = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Erase result\nChoose the operation to perform : "))
        except ValueError as e:
            print(f"Error [ValueError]: You must enter a numeric value. Detalils: {e}")
            continue
        if operation == 5:
            result = 0
            print("Result has been erased")
            continue
        elif operation <1 or operation > 5 :
            print("Value must be within 1 and 5")
            continue
        try:
            num = float(input("Enter a number: "))
        except ValueError as e:
            print(f"Error [ValueError]: You must enter a numeric value. Details: {e}")
            continue
        if operation == 1:
            print("Addition + ")
            result = sum(result,num)
            
        elif operation == 2:
            print("Subtraction - ")
            result = subtract(result,num)
            
        elif operation == 3:
            print("Multiplication * ")
            result = multiply(result,num)
            
        elif operation == 4:
            print("Division / ")
            try:
                result = divide(result,num)
            except ZeroDivisionError as e:
                print(f"Error [ZeroDivisionError]: You tried to divide by zero. Details:  {e}")
           

if __name__ == "__main__":
    main()