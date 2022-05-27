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
    def __init__(self, game: Game):
        wg1, wg2 = [(p.worker_groups, p.id)
                    for p in game.planets if p.worker_groups]

        def set_worker_group_dict(wg) -> dict:
            wg_d = {
                'planet_id': wg[1],
                'workers_id': wg[0][0].player_index
            }

            return wg_d

        wg1, wg2 = (set_worker_group_dict(wg) for wg in (wg1, wg2))
        main_planet_id = wg1['planet_id'] if wg1['workers_id'] == game.my_index else wg2['planet_id']
        self.main_planet = game.planets[main_planet_id]
        self.flag = False

    def find_main_planet(self, game: Game) -> Planet:

        pass

    def find_nearest_planets(self, game: Game, current_planet: Planet,
                             filtered_resources: list = [Resource.STONE]) -> list:
        nearests = []

        for p in game.planets:
            if p.harvestable_resource not in filtered_resources:
                nearests.append(p)

        nearests.sort(key=lambda p: dist(p, current_planet))
        return nearests

    def find_nearest_planets_by_res(self, game: Game, current_planet: Planet) -> dict:
        res_on_planets = dict.fromkeys(MyStrategy.resources, [])

        for p in self.find_nearest_planets(game, current_planet):
            res_on_planets[p.harvestable_resource].append(p)

        return res_on_planets

    def get_action(self, game: Game) -> Action:
        moves = []
        builds = []

        return Action(moves, builds, None)
