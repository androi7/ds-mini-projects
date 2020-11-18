#!/usr/bin/env python
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 15px; height: 80px">
# 
# # Project 1
# 
# ### Building "Pokemon Stay"
# 
# ---
# You are an analyst at a "scrappy" online gaming company that specializes in remakes of last year's fads.
# 
# Your boss, who runs the product development team, is convinced that Pokemon Go's fatal flaw was that you had to actually move around outside. She has design mock-ups for a new game called Pokemon Stay: in this version players still need to move, but just from website to website. Pokemon gyms are now popular online destinations, and catching Pokemon in the "wild" simply requires browsing the internet for hours in the comfort of your home.
# 
# She wants you to program a prototype version of the game and analyze the planned content to help the team calibrate the design.

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Building-&quot;Pokemon-Stay&quot;" data-toc-modified-id="Building-&quot;Pokemon-Stay&quot;-0.1">Building "Pokemon Stay"</a></span><ul class="toc-item"><li><span><a href="#Package-imports" data-toc-modified-id="Package-imports-0.1.1">Package imports</a></span></li></ul></li></ul></li><li><span><a href="#1.-Defining-a-player" data-toc-modified-id="1.-Defining-a-player-1">1. Defining a player</a></span></li><li><span><a href="#2.-Defining-&quot;gym&quot;-locations" data-toc-modified-id="2.-Defining-&quot;gym&quot;-locations-2">2. Defining "gym" locations</a></span></li><li><span><a href="#3.-Create-a-pokedex" data-toc-modified-id="3.-Create-a-pokedex-3">3. Create a pokedex</a></span></li><li><span><a href="#4.-Create-a-data-structure-for-players" data-toc-modified-id="4.-Create-a-data-structure-for-players-4">4. Create a data structure for players</a></span><ul class="toc-item"><li><span><a href="#4.1" data-toc-modified-id="4.1-4.1">4.1</a></span></li><li><span><a href="#4.2" data-toc-modified-id="4.2-4.2">4.2</a></span></li></ul></li><li><span><a href="#5.-Add-captured-pokemon-for-each-player" data-toc-modified-id="5.-Add-captured-pokemon-for-each-player-5">5. Add captured pokemon for each player</a></span></li><li><span><a href="#6.-What-gyms-have-players-visited?" data-toc-modified-id="6.-What-gyms-have-players-visited?-6">6. What gyms have players visited?</a></span><ul class="toc-item"><li><span><a href="#6.1" data-toc-modified-id="6.1-6.1">6.1</a></span></li><li><span><a href="#6.2" data-toc-modified-id="6.2-6.2">6.2</a></span></li></ul></li><li><span><a href="#7.-Calculate-player-&quot;power&quot;." data-toc-modified-id="7.-Calculate-player-&quot;power&quot;.-7">7. Calculate player "power".</a></span></li><li><span><a href="#8.-Load-a-pokedex-file-containing-all-the-pokemon" data-toc-modified-id="8.-Load-a-pokedex-file-containing-all-the-pokemon-8">8. Load a pokedex file containing all the pokemon</a></span><ul class="toc-item"><li><span><a href="#8.1" data-toc-modified-id="8.1-8.1">8.1</a></span></li><li><span><a href="#8.2-Parse-the-raw-pokedex-with-list-comprehensions" data-toc-modified-id="8.2-Parse-the-raw-pokedex-with-list-comprehensions-8.2">8.2 Parse the raw pokedex with list comprehensions</a></span></li></ul></li><li><span><a href="#9.-Write-a-function-to-generate-the-full-pokedex" data-toc-modified-id="9.-Write-a-function-to-generate-the-full-pokedex-9">9. Write a function to generate the full pokedex</a></span></li><li><span><a href="#10.-Write-a-function-to-generate-a-&quot;filtered&quot;-pokedex" data-toc-modified-id="10.-Write-a-function-to-generate-a-&quot;filtered&quot;-pokedex-10">10. Write a function to generate a "filtered" pokedex</a></span></li><li><span><a href="#11.-Descriptive-statistics-on-the-prototype-pokedex" data-toc-modified-id="11.-Descriptive-statistics-on-the-prototype-pokedex-11">11. Descriptive statistics on the prototype pokedex</a></span><ul class="toc-item"><li><span><a href="#11.1" data-toc-modified-id="11.1-11.1">11.1</a></span></li><li><span><a href="#11.2" data-toc-modified-id="11.2-11.2">11.2</a></span></li></ul></li><li><span><a href="#12.-Calibrate-the-frequency-of-Pokemon" data-toc-modified-id="12.-Calibrate-the-frequency-of-Pokemon-12">12. Calibrate the frequency of Pokemon</a></span></li></ul></div>

