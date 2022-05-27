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


needed_buildings = {
    Resource.ORE: BuildingType.MINES,
    Resource.SAND: BuildingType.CAREER,
    Resource.ORGANICS: BuildingType.FARM
}

class MyStrategy:


    def __init__(self):
        self.main_planet = None
        self.flag = False
        self.moves = []
        self.builds = []


    def update_workers(self, game: Game):
        my_workers.clear()

        for planet in game.planets:
            for worker_froup in planet.worker_groups:
                if worker_froup.player_index == 0:
                    my_workers.append((planet.id, worker_froup.number))


    def print_planet(self, game: Game):
        resource_palnets.clear()
        for planet in game.planets:
            if planet.harvestable_resource is not None:
                resource_palnets.append(planet)



    def find_nearest_planets(self, start_planet: Planet, game: Game):
        if self.main_planet:
            nearests = [float("inf"), float("inf"), float("inf")]

            for planet in resource_palnets:
                if planet.harvestable_resource in needed_res:
                    index = needed_res.index(planet.harvestable_resource)
                    if nearests[index] > manhattan(start_planet.x, start_planet.y, self.main_planet.x, self.main_planet.y):
                        nearests[index] = manhattan(start_planet.x, start_planet.y, self.main_planet.x, self.main_planet.y)
                        main_resourses_planets[planet.harvestable_resource] = planet





    def get_action(self, game: Game) -> Action:

        self.moves.clear()


        self.print_planet(game)
        if resource_palnets:
            self.main_planet = resource_palnets[0]

        self.find_nearest_planets(self.main_planet, game)
        self.update_workers(game)


        # print(self.main_planet.resources.keys())


        if self.main_planet.resources:
            if self.main_planet.resources[Resource.STONE] > 300 and self.main_planet.worker_groups[0].number > 100:
                for res, needed_planet in main_resourses_planets.items():
                    self.moves.append(MoveAction(self.main_planet.id, needed_planet.id, 100, Resource.STONE))
                    self.builds.append(BuildingAction(needed_planet.id, needed_buildings[res]))


        all_workers = []

        for workers in range(1, len(my_workers)):
            all_workers.append(my_workers[workers][1] > 200)


        if all(all_workers):
            self.builds.clear()

        print(self.builds)


        return Action(self.moves, self.builds, None)
