weather_data = []

def add_weather():
    city = input("Enter city: ")
    temperature = input("Enter temperature: ")
    weather_data.append({"city": city, "temperature": temperature})
    print("Weather data added")

def view_weather():
    for data in weather_data:
        print(data["city"], "-", data["temperature"])

def main():
    while True:
        print("1. Add Weather")
        print("2. View Weather")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_weather()
        elif choice == "2":
            view_weather()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