# #### Package imports
# 
# The pprint package below is the only package imported here, and it's not even strictly required to do any of the project. Printing python variables and objects with pprint can help to format them in a "prettier" way.

# In[1]:


from pprint import pprint


# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 1. Defining a player
# 
# ---
# 
# The player variables are:
# 
#     player_id : id code unique to each player (integer)
#     player_name : entered name of the player (string)
#     time_played : number of times played the game in minutes (float)
#     player_pokemon: the player's captured pokemon (dictionary)
#     gyms_visited: ids of the gyms that a player has visited (list)
#     
# Create the components for a player object by defining each of these variables. The dictionary and list variables should just be defined as empty; you can use any (correctly typed) values for the others.

# In[2]:


from typing import TypedDict, List, Dict, Tuple, Any, Optional, cast, TypeVar


# In[3]:


class Player(TypedDict):
    player_id: int
    player_name: str
    time_played: float
    player_pokemon: Dict[Optional[int], Optional[List[int]]]
    gyms_visited: List[str]


# In[4]:


import uuid

id_1 = uuid.uuid1().int


# In[5]:


player_1: Player = {
    'player_id': id_1,
    'player_name': 'Ash',
    'time_played': 125.0,
    'player_pokemon': {},
    'gyms_visited': []
}


# In[6]:


player_1


# Convert jupyter notebook to python script:<br>
# `jupyter nbconvert --to script Pokemon_Stay.ipynb`
# 
# Type checking:<br>
# `mypy Pokemon_Stay.py`

# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 2. Defining "gym" locations
# 
# ---
# 
# As the sole programmer, Pokemon Stay will have to start small. To begin, there will be 10 different gym location websites on the internet. The gym locations are:
# 
#     1. 'reddit.com'
#     2. 'amazon.com'
#     3. 'twitter.com'
#     4. 'linkedin.com'
#     5. 'ebay.com'
#     6. 'netflix.com'
#     7. 'sporcle.com'
#     8. 'stackoverflow.com'
#     9. 'github.com'
#     10. 'quora.com'
# 
# 1. Set up a list of all the gym locations. This will be a list of strings.
# 2. Append two of these locations to your player's list of visited gyms.
# 3. Print the list.

# In[7]:


pokemon_gyms: List[str] = [
    'reddit.com', 
    'amazon.com', 
    'twitter.com', 
    'linkedin.com', 
    'ebay.com', 
    'netflix.com', 
    'sporcle.com', 
    'stackoverflow.com', 
    'github.com', 
    'quora.com'
]


# In[8]:


player_1['gyms_visited'].extend([pokemon_gyms[1], pokemon_gyms[5]])


# In[9]:


player_1


# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 3. Create a pokedex
# 
# ---
# 
# We also need to create some pokemon to catch. Each pokemon will be defined by these variables:
# 
#     pokemon_id : unique identifier for each pokemon (integer)
#     name : the name of the pokemon (string)
#     type : the category of pokemon (string)
#     hp : base hitpoints (integer)
#     attack : base attack (integer)
#     defense : base defense (integer)
#     special_attack : base special attack (integer)
#     special_defense : base sepecial defense (integer)
#     speed : base speed (integer)
# 
# We are only going to create 3 different pokemon with these `pokemon_id` and `pokemon_name` values:
# 
#     1 : 'charmander'
#     2 : 'squirtle'
#     3 : 'bulbasaur'
# 
# Create a dictionary that will contain the pokemon. The keys of the dictionary will be the `pokemon_id` and the values will themselves be dictionaries that contain the other pokemon variables. The structure of the pokedex dictionary will start like so:
#      
#      {
#          1: {
#                  'name':'charmander',
#                  'type':'fire',
#                  ...
#                  
# The `type` of charmander, squirtle, and bulbasaur should be `'fire'`, `'water'`, and `'poison'` respectively. The other values are up to you, make them anything you like!
# 
# Print (or pretty print) the pokedex dictionary with the 3 pokemon.

