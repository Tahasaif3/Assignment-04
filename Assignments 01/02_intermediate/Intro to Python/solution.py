## Milestone #1: Mars Weight

def weight_on_mars():
    earth_weight = float(input("Ente your weight on earth: "))
    mars_weight = round(earth_weight * 0.378, 2)
    print(f"The equivalent weight on mars: {mars_weight}")


## Milestone #2: Adding in All Planets
def planetary_weight():
    gravity_factors = {
         "Mercury": 0.376,
         "Venus": 0.889,
         "Mars": 0.378,
         "Jupiter": 2.36,
         "Saturn": 1.081,
         "Uranus": 0.815,
         "Neptune": 1.14 
    }

    earth_weight = float(input("Ente your weight on earth: "))
    planets = input("Enter a planet: ")

    if planets in gravity_factors:
        equivalent_weight = round(earth_weight * gravity_factors[planets],2) 

        print(F"The equivalent weight on {planets}: {equivalent_weight}")
    else:
        print("Invalid planet! please enter a valid name")


# you can Uncomment the function you want to run
# mars_weight()
planetary_weight()