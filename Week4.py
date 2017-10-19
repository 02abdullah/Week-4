#Logbook req 1
name = input('Hello, who are you?')
print ('Hello, ' + name.capitalize() + '. It is good to meet you')

#Logbook req 2

def fahrenheit (tcelsius):
    tfahrenheit =  (tcelsius*1.8+32)
    return tfahrenheit
fahrenheitInput = input('Enter a Celsius Temperature: \n example 19C')
if 'c' in fahrenheitInput.lower():
    tempFahrenheit = float((fahrenheitInput[:-1]))
    print(fahrenheitInput.upper() + ' is', str(round(float(fahrenheit(tempFahrenheit)), 1)) + 'F')
else:
    tempFahrenheit = float(fahrenheitInput)
    print(fahrenheitInput + 'C is', str(round(float(fahrenheit(tempFahrenheit)), 1)) + 'F')
