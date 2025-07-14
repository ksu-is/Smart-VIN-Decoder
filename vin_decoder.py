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
    print("Welcome to the Smart VIN Decoder!")

    while True: # loop to ask for uer input
        print("\n Menu")
        print("1) Decode a VIN")
        print("2) Exit")
        choice = input("Select an Option (1-2): ").strip() #taking the user input and stripping whitespace

        if choice == "1":
            vin = input("\nEnter a 17-character VIN: ").strip().upper()
            if is_valid_vin(vin):
                decode_vin(vin)
            else:
                print("Invalid VIN. Please try again.")
        elif choice == "2":
            print("Thank you for using the VIN Decoder! Goodbye!")
            break 

#start the program
if __name__ == "__main__":
    main() # calling the main function to run the program