# In[10]:


class Pokemon(TypedDict):
    name: str
    type: str
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


# In[11]:


pokedex: Dict[int, Pokemon] = {
    1: {  
        'name': 'charmander',  
        'type': 'fire',  
        'hp': 239,  
        'attack': 52,  
        'defense': 43,  
        'special_attack': 79,  
        'special_defense': 72,  
        'speed': 65  
    },
    
    2: {
        'name': 'squirtle',
        'type': 'water',
        'hp': 244,
        'attack': 48,
        'defense': 65,
        'special_attack': 83,
        'special_defense': 97,
        'speed': 43
    },
    
    3: {
        'name': 'bulbasaur',
        'type': 'poison',
        'hp': 245,
        'attack': 49,
        'defense': 49,
        'special_attack': 71,
        'special_defense': 68,
        'speed': 45
    }
}


# In[12]:


pprint(pokedex)


# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 4. Create a data structure for players
# 
# ---
# 
# ### 4.1 
# 
# In order to maintain a database of multiple players, create a dictionary that keeps track of players indexed by `player_id`. 
# 
# The keys of the dictionary will be `player_id` and the values will be dictionaries containing each player's variables (from question 1). 
# 
# Construct the `players` dictionary and insert the player that you defined in question 1, then print `players`.

# In[13]:


class PlayerList(TypedDict):
    player_name: str
    time_played: float
    player_pokemon: Dict[Optional[int], Optional[List[int]]]
    gyms_visited: List[str]


# In[14]:


players: Dict[int, PlayerList] = {}


# In[15]:


# issue: type checking doesn't work with dynamic created code (dictionary comprehension), that's
# why players_dict: Dict[int, PlayerList] was changed to players_dict[int, Any] for a workaround

def add_player(players_dict: Dict[int, Any], *player: Player) -> None:
    """
    Adds one or several player(s) to a player dictionary indexed by the 'player_id'
    
    Parameters:
    players_dict (dict): player dictionary container where to add player object(s)
    player (dict): one or multiple player dictionaries which should be added to 'players_dict' container
    """
    players_dict.update({p['player_id']: {k: v for k, v in p.items() if k != 'player_id'} for p in player})


# In[16]:


# optional way when fulfulling strict TpyedDict requirements

# def add_player(players_dict: Dict[int, PlayerList], *player: Player) -> Dict[int, PlayerList]:
#     """
#     Adds one or several player(s) to a player dictionary indexed by the 'player_id'
    
#     Parameters:
#     players_dict (dict): player dictionary container where to add player object(s)
#     player (dict): one or multiple player dictionaries which should be added to 'players_dict' container
#     """
#     return {
#         **players_dict,
#         **{
#             p["player_id"]: PlayerList(
#                 player_name=p["player_name"],
#                 time_played=p["time_played"],
#                 player_pokemon=p["player_pokemon"],
#                 gyms_visited=p["gyms_visited"],
#             ) 
#             for p in player
#         },
#     }


# In[17]:


add_player(players, player_1)


# In[18]:


pprint(players)  # containing every player, indexed by their player_id


# ---
# 
# ### 4.2
# 
# Create a new player with `player_id = 2` in the `players` dictionary. Leave the `'player_pokemon'` dictionary empty. Append `'stackoverflow'` and `'github.com'` to the `'gyms_visited'` list for player 2.
# 
# The `'player_name'` and `'time_played'` values are up to you, but must be a string and float, respectively.
# 
# Remember, the player_id is the key for the player in the players dictionary.
# 
# Print the `players` dictionary with the new player inserted.

# In[19]:


