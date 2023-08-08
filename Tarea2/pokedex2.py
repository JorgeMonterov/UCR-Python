#Pokedex2.0 
#Here is the upgrade to the previous pokedex
#New visializations with famous libraries as NumPy, Pandas and matplotlib



import requests as req
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#
#1. Pokemon by type, pokemon per generation and pokemon stats will be displayed on graphics as followed
#1.1- A function which gets all the pokemon information in json format ready for display
#1.2- Functions which create that format into a graphic either on list, pie or bar graphic. We will let user to choose as preferences.

#We will start with a function getting pokemon stats/type/generation/ in that order
#Followed by 1 function to get a list using pandas and numpy, then 1 function for pie chart and anohter for bar chart.
#This information will be send to options_for_menu file for better handling experience


#For stats

def pokemon_stats(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = req.get(url)

    if response.status_code == 200:
        data = response.json()
        stats = data["stats"]
        stats_dict = {stat["stat"]["name"]: stat["base_stat"] for stat in stats}
        return stats_dict
    else:
        return None


def pokemon_stats_list(pokemon_name):
    stats = pokemon_stats(pokemon_name)
    if stats:
        df_stats = pd.DataFrame.from_dict(stats, orient='index', columns=['Base Stat'])
        print(f"{pokemon_name.capitalize()} stats:")
        print(df_stats)
        
    else:
        print(f"Error: Could not retrieve stats for {pokemon_name.capitalize()}.")

# Function for graphics bar / pie
def pokemon_stats_graph(pokemon_name):
    stats = pokemon_stats(pokemon_name)

    if stats:
        plt.figure(figsize=(8, 6))
        plt.bar(stats.keys(), stats.values(), color=plt.cm.Paired.colors)
        plt.xlabel('Stats')
        plt.ylabel('Base Stat')
        plt.title(f"{pokemon_name.capitalize()} Stats (Bar Chart)")
        plt.xticks(rotation=45)

        # asking user if bar or pie chart
        chart_type = input("Do you want a bar chart or a pie chart? Enter 'bar' or 'pie': ").lower()

        if chart_type == 'bar':
            plt.show()
        elif chart_type == 'pie':
            plt.figure(figsize=(8, 8))
            plt.pie(list(stats.values()), labels=list(stats.keys()), autopct='%1.1f%%', colors=plt.cm.Paired.colors)
            plt.title(f"{pokemon_name.capitalize()} Stats (Pie Chart)")
            plt.show()
        else:
            print("Invalid option. No chart will be shown.")
    else:
        print(f"Error: Could not retrieve stats for {pokemon_name.capitalize()}.")



#For pokemon per type


def get_pokemon_types():
    url = "https://pokeapi.co/api/v2/type"
    response = req.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data["results"]

        types = [result["name"] for result in results]
        return types
    else:
        print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")
        return []

def get_pokemon_count_by_type(pokemon_type):
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type}"
    response = req.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_count = len(data["pokemon"])
        return pokemon_count
    else:
        print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")
        return 0

def pokemon_type_listed():
    types = get_pokemon_types()
    
    if not types:
        return
    
    # Create a dictionary to store the counts of each type
    counts = {}
    for pokemon_type in types:
        count = get_pokemon_count_by_type(pokemon_type)
        counts[pokemon_type] = count

    # Convert dictionary to pandas DataFrame
    df = pd.DataFrame.from_dict(counts, orient='index', columns=["Count"])
    return df

def pokemon_list():
    df = pokemon_type_listed()
    print(df)

def bar_chart(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df.index, df["Count"])
    plt.xlabel("Pokemon Type")
    plt.ylabel("Count")
    plt.title("Number of Pokemon by Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def pie_chart(df):
    # Filter for pokemons = 0
    df = df.query('Count > 0')

    plt.figure(figsize=(8, 8))
    sizes = df["Count"]
    labels = df.index
    percentages = df["Count"] / df["Count"].sum() * 100

    plt.pie(sizes, labels=labels, autopct=lambda p: '{:.0f} ({:.1f}%)'.format(p * sizes.sum() / 100, p),
            startangle=140)
    plt.axis("equal")
    plt.title("Number and Percentage of Pokemon by Type")
    plt.tight_layout()
    plt.show()




#Pokemon per generation 

def get_pokemon_by_generation(generation):
    url = f"https://pokeapi.co/api/v2/generation/{generation}"
    response = req.get(url)

    if response.status_code == 200:
        data = response.json()
        count = len(data["pokemon_species"])
        return count
    else:
        return 0
    


def pokemon_generation_list():
    #pokemon by generation in a list
    generations = range(1, 10)
    counts = [get_pokemon_by_generation(generation) for generation in generations]

    # Create a DataFrame for data manipulation
    df = pd.DataFrame({"Generation": generations, "Count": counts})

    # Hide the index column
    df.set_index("Generation", drop=True, inplace=True)

    print("Number of Pokémon per Generation:")
    print(df)
    
def pokemon_generation_vb():
    #pokemon by generation vertical bar
    generations = range(1, 10)
    counts = [get_pokemon_by_generation(generation) for generation in generations]

    #Created a dataframe in pandas for data manipulation
    df = pd.DataFrame({"Generation": generations, "Count": counts})
    #Grapich bar with colors showing amount per generations of pokemons
    
    plt.figure(figsize=(10, 6))
    custom_colors = ['darkred','red','orange','yellow','blue', 'green', 'purple', 'brown', 'gray']
    #added custom color to bars on graphics
    plt.bar(df["Generation"], df["Count"], color=custom_colors)
    plt.xlabel('Generation')
    plt.ylabel('Count')
    plt.title('Number of Pokémon per Generation')
    plt.xticks(generations)
    plt.show()

def pokemon_generation_pie():
    #pokemon by generation pie chart
    generations = range(1, 10)
    counts = [get_pokemon_by_generation(generation) for generation in generations]

    labels = [f"Generation {gen}" for gen in generations]

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=labels, autopct=lambda p: '{:.0f} ({:.1f}%)'.format(p * sum(counts) / 100, p),
            startangle=140)
    plt.axis("equal")
    plt.title("Number and Percentage of Pokémon per Generation")
    plt.tight_layout()
    plt.show()