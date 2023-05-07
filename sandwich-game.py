print("\n\nLets - Make - A...")
print("                     _          _      _        _ ")
print("                    | |        (_)    | |      [ ]")
print(" ___  __ _ _ __   __| |_      ___  ___| |__    [ ]")
print("/ __|/ _` | '_ \ / _` \ \ /\ / / |/ __| '_ \   [ ]")
print("\__ \ (_| | | | | (_| |\ V  V /| | (__| | | |  [_]")
print("|___/\__,_|_| |_|\__,_| \_/\_/ |_|\___|_| |_|  (-)\n \n")
print("Enter 'quit' to quit at any time")
print("")


bread = ''
toasted = ''
condiments = ''
toppings = ''
cheese = ''
bread_used = []
condiments_used = []
toppings_used = []

def printline():
    print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")

def add_bread (ing):
    bread_used.append(ing)

def add_condiments(ing):
    condiments_used.append(ing)

def add_toppings(ing):
    toppings_used.append(ing)

total_ings_used = 0
def ings_sum (total_ings_used):
    total_ings_used += 1
    return total_ings_used

while True:
    printline()
    bread = input("1st, choose a bread:\n  Rye, Wheat, Sourdough, White, or none. \n").lower()
    if 'quit' in bread:
        quit()
    if 'none' in bread:
        printline()
        print("No bread, you got it! Let's move on to picking condiments.")
        printline()
        pass      
    else:
        total_ings_used = ings_sum(total_ings_used) ; add_bread(bread)
        printline()
        toasted = input("\nWould you like it toasted? [Y]es, or [N]o \n").lower()
        printline()
        if 'quit' in toasted:
            break
        if toasted == 'y':       
            toasted = 'Toasted'
            print(f'\nOK, we\'ll use {toasted} {bread} bread. \n')
    printline()
    print("List of condiments:")
    print ("  Yellow Mustard, Brown Mustard, Stadium Mustard\n  Heinz Ketchup, Red77 Ketchup\n  Hellmans Mayonnaise, Miracle Whip\n  Pesto, Garlic Aioli \n")
    while True:
        condiments = str(input("Enter condiments from the list above. Enter 'done' when you've finished making your selections. \n "))
        if 'quit' in condiments:
            quit()
        elif 'done' in condiments:
            printline()  
            print(f"\nYou chose {', ' .join(condiments_used)}.\n")       
            break
        else:
            total_ings_used = ings_sum(total_ings_used) ; add_condiments(condiments) 
    print("Choose your toppings!")    
    printline()
    print ("  Ham, Turkey, Grilled Chicken, Fried Chicken, Bologna, Salami, Pastrami, No Meat\n  Lettuce, Spinach, Kale, Sprouts, Romaine, Mixed Greens\n  Red Onion, White Onion, Tomatoes, Pickles, Avacado, Giardiniera")  
    while True:
        toppings = str(input("Enter toppings from the list above. Enter 'done' when you've finished making your selections. \n "))
        if 'quit' in toppings:
            quit()
        elif 'done' in toppings:    
            print("\nOK, let's put it all together...\n\n")    
            break
        else:
            total_ings_used = ings_sum(total_ings_used) ; add_toppings(toppings)   
    print(f"you ordered a sandwich with {bread} bread, {', ' .join(toppings_used)}, {', ' .join(condiments_used)}.\n That would look something like...\n\n")
    print("                     _.---._")
    print("                 _.-~       ~-._")
    print("             _.-~               ~-._")
    print("         _.-~                       ~---._")
    print("     _.-~                                 ~\"")
    print("  .-~                                    _.;")
    print("  :-._                               _.-~ ./")
    print("  `-._~-._                   _..__.-~ _.-~")
    print("   /  ~-._~-._              / .__..--~----._")
    print("  \_____(_;-._\.        _.-~_/       ~).. . \"")
    print("     /(_____  \`--...--~_.-~______..-+_______)")
    print("   .(_________/`--...--~/    _/nad        /\"")
    print("  /-._     \_     (___./_..-~__.....__..-~./")
    print("  `-._~-._   ~\--------~  .-~_..__.-~ _.-~")
    print("      ~-._~-._ ~---------'  / .__..--~")
    print("          ~-._\.        _.-~_/")
    print("              \`--...--~_.-~")
    print("               `--...--~\n\n")
    quit()