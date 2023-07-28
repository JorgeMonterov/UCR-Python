import requests as req

#1.Create a function to return an random joke
 #2.Create a function to return a list of available joke's categories and 
 #return a joke from selected categorie
 #3Menu creation for client  better experience.



##1.Create a function to return an random joke
# def getRandom():
#     urlGet = "https://api.chucknorris.io/jokes/random"
#     getResponse = req.get(urlGet, verify=False)

#     if getResponse.status_code == 200:
#         data = getResponse.json()
#         print("El chiste es: ")
#         print(data["value"])
#     else:
#         print("Error a realizar la solicitud")

#getRandom()


#2.Create a function to return a list of available joke's categories and 
 #return a joke from selected categorie

# def getCategories():
#     urlGet = "https://api.chucknorris.io/jokes/categories"
#     getResponse = req.get(urlGet, verify=False)
    
#     if getResponse.status_code == 200:
#         categories = getResponse.json()
#         print("Available categories: ")
#         for categorie in categories:
#             print(categorie)

# # an input for client selection and make it show a joke from client selection
#         selected = input("Which categorie would you like to choose? \n")
#         urlGetJoke = f"https://api.chucknorris.io/jokes/random?category={selected}"
#         getResponseJoke = req.get(urlGetJoke, verify=False)
#         joke = getResponseJoke.json()
#         print(joke["value"])
        
#     else:
#         print("Error! Try again")

#getCategories()

#simplify coding by creating only one function/ This function will be called on main.py
#simplify coding by creating an input at the end to know if client would like to keep playing


def jokes():
    print("Welcome to the Chuck Norris Joke's site ")
    option = input("To get a Chuck Norris Joke, type 'Joke'. \nIn order to see avialable joke categories, type 'categories'. \n").lower()
   # Requesting a random joke
    if option == 'joke': 
        urlGet = "https://api.chucknorris.io/jokes/random"
        getJoke = req.get(urlGet, verify=False)
        if getJoke.status_code == 200:
            data = getJoke.json()
            print("Chuck Norris Joke:")
            print(data["value"])
         
# Handling the 'categories' option and user selection of a category
    elif option == "categories" or option =="categorie":
         urlGet = "https://api.chucknorris.io/jokes/categories"
         getCategories = req.get(urlGet, verify=False)
         if getCategories.status_code == 200:
            categories = getCategories.json()
            print("Available categories: ")
            for categorie in categories:
                print(categorie)
            selected = input("Which categorie would you like to choose? \n").lower()
            if selected not in categories:
                 # Restarting the function if the user selects an invalid category
                print("Typing error! System will restart! Please try  again!")
                return jokes()
            
            urlGetJoke = f"https://api.chucknorris.io/jokes/random?category={selected}"
            getResponseJoke = req.get(urlGetJoke, verify=False)
            joke = getResponseJoke.json()
            print(f"{selected.capitalize()} joke of Chuck Norris:")
            print(joke["value"])
            
   # Handling the user's choice to keep playing or finish the program
        
    keep_playing = input("Hope you enjoyed the joke as we did. \nIf you would like to get another Joke type 'Jokes' in order to start over, otherwise type 'done' to finish the program.\n").lower()
    if keep_playing == "joke" or keep_playing == "jokes":
        return jokes()
    else:
        print("Thank you for chosing us!")
         
#jokes()
