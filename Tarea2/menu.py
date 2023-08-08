import menu_options 


print(f"\nWelcome to the Pokedex!")
print(f"What brings you here today?")
print("Press the letter according desired option\n")


    
def menu():
    
    menu_option = input("\nPress 'A' for Pokemons information \nPress 'B' for Pokemon stats information\nPress 'C' for Pokemon specific information\nPress 'D' to shut down\nI choose option : ").lower()

    if menu_option == "a":
        print("\nWhich information would you like to see?")
        information = input("Press 'A' for pokemon by type \nPress 'B' for Pokemon by generation\nPress 'C' to start over \nPress 'D' to shut down \nI choose option : ")
        
        
        if information == "a":
            menu_options.option_a()
            print("\nIs there something else?")
            menu()
        elif information =='b':
            menu_options.option_b()
            print("\nIs there something else?")
            menu()
        elif information =='c':
            menu()
        else:
            print("See you next time! ")
            menu()

    elif menu_option == "b":
        menu_options.poke_stats_viewer()
        print("\nIs there something else?")
        menu()

    elif menu_option=="c":
        menu_options.menu_pokedex()
        print("\nIs there something else?")
        menu()

    elif menu_option=="d":
        print("See you next time!")

        


menu()



