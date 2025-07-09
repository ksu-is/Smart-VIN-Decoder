import requests # =importing requests library to make HTTP requests

def decode_vin(vin): # Function to decode a VIN
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/' + vin + '?format=json' # URL for the NHTSA API

    response = requests.get(url) # making a GET request to the API

    # the code 200 shows that the request was successful
    if response.status_code == 200: 

        data = response.json() # parsing the json response from the api
        result = data["Results"][0] # get the first result from the response

    #vehicle information/summary

        print("\nVehicle Information:")
        print("Make:             ", result["Make"])
        print("Model:            ", result["Model"])
        print("Model Year:       ", result["ModelYear"])
        print("Manufacturer:     ", result["Manufacturer"])
        print("Engine Model:     ", result["EngineModel"])
        print("Engine Cylinders: ", result["EngineCylinders"])
        print("Fuel Type:        ", result["FuelTypePrimary"])
        print("Vehicle Type:     ", result["VehicleType"])
        print("Plant City:       ", result["PlantCity"])
    else:
        print("Error: Could not connect to the NHTSA API.")

#validating the VIN format (7 characters letters & numbers)
def is_valid_vin(vin):
    if len(vin) != 17:
        print("Error: VIN must be 17 characters long.")
        return False
    elif not vin.isalnum():
        print("Error: The VIN must contain only letters and numbers.")
        return False
    elif vin.isdigit():
        print("Error: The VIN must contain at least one letter.")
        return False
    else:
        return True
    
#main funct to run the program
def main():
    print("Welcome to the VIN Decoder!")
    print("Created by Sam Miller\n")

while True: # loop to continuously ask for user input
    user_input = input("Please enter a 17-character VIN (or type 'exit' to quit): ")
    vin = user_input.strip().upper() #the input to be stripped of whitespace and converted to uppercase

    if vin == 'EXIT':
        print("Thank you for using the VIN Decoder!")
        break
    elif is_valid_vin(vin):
        decode_vin(vin)
    else:
        print("Invalid VIN. Please try again.")

#start the program
if __name__ == "__main__":
    main() # calling the main function to run the program