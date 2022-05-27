from model import *

resource_palnets = []
my_workers = []

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

main_resourses_planets = {
    Resource.ORE: None,
    Resource.SAND: None,
    Resource.ORGANICS: None,
                        }



needed_res = [Resource.ORE, Resource.SAND, Resource.ORGANICS]

class MyStrategy:


    def __init__(self):
        self.main_planet = None
        self.flag = False



    def print_planet(self, game: Game):
        resource_palnets.clear()
        for planet in game.planets:
            if planet.harvestable_resource is not None:
                resource_palnets.append(planet)



    def find_nearest_planets(self, game: Game):
        if self.main_planet:
            nearests = [float("inf"), float("inf"), float("inf")]

            for planet in resource_palnets:
                if planet.harvestable_resource in needed_res:
                    index = needed_res.index(planet.harvestable_resource)
                    if nearests[index] > manhattan(planet.x, planet.y, self.main_planet.x, self.main_planet.y):
                        nearests[index] = manhattan(planet.x, planet.y, self.main_planet.x, self.main_planet.y)
                        main_resourses_planets[planet.harvestable_resource] = planet.id





    def get_action(self, game: Game) -> Action:


        moves = []
        builds = []

        self.print_planet(game)
        if resource_palnets:
            self.main_planet = resource_palnets[0]

        self.find_nearest_planets(game)


        print(main_resourses_planets)
        # if not self.flag:
        #     if self.main_planet.resources.stone > 900:
        #         for needed_planet in main_resourses_planets.values():
        #             moves.append(MoveAction(self.main_planet.id, needed_planet, 300, Resource.STONE))
        #
        #     flag = True


        return Action(moves, [], None)
