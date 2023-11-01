def perform_operation(operator, num1, num2):
    if operator == 1:
        return num1 * num2
    elif operator == 2:
        return num1 - num2
    elif operator == 3:
        return num1 + num2
    elif operator == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "0 bolme olmaz"
    else:
        return "Sehv operator"

try:
    print("Elave edin")
    print("Vurma (1), Cixma (2), Ustegel (3), bolme (4)")

    operator = int(input("Operator daxil edin (1/2/3/4): "))
    if operator not in [1, 2, 3, 4]:
        raise ValueError("Invalid operator")

    num1 = float(input("Birinci reqemi daxil edin: "))
    num2 = float(input("Ikinci reqemi daxil edin: "))

    result = perform_operation(operator, num1, num2)
    if isinstance(result, str):
        print("Error:", result)
    else:
        print(f"Cavab: {num1} {'*+-/'[operator - 1]} {num2} = {result}")

except ValueError:
    print("Error: Zehmet olmasa reqemi ve operatoru daxil edin")
except ZeroDivisionError:
    print("Error: 0 bolme olmaz")
except Exception as e:
    print(f"Error: {e}")