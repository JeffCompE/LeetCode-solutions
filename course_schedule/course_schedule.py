class Graph:
    def __init__(self, num_of_vertex):
        self.adjacent_list = [list() for _ in range(num_of_vertex)]
        self.size = num_of_vertex

    def add_edge(self, from_, to):
        self.adjacent_list[from_].append(to)

    def is_acyclic(self):
        def search(vertex):
            marked[vertex] = True
            for v_ in self.adjacent_list[vertex]:
                if marked[v_]:
                    if not done[v_]:
                        return False
                else:
                    if not search(v_):
                        return False
            done[vertex] = True
            return True

        done = [False] * self.size
        marked = [False] * self.size
        for v in range(self.size):
            if not marked[v]:
                if not search(v):
                    return False
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = Graph(numCourses)
        for edge in prerequisites:
            graph.add_edge(edge[1], edge[0])
        return graph.is_acyclic()
