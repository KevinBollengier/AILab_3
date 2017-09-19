class SearchNode:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.children = []

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_cost(self):
        return self.cost

    @staticmethod
    def return_child_node(problem, parent, action)-> 'SearchNode':
        node = SearchNode()
        node.state = problem
        node.parent = parent
        node.action = action
        return node
