from model import *

resource_palnets = []
my_workers = []

main_resourses_planets = {
    Resource.ORE: None,
    Resource.SAND: None,
    Resource.ORGANICS: None,
}


class MyStrategy:
    resources = (Resource.ORE, Resource.SAND, Resource.ORGANICS)

    def __init__(self):
        self.main_planet = None
        self.flag = False

    @property
    def nearest_planets(self, game: Game, current_planet: Planet) -> dict:
        res_on_planets = dict.fromkeys(MyStrategy.resources, [])

        for p in game.planets:
            if p.harvestable_resource != Resource.STONE:
                res_on_planets[p.harvestable_resource].append(p)

        for _, planet in res_on_planets:
            planet.sort(key=lambda p: MyStrategy.dist(p, current_planet))

        return res_on_planets

    def get_action(self, game: Game) -> Action:
        moves = []
        builds = []

        if resource_palnets:
            self.main_planet = resource_palnets[0]

        self.find_nearest_planets(game)

        return Action(moves, builds, None)

    def dist(p1: Planet, p2: Planet) -> int:
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)
