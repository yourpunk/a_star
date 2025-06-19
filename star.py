from blockworld import BlockWorld
import heapq
 
class BlockWorldHeuristic(BlockWorld):
    def __init__(self, num_blocks=5, state=None):
        BlockWorld.__init__(self, num_blocks, state)
 
    def heuristic(self, goal):
        def to_mapping(state):
            mapping = {}
            for stack in state:
                if not stack:
                    continue
                mapping[stack[0]] = "table"
                for i in range(1, len(stack)):
                    mapping[stack[i]] = stack[i - 1]
            return mapping
 
        self_map = to_mapping(self.get_state())
        goal_map = to_mapping(goal.get_state())
 
        cost = 0
        for block in self_map:
            curr = self_map[block]
            goal = goal_map.get(block)
            while curr != goal:
                cost += 1
                curr = self_map.get(curr)
                if curr is None:
                    break
        return cost
 
 
 
 
 
class AStar():
    def search(self, start, goal):
        from collections import defaultdict
        open_heap = []
        g_scores = defaultdict(lambda: float('inf'))
 
        start_state_id = tuple(sorted(start.get_state()))
        g_scores[start_state_id] = 0
        heapq.heappush(open_heap, (start.heuristic(goal), 0, start, []))
        closed = set()
 
        while open_heap:
            f, g, current, path = heapq.heappop(open_heap)
            state_id = tuple(sorted(current.get_state()))
 
            if current == goal:
                return path
 
            if state_id in closed:
                continue
            closed.add(state_id)
 
            for action, neighbor in current.get_neighbors():
                neighbor_id = tuple(sorted(neighbor.get_state()))
                tentative_g = g + 1
                if tentative_g < g_scores[neighbor_id]:
                    g_scores[neighbor_id] = tentative_g
                    f = tentative_g + neighbor.heuristic(goal)
                    heapq.heappush(open_heap, (f, tentative_g, neighbor, path + [action]))
 
        return None
 
 
    if __name__ == '__main__':
        N = 5
 
        start = BlockWorldHeuristic(N)
        goal = BlockWorldHeuristic(N)
 
        print("Searching for a path:")
        print(f"{start} -> {goal}")
        print()
 
        astar = AStar()
        path = astar.search(start, goal)
 
        if path is not None:
            print("Found a path:")
            print(path)
 
            print("\nHere's how it goes:")
 
            s = start.clone()
            print(s)
 
            for a in path:
                s.apply(a)
                print(s)
 
        else:
            print("No path exists.")
 
        print("Total expanded nodes:", BlockWorld.expanded)