player_2: Player = {
    'player_id': 2,  # uuid.uuid1().int
    'player_name': 'Misty',
    'time_played': 84.0,
    'player_pokemon': {},
    'gyms_visited': []
}


# In[20]:


location_stackoverflow = pokemon_gyms[pokemon_gyms.index('stackoverflow.com')]  
location_github = pokemon_gyms[pokemon_gyms.index('github.com')]

player_2['gyms_visited'].extend([location_stackoverflow, location_github])


# In[21]:


player_2


# In[22]:


add_player(players, player_2)


# In[23]:


pprint(players)


# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 5. Add captured pokemon for each player
# 
# ---
# 
# The `'player_pokemon'` keyed dictionaries for each player keep track of which of the pokemon each player has.
# 
# The keys of the `'player_pokemon'` dictionaries are the pokemon ids that correspond to the ids in the `pokedex` dictionary you created earlier. The values are integers specifying the stats for the pokemon.
# 
# Give player 1 a squirtle. Give player 2 a charmander and a bulbasaur.
# 
# Print the players dictionary after adding the pokemon for each player.
# 

# In[24]:


def find_pokemon(pokemons_dict: Dict[int, Pokemon], pokemon_name: str) -> Tuple[Optional[int], Optional[Pokemon]]:
    """
    Finds a pokemon by its name in the pokemon_dict container and 
    returns a tuple with its index and its dictionary
    
    Parameters:
    pokemons_dict (dict): a dictionary with all pokemons
                                    
    pokemon_name (string): pokemon name
    
    Returns:
    pokemon_index (int): pokemon index which is stated in pokemon_dict
    pokemons_dict[pokemon_index] (dict): pokemon dictionary which is saved in the pokemon_dict container
    """
    for pokemon_index in pokemons_dict:
        if pokedex[pokemon_index]['name'] == pokemon_name:
            return pokemon_index, pokemons_dict[pokemon_index]
    return None, None


# In[25]:


def get_pokemon_stats(pokemon: Pokemon) -> List[int]:
    """
    Returns a list of all integer pokemon stats
    
    Parameters: 
    pokemon_dict (dict): pokemon dictionary
    
    Returns:
    pokemon_dict[prop] (list): a list with all integer stats values of 
                               that pokemon ([hp, attack, defense, special_attack, special_defense, speed])
    """
    return [pokemon['hp'], 
            pokemon['attack'], 
            pokemon['defense'],
            pokemon['special_attack'],
            pokemon['special_defense'], 
            pokemon['speed']]


# In[26]:


def add_pokemon_to_player(player: Player, pokemons_dict: Dict[int, Pokemon], pokemon_name: str) -> None:
    """
    Adds a pokemon with its stats from a pokemon container to a player
    
    Parameters:
    player (dict): player dictionary
    pokemons_dict (dict): pokemons dictionary with all pokemons, 
                          should include following keys: 'hp', 'attack', 'defense', 'special_attack',
                                                         'special_defense', 'speed'
                                                                                     
    pokemon_name (string): pokemon name which is located inside the 'pokemons_dict'
    """
    pokemon_tuple = find_pokemon(pokemons_dict, pokemon_name)
    assert pokemon_tuple[0] is not None and pokemon_tuple[1] is not None, "Pokemon not found!"
    player['player_pokemon'][pokemon_tuple[0]] = get_pokemon_stats(pokemon_tuple[1])


# In[27]:


add_pokemon_to_player(player_1, pokedex, 'squirtle')
player_1


# In[28]:


add_pokemon_to_player(player_2, pokedex, 'charmander')
add_pokemon_to_player(player_2, pokedex, 'bulbasaur')
pprint(player_2)


# In[29]:


pprint(players)


# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ### 6.1
# 
# Write a for-loop that:
# 
# 1. Iterates through the `pokemon_gyms` list of gym locations you defined before.
# 2. For each gym, iterate through each player in the `players` dictionary with a second, internal for-loop.
# 3. If the player has visited the gym, print out "[player] has visited [gym location].", filling in [player] and [gym location] with the current player's name and current gym location.

# In[30]:


counter = 0
for gym in pokemon_gyms:
    for player in players:
        #counter += 1
        if gym in players[player]['gyms_visited']:
            print("{p} has visited {g}.".format(p=players[player]['player_name'].title(), g=gym))
#print(counter)


# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ### 6.2
# 
# How many times did that loop run? If you have N gyms and also N players, how many times would it run as a function of N?
# 
# Can you think of a more efficient way to accomplish the same thing? 
# 
# (You can write your answer as Markdown text.)

# $loops=N_{p}*N_{g}=2*10=20$ 
# <br>
# $O(N_{p}*N_{g})$

# In[31]:


counter = 0
for player in players:
    for gym in players[player]['gyms_visited']:
        counter += 1
        if gym in pokemon_gyms:
            pass
print(counter)


# Looping over players and then over the visited gyms of each player. Shorter as long as player hasn't visited each gym.
# <br>
# $loops=N_{p}*N_{gp}=2*2=4$
# <br>
# But the in-operator is a loop function itself.

# Alternative way:

# In[32]:


for v in players.values():
    name = v['player_name']
    gyms = v['gyms_visited']
    print("{p} has visited {g1} and {g2}.".format(p=name,
                                                 g1=', '.join(gyms[:-1]),
                                                 g2=gyms[-1]))


# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 7. Calculate player "power".
# 
# ---
# 
# Define a function that will calculate a player's "power". Player power is defined as the sum of the base statistics of all their pokemon.
# 
# Your function will:
# 
# 1. Accept the `players` dictionary, `pokedex` dictionary, and a player_id as arguments.
# 2. For the specified player_id, look up that player's pokemon and their level(s).
# 3. Find and aggregate the attack and defense values for each of the player's pokemon from the `pokedex` dictionary.
# 4. Print "[player name]'s power is [player power].", where the player power is the sum of the base statistics for all of their pokemon.
# 5. Return the player's power value.
# 
# Print out the pokemon power for each of your players.

# In[33]:


def get_player_power(players_dict: Dict[int, PlayerList], pokemons_dict: Dict[int, Pokemon], player_id: int) -> int:
    """
    Returns and prints the total power of player. 
    The player total power is defined as the sum of the base
    statistics of all their pokemon.
    
    Parameters:
    players_dict (dict): player container with each player
    pokemons_dict (dict): pokemon container with every pokemon
    player_id (int): player id within 'players_dict'
    
    Returns:
    power (int): sum of the base statistics of all its pokemons
    """
    power = 0
    pokemons = players_dict[player_id]['player_pokemon']
    for pokemon_id in pokemons:
        assert pokemons[pokemon_id] is not None
        poke_power = cast(Any, pokemons[pokemon_id])
        power += sum(poke_power)
        # without hp and speed:
        # (first idx: hp, last idx: speed)
        # power += sum(pokemons[pokemon_id][1:-1])  
    print(f"{players_dict[player_id]['player_name'].title()}'s power is {power}.")
    return power


# In[34]:


player_1_id = player_1['player_id']
player_1_pokemon_power = get_player_power(players, pokedex, player_1_id)


# In[35]:


player_2_pokemon_power = get_player_power(players, pokedex, 2)


# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 8. Load a pokedex file containing all the pokemon
# 
# ---
# 
# ### 8.1
# 
# While you were putting together the prototype code, your colleagues were preparing a dataset of Pokemon and their attributes. (This was a rush job, so they may have picked some crazy values for some...)
# 
# The code below loads information from a comma separated value (csv) file. You need to parse this string into a more useable format. The format of the string is:
# 
# - Rows are separated by newline characters: \n
# - Columns are separated by commas: ,
# - All cells in the csv are double quoted. Ex: "PokedexNumber" is the first cell of the first row.
# 
# 
# Using for-loops, create a list of lists where each list within the overall list is a row of the csv/matrix, and each element in that list is a cell in that row. Additional criteria:
# 
# 1. Quotes are removed from each cell item.
# 2. Numeric column values are converted to floats.
# 3. There are some cells that are empty and have no information. For these cells put a -1 value in place.
# 
# Your end result is effectively a matrix. Each list in the outer list is a row, and the *j*th elements of the list together form the *j*th column, which represents a data attribute. The first three lists in your pokedex list should look like this:
# 
#     ['PokedexNumber', 'Name', 'Type', 'Total', 'HP', 'Attack', 'Defense', 'SpecialAttack', 'SpecialDefense', 'Speed']
#     [1.0, 'Bulbasaur', 'GrassPoison', 318.0, 45.0, 49.0, 49.0, 65.0, 65.0, 45.0]
#     [2.0, 'Ivysaur', 'GrassPoison', 405.0, 60.0, 62.0, 63.0, 80.0, 80.0, 60.0]

