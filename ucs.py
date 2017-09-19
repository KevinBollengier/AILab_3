import fileinput
from queue import PriorityQueue
import AILab_3.SearchNode


def main():
    """lines = []
    for line in fileinput.input():
        lines.append(line)
    maximumHeight = lines[0]
    # initial_location = lines[1]"""
    initial_location = "(A); (B); (C)"
    goal_location = "(A, C); (B); X"
    max_height = 2
    """goalState = lines[2]"""
    pick_up = 0.5
    moveLeftRight = 1
    putDown = 0.5
    input_matrix = build_matrix(initial_location)
    goal_matrix = build_matrix(goal_location)
    # print(goal_matrix)
    compare_index(input_matrix, goal_matrix)


def calc_cost(pickup: float, start_stack: int, goal_stack: int, putdown: float)->float:
    cost = pickup + (goal_stack - start_stack) + putdown
    return cost


def build_matrix(location: str)->[]:
    columns = location.split("; ")
    containerstack = []
    for stack in columns:
        temp = stack.replace('(', '')
        temp = temp.replace(')', '')
        temp = temp.split(", ")
        containerstack.append(temp)
    return containerstack


def compare_index(input_matrix, goal_matrix):
    indexes = []
    for index, value in enumerate(input_matrix):
        search_key = value
        for idx, sublist in enumerate(goal_matrix):
            if sublist[0] == search_key:
                indexes.append(index, idx)
                # TODO: fix this so i have an index array of where to find index(input) in the goal_matrix
        print(indexes)


def ucs(search_tree, start_state: SearchNode, goal_state: SearchNode):
    visited = set()  # create set of visited nodes
    q = PriorityQueue()  # make a new PQ
    q.put((start_state.get_cost(), start_state.get_state()))  # store node state and cost

    while q:
        cost, node = q.get()
        if node not in visited:
            visited.add(node)
        if node.get_state() == goal_state:
            return
        for i in search_tree:
            if i not in visited:
                total_cost = i.get_cost() + calc_cost()  # TODO: fix calc_cost function
                q.put(total_cost, i)


if __name__ == '__main__':
    main()
