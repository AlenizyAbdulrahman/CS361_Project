class AstarSearch:

    #creat class constructor that takes two parameters: tree and heuristic 
    def __init__(self, tree, heuristic):
        self.tree       = tree
        self.heuristic  = heuristic 

    #A* search algorithm function
    #this function used constructor variables and returns two parameters : visited node & Optimal path
    def a_star_search_algorithm(self, start, Goal):
        self.Expand_nodes = []     # Expanded nodes
        self.fringe_nodes = []     # Fringe nodes
        self.cost = {start: 0}     #initial cost of paths
        self.start_heuristic = self.heuristic[start]       #getting start state heuristic
        self.fringe_nodes = [[start,self.start_heuristic]] #add start state and its heuristic to fringe node

        #find visited nodes
        while True:
            self.hn = [i[1] for i in self.fringe_nodes]     # determine h(n): for current state 
            self.min_value_hn = self.hn.index(min(self.hn)) # take the smallest node value of h(n) from fringe nodes "value"

            self.small_node_char = self.fringe_nodes[self.min_value_hn][0]  # determine character of smallest node value
            self.Expand_nodes.append(self.fringe_nodes[self.min_value_hn]) # add smallest h(n) node to expand nodes
            del self.fringe_nodes[self.min_value_hn] # delete smallest node value from fringe
            if self.Expand_nodes[-1][0] == Goal:  # break the loop if Goal state has been expanded
                break

            for self.item in self.tree[self.small_node_char]: # if goal not in expand, then go to next node that have the smallest value
                if self.item[0] in [self.closed_item[0] for self.closed_item in self.Expand_nodes]: # check whether parent node contain children node
                    continue
                self.cost.update({self.item[0]: self.cost[self.small_node_char] + self.item[1]})            # add nodes to self.cost dictionary
                self.fn_node = self.cost[self.small_node_char] + heuristic[self.item[0]] + self.item[1]     # calculate f(n) of current node
                temp = [self.item[0], self.fn_node]
                self.fringe_nodes.append(temp)                                     # store f(n) of current node in array opened

            #-------------------------------------------------------------------------------------------------------
                '''find optimal sequence'''
            trace_node = Goal                        # correct optimal tracing node, initialize as node G
            optimal_sequence = [Goal]                # optimal node sequence
            for i in range(len(self.Expand_nodes)-2, -1, -1):
                check_node = self.Expand_nodes[i][0]           # current node
                if trace_node in [children[0] for children in tree[check_node]]:
                    children_costs = [temp[1] for temp in tree[check_node]]
                    children_nodes = [temp[0] for temp in tree[check_node]]

                    '''check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence
                    change the correct optimal tracing node to current node'''
                    if self.cost[check_node] + children_costs[children_nodes.index(trace_node)] == self.cost[trace_node]:
                        optimal_sequence.append(check_node)
                        trace_node = check_node
        print(optimal_sequence)
        print(self.Expand_nodes)
        print(self.cost)


if __name__ == "__main__":
    tree = {
        'A': [ ['R1',1] ],
        'B': [ ['R1',1] ],
        'C': [ ['R1',1] ],
        'D': [ ['R1',1] ],
        'R1': [ ['R2',3], ['R3',5] ],
        'R2': [ ['R3',1], ['R4',4], ['R5',6] ],
        'R3': [ ['R2',1], ['R5',5] ],
        'R4': [ ['R6',6] ],
        'R5': [ ['R6',4] ],
        'R6': [ ['G1', 1], ['G2', 1], ['G3', 1], ['G4', 1] ],
        'G1': [ ['R6',1] ],
        'G2': [ ['R6',1] ],
        'G3': [ ['R6',1] ],
        'G4': [ ['R6',1] ]  
    }

    heuristic = {'A': 14, 'B': 14, 'C': 14, 'D': 14, 'R1': 13, 'R2': 10, 'R3': 9, 'R4': 7, 'R5': 6, 'R6': 1, 'G1': 0, 'G2': 0, 'G3': 0, 'G4': 0}
    astar= AstarSearch(tree, heuristic)
    astar.a_star_search_algorithm('A','G2')