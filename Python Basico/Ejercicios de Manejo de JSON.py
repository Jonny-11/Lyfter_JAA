
import json


# Read JSON file
def read_json_file(file_name):
    with open(file_name, "r") as file:
        return json.load(file)


# Ask for Pokémon information
def pokemon_data():

    name = input("Enter the Pokémon name: ")
    pokemon_type = input("Enter the Pokémon type: ")
    level = int(input("Enter the Pokémon level: "))
    weight_kg = float(input("Enter the Pokémon weight in kg: "))

    shiny_input = input("Is the Pokémon shiny? (yes/no): ").lower()
    is_shiny = shiny_input == "yes"

    held_item = input("Enter the held item: ")

    skills = input("Enter Pokémon skills separated by commas: ").split(",")

    hp = int(input("Enter HP stat: "))
    attack = int(input("Enter Attack stat: "))
    defense = int(input("Enter Defense stat: "))

    # Remove extra spaces from skills
    skills = [skill.strip() for skill in skills]

    return {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": {
            "hp": hp,
            "attack": attack,
            "defense": defense
        }
    }


# Add Pokémon to list
def add_pokemon(pokemon_list, new_pokemon):
    pokemon_list.append(new_pokemon)


# Save JSON file
def save_json_file(file_name, pokemon_list):
    with open(file_name, "w") as file:
        json.dump(pokemon_list, file, indent=4)


# Main function
def main():

    file_name = "pokemons.json"

    pokemons = read_json_file(file_name)

    new_pokemon = pokemon_data()

    add_pokemon(pokemons, new_pokemon)

    save_json_file(file_name, pokemons)

    print("Pokémon added successfully.")


# Execute program
if __name__ == "__main__":
    main()