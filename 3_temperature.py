# convert farenheit to Celsius

tempF = int(input("Temperature in Farenheit: "))

def fahToCel(T):
    return((T-32)*5/9)


print(f"Celsius: {fahToCel(tempF):.2f}")