import requests # =importing requests library to make HTTP requests

vin_history = {} # list to store the history of VINs decoded

def decode_vin(vin): # Function to decode a VIN
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/' + vin + '?format=json' # URL for the NHTSA API

    response = requests.get(url) # making a GET request to the API

    # the code 200 shows that the request was successful
    if response.status_code == 200: 
        data = response.json() # parsing the json response from the api
        result = data["Results"][0] # get the first result from the response

        key_fields = ["Make", "Model", "ModelYear"] #defining the key fields to be displayed 
        if all (result[field] == "" for field in key_fields): # checking if the key fields are empty
            print("Error: No data found for the provided VIN.")
            return
        
        #store the VIN + model in the history 
        model = result["Make"]
        vin_history[vin] = model

    #vehicle information/summary

        print("\nVehicle Information:")
        print(" =====================")
        print("Make:             ", result["Make"])
        print("Model:            ", result["Model"])
        print("Model Year:       ", result["ModelYear"])
        print("Manufacturer:     ", result["Manufacturer"])
        print("Engine Model:     ", result["EngineModel"])
        print("Engine Cylinders: ", result["EngineCylinders"])
        print("Fuel Type:        ", result["FuelTypePrimary"])
        print("Vehicle Type:     ", result["VehicleType"])
        print("Plant City:       ", result["PlantCity"])
        print(" =====================")

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

def input_history():
    if not input_history:
        print("No VINs decoded yet.")
        return

    print("\nPreviously Decoded VINs: ")
    vin_list = list(vin_history.keys()) # get the keys from the vin_history dictionary

    for i in range(len(vin_list)):

        vin = vin_list[i] # get the VIN from the list at index i
        model = vin_history[vin] # try to get the decoded model from the vin_history dictionary
        #printing the VIN and its corresponding model and make
        print("{}. {} (VIN: {})".format(i + 1, model, vin))

    while True: #back option
        choice = input("\nSelect a number to re-view details or type 'back' to return to menu: ").strip().lower()

        if choice == "back":
            break
        elif choice.isdigit():
            index = int(choice) - 1 #converts the user's input (string) to an integer and subtracts 1 to get the correct index
            if 0 <= index < len(vin_list): #checks the index is within the range of the vin_list
                selected_vin = vin_list[index] # get the selected VIN from the list
                decode_vin(selected_vin) # decode the selected VIN
                break
            else:
                print("\ninvalid choice. Try Again.") 
        else:
            print("\nPlease enter a valid number or 'back' to return to the menu.")
    

#main funct to run the program
def main():
    print("Welcome to the Smart VIN Decoder!")

    while True: # loop to ask for uer input
        print("\n ========= Menu =========")
        print("1) Decode a VIN")
        print("2) View Decoded VIN History")
        print("3) Exit")
        print("==========================") #stylizing the menu
        choice = input("Select an Option (1-3): ").strip() #taking the user input and stripping whitespace
        print("==========================")

        #ask the user for choice
        if choice == "1": #vin decoding option
            vin = input("\nEnter a 17-character VIN: ").strip().upper()

            #option 1: decode vin
            if is_valid_vin(vin):
                decode_vin(vin)
            else:
                print("Invalid VIN. Please try again.")

        #option 2: vin history
        elif choice == "2": 
            input_history()
        
        #option 3: exit
        elif choice == "3": #exit option
            print("Thank you for using the VIN Decoder! Goodbye!")
            break 
        else: #if the user enters an invalid option
            print("Invalid choice. Please select a valid option (1-3).")
#start the program
if __name__ == "__main__":
    main() # calling the main function to run the program