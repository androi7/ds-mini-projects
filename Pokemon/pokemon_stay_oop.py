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


from typing import List, Dict, Sequence, Optional, Union, TypedDict, Any


# In[3]:


class Pokemon:
    def __init__(self, pokemon_id: int, name: str, pokemon_type: str, 
                 hp: int, attack: int, defense: int, special_attack: int, 
                 special_defense: int, speed: int) -> None:
        self.pokemon_id = pokemon_id
        self.name = name
        self.pokemon_type = pokemon_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        
    def __repr__(self):
        return """
        ID:              {pokemon_id}
        Name:            {name}
        Name of type:    {type_name}
        Hp:              {hp}
        Attack:          {attack}
        Defense:         {defense}
        Special attack:  {special_attack}
        Special defense: {special_defense}
        Speed:           {speed}\n""".format(pokemon_id=self.pokemon_id, 
                                             name=self.name, 
                                             type_name=self.pokemon_type, 
                                             hp=self.hp, 
                                             attack=self.attack,
                                             defense=self.defense, 
                                             special_attack=self.special_attack, 
                                             special_defense=self.special_defense, 
                                             speed=self.speed)
        
        


# In[4]:


class PokemonStats(TypedDict):
    name: str
    pokemon_type: str
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


# In[5]:


class Player:
    pokemon_list: List[Pokemon] = []
    def __init__(self, player_id: int, player_name: str, 
                 time_played: float, player_pokemon: Optional[List[Pokemon]] = None, 
                 gyms_visited: Optional[List[str]] = None) -> None:
        self.player_id = player_id
        self.player_name = player_name
        self.time_played = time_played
        self.player_pokemon = player_pokemon or []
        self.gyms_visited = gyms_visited or []
        
        
    def add_gym(self, *gyms: str) -> None:
        for gym in gyms:
            self.gyms_visited.append(gym)

            
    def add_pokemon(self, *pokemon: Pokemon) -> None:
        for pok in pokemon:
            if pok not in self.pokemon_list:
                self.player_pokemon.append(pok)
                self.pokemon_list.append(pok)
            else:
                print(f"{pok.name} is already been used.")
        
        
    def get_pokemons(self) -> Dict[int, Any]: #PokemonStats]:
        return {k.pokemon_id: {prop: getattr(k, prop) for prop in k.__dict__.keys() 
                               if prop != 'pokemon_id'} 
                for k in self.player_pokemon}
    
    
    def _get_pokemon_names(self) -> List[str]:
        return [pok.name for pok in self.player_pokemon]
    
        
    def _get_gyms(self) -> List[str]:
        return [gym for gym in self.gyms_visited]

            
    def __repr__(self):
        return """
        Player ID:    {id}
        Player name:  {name}
        Time played:  {time}
        Pokemon list: [{pokemons}]
        Gyms visited: [{gyms}]""".format(id=self.player_id, 
                                         name=self.player_name, 
                                         time=self.time_played, 
                                         pokemons=", ".join(self._get_pokemon_names()),  
                                         gyms=", ".join(self._get_gyms()))
    


# In[6]:


player_1 = Player(1, 'Ash', 125.0)
player_1


# In[7]:


list_of_players = [player_1]
list_of_players


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

# In[8]:


locations: List[str] = ['reddit.com', 
                        'amazon.com', 
                        'twitter.com', 
                        'linkedin.com', 
                        'ebay.com', 
                        'netflix.com', 
                        'sporcle.com', 
                        'stackoverflow.com', 
                        'github.com', 
                        'quora.com']


# In[9]:


locations


# In[10]:


player_1.add_gym(locations[1], locations[4])
player_1.gyms_visited


# In[11]:


print(player_1)


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

# In[12]:


charmander = Pokemon(1, 'charmander', 'fire', 239, 52, 43, 81, 94, 65)
squirtle = Pokemon(2, 'squirtle', 'water', 244, 48, 65, 72, 76, 43)
bulbasaur = Pokemon(3, 'bulbasaur', 'poison', 245, 49, 49, 78, 55, 45)

pokedex: List[Pokemon] = [charmander, squirtle, bulbasaur]


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


class PlayerDescription(TypedDict):
    player_name: str
    time_played: float
    player_pokemon: List[Pokemon]
    gyms_visited: List[str]


# In[14]:


class PlayerList:
    def __init__(self, players: List[Player]) -> None:
        self.players = players
        self._player_dict: Dict[int, Any] = {} #PlayerDescription] = {}
        
        
    def get_players(self) -> Dict[int, Any]: #PlayerDescription]:
        self._player_dict =  {k.player_id: {attrs: value for attrs, value in k.__dict__.items() 
                                            if attrs != 'player_id'} 
                             for k in self.players}
        return self._player_dict
    
    
    def _get_player_names(self) -> List[str]:
        names: List[str] = []
        for player in self.players:
            names.append(player.player_name)
        return names
    
    
    def add_player(self, *player: Player) -> Dict[int, Any]: #PlayerDescription]:
        for p in player:
            if p.player_name not in self._get_player_names():
                self.players.append(p)
        return self.get_players()
    
    
    def find_player(self, player_id: int) -> Optional[Player]:
        for player in self.players:
            if player.player_id == player_id:
                return player
        else:
            print('Player not found!')
            return None
    
    
    def calculate_power(self, player_id: int) -> int:
        player = self.find_player(player_id)
        power = 0
        if player:
            for pokemon in player.player_pokemon:
                power += sum([value for attrs, value in pokemon.__dict__.items() 
                              if attrs in ['hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed']])
        return power
    
        
    def __repr__(self):
        return ", ".join([player.player_name for player in self.players])