# In[36]:


from typing import Generic, Union, Sequence


# In[37]:


# Code to read in pokedex info
raw_pd: str = ''
pokedex_file = 'pokedex_basic.csv'

#pd_list: List[List[Union[str, float, int]]] = []
pd_list: List[List[Union[str, int, float]]] = [] # List[Union[List[str], List[Union[str, float, int]]]]
import csv
import string

with open(pokedex_file, newline='') as f:
    f_reader: Any = csv.DictReader(f, delimiter=',')
    pd_list.append(f_reader.fieldnames)
    for row in f_reader:
        inner_list: List[Union[str, float, int]] = []
        for val in row.values():
            cell_value: Union[str, float, int] = -1
            if val[0] in string.ascii_letters:
                cell_value = str(val)
            elif val.isnumeric():
                cell_value = float(val)
            inner_list.append(cell_value)
        pd_list.append(inner_list)


# In[38]:


pprint(pd_list)


# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ### 8.2 Parse the raw pokedex with list comprehensions
# 
# ---
# 
# Perform the same parsing as above, but **using only a single list comprehension** instead of for loops. You may have nested list comprehensions within the main list comprehension! The output should be exactly the same.

# In[39]:


# Code to read in pokedex info
raw_pd = ''
pokedex_file = 'pokedex_basic.csv'
with open(pokedex_file, 'r') as f:
    raw_pd = f.read()
    
# the pokedex string is assigned to the raw_pd variable


# In[40]:


pprint(raw_pd)


# In[41]:


pd_list2: List[List[object]] =     [[float(cell_check) if cell_check.isnumeric() 
      else cell_check if len(cell_check) > 1 and cell_check[0] in string.ascii_letters 
      else -1 for cell_check in 
      [cell.replace("\"", "") for cell in 
       [row for row in list_split.split(',')]]] for list_split in raw_pd.split('\n')]

pd_list2


# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 9. Write a function to generate the full pokedex
# 
# ---
# 
# Write a function that recreates the pokedex you made before, but with the data read in from the full pokemon file. Create a unique key value for each entry in the pokemon dictionary.
# 
# Your function should:
# 
# 1. Take the parsed pokedex information you created above as an argument.
# 2. Return a dictionary in the same format as your original pokedex you created before containing the information from the parsed full pokedex file.
# 
# To test the function, print out the pokemon with id = 100.

# In[42]:


def create_pokedex_dict(pokedex_data: List[List[Union[str, int, float]]]) -> Dict[int, Dict[str, Union[str, float, int]]]:
    """
    Creates a pokemon index 
    
    Parameters:
    pokedex_data (list): a list of pokemons where the first row is the header 
                         with the key values for the pokemon index
                         
    Returns:
    (dict): pokemon index where the keys are the pokemon id's
    """
    return {int(inner_poke_list[0]): {str(pokedex_data[0][i]): inner_poke_list[i] if i != 0 else int(inner_poke_list[i])
                               for i in range(1, len(inner_poke_list))}  
             for poke_ind, inner_poke_list in enumerate(pokedex_data) if poke_ind > 0}  # if 0.0 convert to 0


poke_index: Dict[int, Dict[str, Union[str, float, int]]] = create_pokedex_dict(pd_list)


# In[43]:


pprint(poke_index)


# In[44]:


pprint(poke_index[100])


# <img src="http://i.imgur.com/GCAf1UX.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 10. Write a function to generate a "filtered" pokedex
# ---
# Your function should:
# 1. Take the parsed pokedex information you created above as an argument.
# 1. Take a dictionary as a parameter with keys matching the features of the Pokedex, filtering by exact match for string type values, and/or filter continuous variables specified by a value that is greater than or equal to the value of the corresponding dictionary key parameter.
# 1. Return multiple elements from the Pokedex
# 
# Example:
# 
# ```python
# 
# # Only filter based on parameters passed
# filter_options = {
#     'Attack':   25,
#     'Defense':  30,
#     'Type':     'Electric'
# }
# 
# # Return records with attack >= 25, defense >= 30, and type == "Electric"
# # Also anticipate that other paramters can also be passed such as "SpecialAttack", "Speed", etc.
# filtered_pokedex(pokedex_data, filter=filter_options)
# 
# # Example output:
# # [{'Attack': 30.0,
# #  'Defense': 50.0,
# #  'HP': 40.0,
# #  'Name': 'Voltorb',
# #  'SpecialAttack': 55.0,
# #  'SpecialDefense': 55.0,
# #  'Speed': 100.0,
# #  'Total': 330.0,
# #  'Type': 'Electric'},
# #  {'Attack': 30.0,
# #  'Defense': 33.0,
# #  'HP': 32.0,
# #  'Name': 'Pikachu',
# #  'SpecialAttack': 55.0,
# #  'SpecialDefense': 55.0,
# #  'Speed': 100.0,
# #  'Total': 330.0,
# #  'Type': 'Electric'},
# #  ... etc
# #  ]
# 
# ```
# 
# 

# In[45]:


def filtered_pokedex(pokedex_data: Dict[int, Dict[str, Union[str, float, int]]], filter_pokedex_data: Dict[str, Union[str, int]]) -> List[Dict[str, Union[str, float, int]]]:
    """Returns filtered pokemons based on the filter option.
    Only pokemons are returned which have higher stats (floats) than in the filter
    dictionary and have the same values for strings.
    
    Parameters:
    pokedex_data (dict): pokemon index 
    filter_pokedex_data (dict): dictionary with filter key/value-pairs 
    
    Returns:
    pokemon_list (list): a list of all pokemons (dictionaries)
    """
    pokemon_list = []
    for pokemon_index in pokedex_data:
        pokemon: Dict[str, Union[str, float, int]] = pokedex_data[pokemon_index]
        check_stats = True
        for pokemon_filtered_stat in filter_pokedex_data:
            pok_stat = pokemon[pokemon_filtered_stat]
            fil_stat = filter_pokedex_data[pokemon_filtered_stat]
            if type(pok_stat) in (float, int):
                # print(pokemon_filtered_stat, pok_stat, fil_stat])
                if isinstance(pok_stat, (float, int)) and isinstance(fil_stat, (float, int)):  # used for type checking
                    if pok_stat < fil_stat:
                        check_stats = False
            elif type(pok_stat) == str:
                if pok_stat != fil_stat:
                    # print(pok_stat, fil_stat)
                    check_stats = False
            else:
                check_stats = False
        if check_stats:
            pokemon_list.append(pokemon)
                
    return pokemon_list 


# In[46]:


filtered_pokedex(poke_index, filter_pokedex_data={
    'Attack':   85,
    'Defense':  75,
    'Type':     'Poison',
    'Speed': 30
})


# 
# ## 11. Descriptive statistics on the prototype pokedex
# 
# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ### 11.1
# 
# What is the population mean and standard deviation of the "Total" attribute for all characters in the Pokedex?
# 
# 

# In[47]:


import numpy as np  # type: ignore

pokemon_mean = np.mean([poke_index[poke_idx]['Total'] for poke_idx in poke_index])


# In[48]:


print(round(pokemon_mean, 2))


# In[49]:


# for sample std: N-1
# therefore use option: ddof=1

pokemon_std = np.std([poke_index[poke_idx]['Total'] for poke_idx in poke_index])


# In[50]:


print(round(pokemon_std, 2))


# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ### 11.2
# 
# The game is no fun if the characters are wildly unbalanced! Are any characters "overpowered", which we'll define as having a "Total" more than three standard deviations from the population mean?

# In[51]:


overpowered_pokemons = [poke_index[poke_idx] for poke_idx in poke_index if poke_index[poke_idx]['Total'] > (pokemon_mean + 3*pokemon_std)]


# In[52]:


overpowered_pokemons


# In[53]:


pokemon_total_max = max([poke_index[poke_idx]['Total'] for poke_idx in poke_index])


# In[54]:


pokemon_total_max


# In[55]:


overpowered_criteria = pokemon_mean + 3*pokemon_std


# In[56]:


print(round(overpowered_criteria, 2))


# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 12. Calibrate the frequency of Pokemon
# 
# The design team wants you to make the powerful Pokemon rare, and the weaklings more common. How would you set the probability $p_i$ of finding Pokemon *i* each time a player visits a gym?
# 
# Write a function that takes in a Pokedex number and returns a value $p_i$ for that character.
# 
# Hint: there are many ways you could do this. What do _you_ think makes sense? Start with simplifying assumptions: for example, you could assume that the probabilities of encountering any two Pokemon on one visit to a gym are independent of each other.

# In[57]:


import matplotlib.pyplot as plt  # type: ignore
#%config InlineBackend.figure_format = 'retina'  
#%matplotlib inline  # type: ignore

population: List[Tuple[int, Union[str, float, int]]] = [(poke_idx, poke_index[poke_idx]['Total']) for poke_idx in poke_index]

def sort_func(e: Tuple[int, Union[str, float, int]]) -> float:
    '''Sort function to sort a tuple by second value'''
    assert isinstance(e[1], float)
    return e[1]
    
population.sort(key=sort_func)

plt.figure(figsize=(8,6))
plt.scatter(y=[total[1] for total in population], 
            x=[i for i in range(len(population))], 
            lw=1)
plt.title('Sorted pokemon total powers')
plt.xlabel('Continuously labelled pokemons')
plt.ylabel('Pokemon total power')
plt.show()


# In[58]:


def pokemon_probability(pokemons_dict: Dict[int, Dict[str, Union[str, float, int]]], pokemon_idx: int) -> Union[Tuple[()], Tuple[int, float]]:
    """Creating a probability of finding a pokemon based on its total stat.
    The higher the total stat the lower is its probility to find it and
    vice versa.
    
    Parameters:
    pokemons_dict (dict): pokemon index dictionary
    pokemon_index (int): pokemon index for the specific pokemon you want to get the probability
    
    Returns:
    pokemon (tuple): a tuple with the pokemon index value and the probability to find it
    """
    population = [(poke_idx, poke_index[poke_idx]['Total']) for poke_idx in pokemons_dict]
    
    assert all(isinstance(pok_tot, float) for pok_tot in dict(population).values())
    casted_population = cast(List[Tuple[int, float]], population)
    new_pokemon_index = [(total[0], 1/total[1]) for total in casted_population]
    new_pokemon_index_sum = sum([total[1] for total in new_pokemon_index])

    pokemon_probs = [(total[0], total[1]/new_pokemon_index_sum) for total in new_pokemon_index]
    # for testing: sum has to be closely to 1 (floating point calculation deviations)
    # print(sum([i[1] for i in pokemon_probs]))
    
    pokemon: Union[Tuple[()], Tuple[int, float]] = ()
    for i in pokemon_probs:
        if i[0] == pokemon_idx:
            pokemon = i
    return pokemon


# In[59]:


# Testing probabilities of a few pokemons based on their total stat

pokemon382 = pokemon_probability(poke_index, 382)
print(pokemon382)
print(poke_index[382]['Total'])
print('----------')
pokemon91 = pokemon_probability(poke_index, 91)
print(pokemon91)
print(poke_index[91]['Total'])
print('----------')
pokemon75 = pokemon_probability(poke_index, 75)
print(pokemon75)
print(poke_index[75]['Total'])
print('----------')
pokemon1 = pokemon_probability(poke_index, 1)
print(pokemon1)
print(poke_index[1]['Total'])


# In[60]:


# Check if the sum of the probabilites of each pokemon is 1

np.isclose(1, sum([prob[1] for prob in [pokemon_probability(poke_index, idx) for idx in poke_index.keys()]]))  # type: ignore


# In[ ]:




