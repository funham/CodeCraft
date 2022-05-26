from model import *


class MyStrategy:
    def __init__(self):
        pass
    '''
    Примитивная стратегия, которая пытается застроить всю карту каменоломнями и получать очки за добычу камня.
    Смотри подсказки по ее улучшению, оформленные в виде специальных комментариев: # TODO ...
    '''
    def get_action(self, game: Game) -> Action:
        moves = []
        builds = []
        # прочитать свойства здания "каменоломня"
        quarry_properties = game.building_properties[BuildingType.QUARRY]

        # перебрать все планеты
        for planet_index, planet in enumerate(game.planets):
            # попытаться построить каменоломню, ничего не проверяя (вдруг повезет)
            # TODO стоит всё-таки проверить, выгодно ли строить на этой планете? См. поле planet.harvestable_resource
            builds.append(BuildingAction(planet_index, BuildingType.QUARRY))

            # подсчитать количество своих роботов на этой планете
            my_workers = sum(wg.number for wg in planet.worker_groups if wg.player_index == game.my_index)
            if planet.harvestable_resource == Resource.STONE:
                my_workers -= quarry_properties.max_workers             # вычесть количество занятых работой
                # TODO кстати, роботы могут быть заняты не только работой, но и строительством. См. game.max_builders

            # и всех бездельников отправить на другие планеты
            next_planet_index = (planet_index + 1) % len(game.planets)  # выбрать следующую планету
            # TODO перебирать планеты по индексу - плохая идея, лучше искать близкие и пригодные для застройки
            if my_workers > 0 and (planet.building is not None or planet.harvestable_resource != Resource.STONE):
                # отправлять группами по количеству стройматериала, необходимого для постройки следующей каменоломни
                send_count = min(my_workers, quarry_properties.build_resources[Resource.STONE])
                # TODO стоит проверить, что стройматериалы готовы к отправке и лежат на планете. См. planet.resources
                moves.append(MoveAction(planet_index, next_planet_index, send_count, Resource.STONE))
                # TODO за один ход можно отправить много групп роботов (вызывать moves.append() в цикле)

        # сформировать ответ серверу
        return Action(moves, builds, None)