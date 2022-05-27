# стратегия с комментариями
from model import *

resource_planets = []  # все доступные нам планеты
my_workers = []
numbers = []
planets_workers_count = dict()  # сколько куда рабочих отправили
builds_done = []

types_of_buildings = {Resource.ORE: BuildingType.MINES,
                      Resource.SAND: BuildingType.CAREER,
                      Resource.ORGANICS: BuildingType.FARM}


class MyStrategy:
    def __init__(self):
        pass

    def first_time_preparation(self, game):
        global resource_planets, my_workers, planets_workers_count, builds_done, first_time_flag, types_of_buildings, taken_stone
        for planet in resource_planets:
            builds_done[planet.id] = False  # заполняем посроения false'ами
            # обнуляем количесвто рабочих в начале игры (чтобы не отправляли нескоько раз рабочих)
            planets_workers_count[planet.id] = 0

    '''
    Примитивная стратегия, которая пытается застроить всю карту каменоломнями и получать очки за добычу камня.
    Смотри подсказки по ее улучшению, оформленные в виде специальных комментариев: # TODO ...
    '''

    def init_values(self, game):
        global resource_planets, my_workers, planets_workers_count, builds_done, first_time_flag, types_of_buildings
        resource_planets.clear()
        my_workers.clear()

        taken_stone[0] = 0

        for planet in game.planets:
            # закидываем ресурс (НЕ камень)
            if planet.harvestable_resource is not None and planet.harvestable_resource is not Resource.STONE:
                resource_planets.append(planet)
                taken_stone[planet.id] = 0

            for worker_group in planet.worker_groups:
                if worker_group.player_index == game.my_index:
                    my_workers.append((planet.id, worker_group.number))

    def action_generation(self, game):
        global resource_planets, my_workers, planets_workers_count, builds_done, first_time_flag, types_of_buildings, taken_stone
        moves = []
        builds = []

        for worker in my_workers:
            for planet in resource_planets:

                # это на будущее
                # if planets_workers_count[planet.id] < 50 and planet.resources[Resource.STONE] >= min(worker[1],50):
                #     moves.append(MoveAction(worker[0], planet.id, min(worker[1],50), Resource.STONE))

                # есть ли камни там, есть ли рабочие (< 50)
                if planets_workers_count[planet.id] < 50 and Resource.STONE in game.planets[worker[0]].resources.keys():

                    if game.planets[worker[0]].resources[Resource.STONE] - taken_stone[worker[0]] >= 50 \
                            and worker[0] == 0:
                        taken_stone[worker[0]] += 50  # откуда отправляем
                        planets_workers_count[planet.id] = 50
                        moves.append(MoveAction(
                            worker[0], planet.id, 50, Resource.STONE))
                        # worker[0] - откуда, planet.id = куда

        for planet in resource_planets:
            if planet.building is not None:
                builds_done[planet.id] = True

        for planet in resource_planets:
            have_workers = False  # есть ли нужное количество рабочи там
            for worker in planet.worker_groups:
                if worker.player_index == game.my_index and worker.number >= 50:
                    have_workers = True  # есть рабочие, которых можно эксплуатировать

            if have_workers and Resource.STONE in planet.resources.keys() and planet.resources[
                    Resource.STONE] >= 50 and not builds_done[planet.id]:

                builds.append(BuildingAction(
                    planet.id, types_of_buildings[planet.harvestable_resource]))  # строим здание

        return (moves, builds)

    def get_action(self, game: Game) -> Action:
        global resource_planets, my_workers, planets_workers_count, builds_done, first_time_flag, types_of_buildings, taken_stone
        self.init_values(game)

        if not first_time_flag:
            self.first_time_preparation(game)
            first_time_flag = True

        moves, builds = self.action_generation(game)
        return Action(moves, builds, None)
