class Temperature:
    def __init__(self, temp):
        self.temp = temp

    def convertFahrenheit(self):
        return ((9/5)*self.temp)+32

    def convertCelcius(self):
        return ((5/9)*self.temp)-32

temp_v = 1
choice = int(input("What temperature will you want to convert:\n(1)Farenheit->Celcius\n(2)Celcius->Farenheit?\n\t: "))
if choice == 1:
    temp_v = float(input("Enter the temperature °F: "))
    temp__t = Temperature(temp_v)
    print(f"The temp is {temp__t.convertCelcius()} °C")
else:
    temp_v = float(input("Enter the temperature (°C): "))
    temp__t = Temperature(temp_v)
    print(f"The temp is {temp__t.convertFahrenheit()} °F")

