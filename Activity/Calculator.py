print("Simple Calculator (type 'exit' to quit)")
while True:
    expr = input("Enter expression: ")
    if expr.lower() == "exit":
        break
    try:
        result = eval(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
