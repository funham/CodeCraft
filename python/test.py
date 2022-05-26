from model import *

resource_palnets = []
my_workers = []


class MyStrategy:

    def __init__(self):
        pass

    def init_values(self, game):
        resource_palnets.clear()
        my_workers.clear()

        for planet in game.planets:
            if planet.harvestable_resource is not None:
                resource_palnets.append(planet)

            for worker_group in planet.worker_groups:
                if worker_group.player_index == game.my_index:
                    my_workers.append((planet.id, worker_group.number))


    def action_generation(self, game):
        moves = []
        builds = []

        planets_workers_count = {}

        for worker in my_workers:
            for planet in resource_palnets:
                if planets_workers_count[planet.id] < 50 and planet.resources >= min(worker[1], 50):
                    moves.append(MoveAction(worker[0], planet.id, min(worker[1], 50), Resource.STONE))

        return (moves, builds)



    def get_action(self, game: Game) -> Action:

        self.init_values(game)

        moves = []
        builds = []


        return Action([], [], None)