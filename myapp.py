import pandas as pd 

dt = pd.read_csv("dragon_ball_z_characters.csv", encoding="utf-8")




def user_action():  
    running = True 
    while running:
        try:
            choice = int(input("\t Please enter your choice: "))
        except ValueError:
            print("\n\t\tInvalid choice.\n\t\tPlease enter a number between 1-6 .\n")
            continue
        if choice == 1 :
            print("\n********* CHARACTER SESRCHING *********\n")
            char_name = input("\t Enter your character name : ")
            try:
                name = dt[dt["name"]==char_name].iloc[0]
                gender = name["gender"]
                race = name["race"]
                ki = name["ki"]
                image = name["image"]
                affiliation = name["affiliation"]

                print(f"\n\t {char_name} is a {gender} {race} from the {affiliation} side, with a ki of {ki}.\n")
                print(f"\t here is a picture of {char_name} by following the next link :\n\n\t {image}\n")
                
            except IndexError :
                print(f"\n\t{char_name} is not currently a DRAGON_BALL Z charachter\n")
                continue
                

        
        elif choice == 2 :
            print("\n**************** RACE SORTING *******************\n")
            print("\t DBZ has a lot of characters with different races .\n\t But the main races are 'Saiyan' , 'Human' , 'God', 'Namekian' ,'Frieza Race', 'Android', 'Majin' ,'Evil'\n")
            race = input("\tView all characters belonging to a specific Race from the above: ")
            try:
                chars = dt[dt["race"]==race]["name"].tolist()
                print(f"\n\tHere are the charcacters from {race} race :\n")
                for name in chars:
                    print(f"\t{name}")
            
            except IndexError:
                print(f"\n\t\n\t the race '{race}' is invalid . \nPLease enter one from the above \n")
                continue


        elif choice == 3 :
            print("\n****************** CHARACTER KI *****************\n")
            print("\t In DRAGON BALL Universe , the ki stands for Base power level/fighting strength of the character\n")
            char = input("\twho is the character : ")
            try:
                 serie = dt[dt["name"]==char].iloc[0]
                 ki = serie["ki"]
                 max_ki = serie["maxKi"]
                 print(f"\n\t{char} has a ki of '{ki}' \n\twith a Max KI of '{max_ki}'\n")
            except IndexError:
                print("\n\tthe character '{char}' doesn't exist\n\t Try to look for all characters (option 5)\n")
                 


        elif choice == 4 :
            print("\n*************** UNDERSTAND SPECIFIC COLUMN FEATURES *****************\n")
            print("\t - name: Character's full name as shown in the series\n")
            print("\t - ki: Base power level/fighting strength of the character\n")
            print("\t - maxKi: Maximum power level achievable by the character\n")
            print("\t - race: Character's species or racial background (e.g., Saiyan, Human, Namekian)\n")
            print("\t -affiliation: Character's primary group allegiance or association \n")
            
        elif choice == 5 :
            print("\n**************** ALL CHARACTERS ******************\n")
            print("\n\t Here are all the DBZ characters :\n")
            names = dt["name"].to_list()
            for name in names :
                print(f"\t - {name}")
            print("\n")

        
        elif choice == 6 :
            print("\n**************** GOOD BYE ************\n ")
            running = False  

        else:
            print(f"\nWARNING :\toption '{choice}' is invalid .\n\t\tPlease enter a number between 1-6 .\n")


def options():
    print("\t\t*** Here is what you can do ?***\n")
    print("\t\t 1- Search a character\n")
    print("\t\t 2- Filter by race\n")
    print("\t\t 3- Who is stronger between 2 characters \n")
    print("\t\t 4- Understand column features\n")
    print("\t\t 5- ALL Characters\n")
    print("\t\t 6- EXIT\n")

def welcome():
    try:
        print("\n******************* DRAGON_BALL Z  CHARACTERS REVIEW ******************* \n ")
        print("\t\t\tDesigned by Yohan .\n")
        options()
        user_action()    
    except KeyboardInterrupt:
        print("\n\t\tApp STOPPED\n")
if __name__ == "__main__" :
    welcome()
