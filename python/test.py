from model import *

resource_palnets = []
my_workers = []


class MyStrategy:

    def __init__(self):
        pass


    def print_planet(self, game: Game):
        resource_palnets.clear()
        for planet in game.planets:
            if not planet.harvestable_resource is None:
                resource_palnets.append(planet.id)
                print(planet.id)


    def get_action(self, game: Game) -> Action:

        self.print_planet(game)

        return Action([], [], None)