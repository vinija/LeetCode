class Node(object):
    def __init__(self):
        self.IN = set()
        self.OUT = set()

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # initialization
        allnodes, graph, res = set("".join(words)), {}, ""
        for i in allnodes:
            graph[i] = Node()

        # build the graph
        for i in range(len(words)-1):
            if words[i].find(words[i + 1]) == 0 and len(words[i]) > len(words[i + 1]): 
                return ""

            for j in zip(words[i], words[i+1]):
                if j[0] != j[1]:
                    graph[j[0]].OUT.add(j[1])
                    graph[j[1]].IN.add(j[0])
                    break

        # topo-sort
        while allnodes:
            buff = set([i for i in allnodes if graph[i].OUT and not graph[i].IN])
            if not buff:
                return res + "".join(allnodes) if not [i for i in allnodes if graph[i].IN] else "" # have solution if no connected node
            res += "".join(buff)
            allnodes -= buff
            for i in allnodes:
                graph[i].IN -= buff
        return res