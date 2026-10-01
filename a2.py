while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        print("Result is", result)
    except ZeroDivisionError:
        print("Division by zero is not allowed !!")
    except SyntaxError:
        print("Coma is missing. Enter like this 1,2")
    except ValueError:
        print("Please enter valid whole numbers")
    except:
        print("Wrong input")
    else:
        print("No exceptions")
    finally:
        print("This will execute no matter what")