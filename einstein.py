def main():
    speed_of_light = 300000000  # meters per second

    mass_kg = int(input("Enter mass in kilograms: "))
    energy_joules = mass_kg * (speed_of_light ** 2)

    print("Equivalent energy in Joules:", energy_joules)

if __name__ == "__main__":
    main()
