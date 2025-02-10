import time

class Router:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}

    def initialize(self, graph):
        self.routing_table = {node: (cost, node) for node, cost in graph[self.name].items()}
        self.routing_table[self.name] = (0, self.name)

    def update(self, neighbors):
        updated = False
        for neighbor, cost in neighbors.items():
            for dest, (route_cost, _) in neighbor.routing_table.items():
                new_cost = cost + route_cost
                if dest not in self.routing_table or new_cost < self.routing_table[dest][0]:
                    self.routing_table[dest] = (new_cost, neighbor.name)
                    updated = True
        return updated

    def display(self):
        print(f"\nRouter {self.name} Routing Table:")
        print("Dest\tCost\tNext Hop")
        for dest, (cost, next_hop) in sorted(self.routing_table.items()):
            print(f"{dest}\t{cost}\t{next_hop}")
        print("-" * 30)


def get_user_graph():
    graph = {}
    for _ in range(int(input("Enter number of nodes: "))):
        node = input("\nNode name: ")
        graph[node] = {nbr: int(cost) for _ in range(int(input(f"Neighbors of {node}: ")))
                       for nbr, cost in [input("Neighbor Cost: ").split()]}
    return graph


def distance_vector_routing(graph):
    routers = {name: Router(name) for name in graph}
    for router in routers.values():
        router.initialize(graph)

    print("\nInitial Routing Tables:")
    for router in routers.values():
        router.display()

    print("\nUpdating Routing Tables...\n")
    iteration = 0

    while True:
        updates = False
        for router in routers.values():
            updates |= router.update({routers[nbr]: cost for nbr, cost in graph[router.name].items()})

        iteration += 1
        print(f"\nIteration {iteration}:")
        for router in routers.values():
            router.display()

        if not updates:
            break
        time.sleep(1)

    print("Final Routing Tables Stabilized.")


if __name__ == "__main__":
    distance_vector_routing(get_user_graph())
