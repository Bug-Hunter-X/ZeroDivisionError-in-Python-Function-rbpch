def function(a, b):
    if b == 0:
        return "Division by zero error"
    else:
        return a / b

result = function(10, 0)
print(result) # Output: Division by zero error
result = function(10,2)
print(result) # Output: 5.0