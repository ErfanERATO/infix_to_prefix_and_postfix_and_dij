# def => یک کیوورد برای تعریف فانکشن


def create_graph():
    # مشخص کردن مسیر های موجود
    dictionary = {'A': {'B': 2, 'C': 5},
                  'B': {'C': 8, 'D': 7},
                  'C': {'E': 4, 'D': 2},
                  'D': {'F': 1},
                  'E': {'F': 3, 'D': 6},
                  'F': {'F': 0}
                  }

    return dictionary


graph = create_graph()

print("The single source non negative weighted direct graph \n {} \n".format(graph))

source_node = input(
    "Input the sourse node from below list \n {} - ".format(graph.keys()))
while(source_node not in graph.keys()):
    source_node = input(
        "Input the sourse node from below list \n {} - ".format(graph.keys()))

end_node = input(
    "Input the end node from below list \n {} - ".format(graph.keys()))
while(end_node not in graph.keys()):
    end_node = input(
        "Input the end node from below list \n {} - ".format(graph.keys()))

while((source_node == end_node)):
    print("The source and end node are same.")
    end_node = input(
        "Input the end node from below list \n {} - ".format(graph.keys()))

final_source = source_node
path = {}
queue = []

for node in graph:
    path[node] = float('inf')
    queue.append(node)

print("Initial path dictionary \n {}".format(path))
print("Initial queue list \n {}".format(queue))

distance = []
visited = []

while source_node != end_node:
    try:
        path[source_node] = 0
        in_dict = graph[source_node]

        short = min(in_dict.values())
        s = None

        for k in graph[source_node]:
            if(graph[source_node][k] == short and (k not in visited)):
                distance.append(short)
                visited.append(k)
                s = k

        #print("Visited now : {}".format(s))
        source_node = s
        #print("Changed source : {}".format(source_node))

        if(source_node == end_node):
            print("You reached your station.")
            final_visited = ' -> '.join([str(item) for item in visited])
            print("Path followed : {} -> {}".format(final_source, final_visited))
            print("Cost : {}".format(sum(distance)))

    except KeyError:
        print("You can reach to your end point from this source because there is not path available.")
        break
