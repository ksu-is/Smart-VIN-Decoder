import requests # =importing requests library to make HTTP requests

vin_history = {} # list to store the history of VINs decoded

def decode_vin(vin, allow_repeat=False): # Function to decode a VIN

    if vin in vin_history and not allow_repeat: #checking to see if the vin has already been stored in the history
        print("This VIN has already been decoded.")
        return

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
        model = result["Make"] or "Unknown Model"
        vin_history[vin] = model

    #vehicle information/summary

        print("\nVehicle Information:", vin)
        print(" =====================")
        print("Make:             ", result["Make"] or "UNAVAILABLE")
        print("Model:            ", result["Model"] or "UNAVAILABLE")
        print("Model Year:       ", result["ModelYear"] or "UNAVAILABLE")
        print("Manufacturer:     ", result["Manufacturer"] or "UNAVAILABLE")
        print("Engine Model:     ", result["EngineModel"] or "UNAVAILABLE")
        print("Engine Cylinders: ", result["EngineCylinders"] or "UNAVAILABLE")
        print("Fuel Type:        ", result["FuelTypePrimary"] or "UNAVAILABLE")
        print("Vehicle Type:     ", result["VehicleType"] or "UNAVAILABLE")
        print("Plant City:       ", result["PlantCity"] or "UNAVAILABLE")
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
                decode_vin(selected_vin, allow_repeat=True) # decode the selected VIN
                break
            else:
                print("\ninvalid choice. Try Again.") 
        else:
            print("\nPlease enter a valid number or 'back' to return to the menu.")
    

def delete_vin():
    if not vin_history:
        print("VIN history is empty. Nothing to delete.")
        return
    
    print("\n Previously Decoded VINs:")

    vin_list = list(vin_history.keys()) #get the keys from the vin 

    index = 0 #initializing the index to 0

    while index <len(vin_list):
        vin = vin_list[index] #get the vin from the list 
        model = vin_history[vin] #fetching the decoded model from the history dictionary
        print(str(index + 1) + ". " + model + " (VIN: " + vin + ")") #printing the vin and its corresponding model
        index += 1 #incrementing the index by 1

    while True: 
        choice = input("\nType the number of the VIN to delete or 'back': ").strip().lower()
        if choice == "back":
            break

        elif choice.isdigit():
            selected_index = int(choice) - 1 #converting the user's input to an int and subtracting 1 to get the corrrect index
            if selected_index >= 0 and selected_index < len(vin_list): #checks to make sure the selected index is within range
                selected_vin = vin_list[selected_index] #get the selected VIN from the list
                del vin_history[selected_vin] #deleting the selected vin from the history
                print("VIN " + selected_vin + " has been deleted from history.")
                break
            else:
                print("Invalid choice. Try again.")
        else:
            print("PLease enter a valid number or type 'back'.")
    


#main funct to run the program
def main():
    print("Welcome to the Smart VIN Decoder!")

    while True: # loop to ask for uer input
        print("\n ========= Menu =========")
        print("1) Decode a VIN")
        print("2) View Decoded VIN History")
        print("3) Delete a VIN from History")
        print("4) Exit")
        print("==========================") #stylizing the menu
        
        
        choice = input("Select an Option (1-4): ").strip() #taking the user input and stripping whitespace

        #ask the user for choice
        if choice == "1": #vin decoding option
            while True: #loop to ask for a VIN
                print("Type 'back' to return to the menu.\n")
                vin = input("\nEnter a 17-character VIN (or type 'back' to return to menu): ").strip().upper()

                if vin.lower() == "back":
                    break
                #option 1: decode vin
                elif is_valid_vin(vin):
                    decode_vin(vin)
                else:
                    print("Invalid VIN. Please try again.")

        #option 2: vin history
        elif choice == "2": 
            input_history()

        #option 3: delete vin
        elif choice == "3": 
            delete_vin()

        #option 4: exit
        elif choice == "4": #exit option
            print("Thank you for using the VIN Decoder! Goodbye!")
            break 
        else: #if the user enters an invalid option
            print("Invalid choice. Please select a valid option (1-4).")


#start the program
if __name__ == "__main__":
    main() # calling the main function to run the program