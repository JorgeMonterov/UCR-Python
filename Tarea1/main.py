import pokedex as pokedex 
print(f"Welcome to the Pokedex!")
print(f"What brings you here today?")

def menu():
 print("Press the letter according desired option")
 option = input(" Press 'A' for Pokemon stats \n Press 'B' for to know Pokemon Type \n Press 'C' for Pokemon abilities  \n Press 'D' for pokemon height \n Press 'E' for pokemon weight \n Press 'F' to shut down Pokedex \n Option:  ").lower()
 
 if option == 'f' :
    print("See you next time!")

 else: 
  pokemon = input("From which pokemon do you want this information? ")
  if option == 'a' :
    print(f"{pokemon.capitalize()} stats :")
    pokedex.pokemon_stats(pokemon_name=pokemon)

  elif option == 'b' :
    print(f"The Pokemon type of {pokemon} is :")
    pokedex.pokemon_type(pokemon_name=pokemon)

  elif option == 'c' :
    print(f"The abilities of {pokemon} are: ")
    pokedex.pokemon_abilities(pokemon_name=pokemon)

  elif option == 'd' :
    poke_height = pokedex.pokemon_height(pokemon_name=pokemon)
    print(f"{pokemon.capitalize()} is {poke_height} meters tall")

  elif option == 'e' :
    poke_weight = pokedex.pokemon_weight(pokemon_name=pokemon) 
    print(f"{pokemon.capitalize()} weights {poke_weight} kilograms")

  keep_on = input("Do you have any other request? Type 'yes' or 'no \n").lower()
  if keep_on == "yes" :
   menu()
  else: 
    print("See you next time!")
   
   


menu()