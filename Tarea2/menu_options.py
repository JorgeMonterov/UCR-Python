import pokedex
import pokedex2

#Heres  a menu calling assigned function from previous pokedex2 providing the return with the correct answer acording user experience in menu.py 
def option_a():
    print("\nGreatnews! Now information can be displayed in many ways! Choose your favorite! ")
    type_bar = input(" Press 'A' to see information in a list \n Press 'B' to see information in a bar chart \n Press 'C' to see information in a pie chart\nI choose option : ")
    if type_bar =='a':
     return pokedex2.pokemon_list()
    
    elif type_bar == 'b':
     df = pokedex2.pokemon_type_listed()
     pokedex2.bar_chart(df)

    elif type_bar == 'c':
     df = pokedex2.pokemon_type_listed()
     return pokedex2.pie_chart(df)
    
def option_b():
   print("\nGreat! Now information can be displayed in many ways! Choose your favorite! ")
   type_bar = input(" Press 'A' to see information in a list \n Press 'B' to see information in a bar chart \n Press 'C' to see information in a pie chart\nI choose option : ")
       
   if type_bar =='a':
     return pokedex2.pokemon_generation_list()
   elif type_bar == 'b':
     return pokedex2.pokemon_generation_vb()
   elif type_bar == 'c':
      return pokedex2.pokemon_generation_pie()
   


def poke_stats_viewer():
    print("\nWelcome to the Pokémon Stats Viewer section!")
    print("We have the stats from all pokemon!")

    pokemon_name = input("\nWhich pokemon stat's would you like to see?\nI want to see the stats of: ").lower()

    while True:
        print("\nNow information can be displayed in many ways! Choose your favorite! ")
        print(f"1. Show {pokemon_name.capitalize()} stats in list")
        print(f"2. Show {pokemon_name.capitalize()} stats in graphs ")
        print("3. Exit")

        option = input("Enter the number of the desired option: ")

        if option == '1':
         pokedex2.pokemon_stats_list(pokemon_name)
         break
        elif option == '2':
         pokedex2.pokemon_stats_graph(pokemon_name)
         break
        elif option == '3':
         print("Thank you for using the Pokémon Stats Viewer. Goodbye!")
         break
        else:
            print("Invalid option. Please choose again.")




#If user choose option C at the beginning for pokemon specific information, he well be calling the previous pokedex


def menu_pokedex():
 print("\nPress the letter according desired option")
 option = input(" Press 'A' for Pokemon stats \n Press 'B' for to know Pokemon Type \n Press 'C' for Pokemon abilities  \n Press 'D' for pokemon height \n Press 'E' for pokemon weight \n Press 'F' to shut down Pokedex \n Option:  ").lower()
 while True:
  if option == 'f' or option=="":
   print("See you next time!")
   break
  else: 
   pokemon = input("From which pokemon do you want this information? ")
  if option == 'a' :
    print(f"{pokemon.capitalize()} stats :")
    pokedex.pokemon_stats(pokemon_name=pokemon)
    break
  elif option == 'b' :
    print(f"The Pokemon type of {pokemon} is :")
    pokedex.pokemon_type(pokemon_name=pokemon)
    break
  elif option == 'c' :
    print(f"The abilities of {pokemon} are: ")
    pokedex.pokemon_abilities(pokemon_name=pokemon)
    break
  elif option == 'd' :
    poke_height = pokedex.pokemon_height(pokemon_name=pokemon)
    print(f"{pokemon.capitalize()} is {poke_height} meters tall")
    break
  elif option == 'e' :
    poke_weight = pokedex.pokemon_weight(pokemon_name=pokemon) 
    print(f"{pokemon.capitalize()} weights {poke_weight} kilograms")
    break
  else:
   keep_on = input("Do you have any other request? Type 'yes' or 'no \n").lower()
   if keep_on == "yes" :
    menu_pokedex()
   else: 
    print("See you next time!")
    break
   