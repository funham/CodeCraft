from model import *

main_resourses_planets = {
    Resource.ORE: None,
    Resource.SAND: None,
    Resource.ORGANICS: None,
}

resources = (Resource.ORE, Resource.SAND, Resource.ORGANICS)


def dist(p1: Planet, p2: Planet) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


class MyStrategy:

    def __init__(self):
        self.main_planet = None
        self.flag = False

    def find_nearest_planets(self, game: Game, current_planet: Planet) -> dict:
        res_on_planets = dict.fromkeys(MyStrategy.resources, [])

        for p in game.planets:
            if p.harvestable_resource != Resource.STONE:
                res_on_planets[p.harvestable_resource].append(p)

        for _, planet in res_on_planets:
            planet.sort(key=lambda p: dist(p, current_planet))

        return res_on_planets

    def get_action(self, game: Game) -> Action:
        moves = []
        builds = []

        return Action(moves, builds, None)
