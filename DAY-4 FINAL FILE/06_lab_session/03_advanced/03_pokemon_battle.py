"""
Project Idea: Pokémon Simplified Battle Simulation

In this project, you will create a Pokémon battle simulation by utilizing the `pokedex.json` and `moves.json` files.

1. Pokémon Creation:
    First, create a `Pokémon` class with the following attributes:
        - name (str): The Pokémon's name (in English).
        - types (list[str]): A list of types (e.g., Water, Fire, Grass).
        - hp (int): The Pokémon's health points.
        - attack (int): The Pokémon's attack stat.
        - defense (int): The Pokémon's defense stat.
        - sp_attack (int): The Pokémon's special attack stat.
        - sp_defense (int): The Pokémon's special defense stat.
        - speed (int): The Pokémon's speed stat.

    The `Pokémon` class should also have a collection of moves based on the `moves.json`:
        - moves (list[Move]): A list of `Move` objects that the Pokémon can use.

    Additionally, create the following method for the Pokémon class:
        - use(skill, other): This method allows the Pokémon to use a move against another Pokémon. The damage calculation depends on the type of the move:
            - If the move is one of the following types: Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Steel, Ice, Dragon, or Dark, use the formula:
                - damage = ((skill.power * self.attack) / other.defense)
            - Otherwise, use the formula:
                - damage = ((skill.power * self.sp_attack) / other.sp_defense)

    After using a move, decrease its PP by 1. A move cannot be used if its PP is 0.

    Also, create a property for the Pokémon class:
        - knocked_out: This property returns `True` if the Pokémon's HP is 0 or lower, indicating that it has been knocked out.

2. Pokémon Moves:
    Create a `Move` class with the following attributes:
        - name (str): The name of the move.
        - type (str): The type of the move (e.g., Fire, Electric).
        - power (int): The move's power.
        - pp (int): The number of uses remaining for the move.

    Additionally, create the following property for the `Move` class:
        - usable: This property returns `True` if the move's PP is greater than 0.

3. Pokémon Battle:
    At the beginning of the program, prompt the player to select a Pokémon to use in battle and choose six possible moves for their Pokémon (based on type).

    Implement an infinite loop with the following steps:
        1. Create a new enemy Pokémon for the player to battle, and randomly assign its moves.
        2. Allow the player to select a move. If the PP for all moves is exhausted, immediately end their turn.
        3. The enemy Pokémon randomly selects a move to use against the player's Pokémon.
        4. End the game when either the player wins or loses.

Challenge:
    - Multiple Rounds: Can you implement a battle system with multiple rounds, where each round continues until one Pokémon is knocked out?
    - Randomization: Can you make the Pokémon and their moves randomized for each battle?
    - Damage Randomization: Can you add some randomness in the damage calculation to make the battle outcomes less predictable?

"""