# In[15]:


players = PlayerList(list_of_players)


# In[16]:


players.get_players()


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

# In[17]:


player_2 = Player(2, 'Misty', 84.0, gyms_visited=['stackoverflow', 'github.com'])
player_2


# In[18]:


players.add_player(player_2)


# In[19]:


players.get_players()


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

# In[20]:


player_1.add_pokemon(squirtle)
player_2.add_pokemon(charmander, bulbasaur)


# In[21]:


player_1.add_pokemon(charmander)


# In[22]:


player_1


# In[23]:


players.get_players()


# In[24]:


players


# ## 6. What gyms have players visited?
# 
# ---

# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ### 6.1
# 
# Write a for-loop that:
# 
# 1. Iterates through the `pokemon_gyms` list of gym locations you defined before.
# 2. For each gym, iterate through each player in the `players` dictionary with a second, internal for-loop.
# 3. If the player has visited the gym, print out "[player] has visited [gym location].", filling in [player] and [gym location] with the current player's name and current gym location.

# In[25]:


for gym in locations:
    for player in players.players:
        if gym in player.gyms_visited:
            print(f"{player.player_name.title()} has visited {gym}.")


# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ### 6.2
# 
# How many times did that loop run? If you have N gyms and also N players, how many times would it run as a function of N?
# 
# Can you think of a more efficient way to accomplish the same thing? 
# 
# (You can write your answer as Markdown text.)

# In[26]:


for player in players.players:
    print(f"{player.player_name.title()} has visited {', '.join(player.gyms_visited)}.")


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

# In[27]:


# see PlayerList -> calculate_power()
players.calculate_power(1)


# In[28]:


players.calculate_power(2)


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

# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ### 8.2 Parse the raw pokedex with list comprehensions
# 
# ---
# 
# Perform the same parsing as above, but **using only a single list comprehension** instead of for loops. You may have nested list comprehensions within the main list comprehension! The output should be exactly the same.

# In[29]:


import csv

# Code to read in pokedex info
raw_pd: Optional[List[List[object]]]  = None
pokedex_file = 'pokedex_basic.csv'
with open(pokedex_file, 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)
    raw_pd = [[int(i) if i.isnumeric() 
               else -1 if i == '' 
               else i for i in row] 
              for row in rows]

raw_pd

    
# the pokedex string is assigned to the raw_pd variable


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

# In[30]:


class PokemonExtended(Pokemon):
    def __init__(self, pokemon_id: int, name: str, pokemon_type: str, total: int,
                 hp: int, attack: int, defense: int, special_attack: int, 
                 special_defense: int, speed: int) -> None:
        super().__init__(pokemon_id, name, pokemon_type, hp, attack, defense, 
                         special_attack, special_defense, speed)
        self.total = total


# In[31]:


class PokemonList:
    
    pokedex: List[PokemonExtended] = []
    
    def __init__(self, pokemon_file: List[List[object]] = None) -> None:
        self.pokemon_file = pokemon_file or []
        if self.pokemon_file:
            self._create_pokedex()
        
    def _create_pokedex(self) -> None:
        if self.pokemon_file:
            try: 
                for row in self.pokemon_file:
                    self.pokedex.append(PokemonExtended(*row))  # type: ignore
            except:
                raise ValueError("Pokemon couldn't be add to the pokedex.")
    
    def add_to_pokedex(self, *pokemon: PokemonExtended) -> None:
        for pok in pokemon:
            assert isinstance(pok, PokemonExtended), f"{pok} is not a pokemon!"
            if id(pok) not in [id(pok_in_index) for pok_in_index in self.pokedex]: 
                self.pokedex.append(pok)
            
    def get_pokedex(self) -> Optional[Dict[int, Any]]:
        if self.pokedex:
            return {pok.pokemon_id: {attrs: value for attrs, value in pok.__dict__.items()}
                    for pok in self.pokedex}
        else:
            return None
        
    def search_pokemon(self, pokemon_id: int) -> Optional[PokemonExtended]:
        for pokemon in self.pokedex:
            if pokemon.pokemon_id == pokemon_id:
                return pokemon
        else:
            return None


# In[32]:


tuple([1, 2])


# In[33]:


new_pokedex = PokemonList(raw_pd[1:])
new_pokedex.pokedex[2]


# In[34]:


# for testing purposes
new_pokedex.get_pokedex()[100]  # type: ignore


# In[35]:


pokemon_id_100 = new_pokedex.search_pokemon(100)
pokemon_id_100


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

# In[ ]:





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

# In[ ]:





# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ### 11.2
# 
# The game is no fun if the characters are wildly unbalanced! Are any characters "overpowered", which we'll define as having a "Total" more than three standard deviations from the population mean?

# In[ ]:





# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# 
# ## 12. Calibrate the frequency of Pokemon
# 
# The design team wants you to make the powerful Pokemon rare, and the weaklings more common. How would you set the probability $p_i$ of finding Pokemon *i* each time a player visits a gym?
# 
# Write a function that takes in a Pokedex number and returns a value $p_i$ for that character.
# 
# Hint: there are many ways you could do this. What do _you_ think makes sense? Start with simplifying assumptions: for example, you could assume that the probabilities of encountering any two Pokemon on one visit to a gym are independent of each other.

# In[ ]:




