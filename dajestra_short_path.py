# def => یک کیوورد برای تعریف فانکشن


def create_graph():
    #دارد که به معنی وجود یال و وزن آن هست j و i ماتریس مجاورتی رو به وجود میاریم هر عنصر یک 
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

#از یک گره مبدا شروع میکنیم به پیمایش
source_node = input(
    "Input the sourse node from below list \n {} - ".format(graph.keys()))
while(source_node not in graph.keys()):
    source_node = input(
        "Input the sourse node from below list \n {} - ".format(graph.keys()))
#مسیر نهایی رو هم مشخص میکنیم
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

# iبردار مسیر رو مشخص میکنیم که نشون میده اندازه مسیر طی شده از نقطه مبدا تا نقطه 
distance = []

#بردار وضعیت که نشون میده وضعیت یک راس رو که آیا این راس بررسی شده یا نه  
status = []

#ابتدا از یک گره مبدا شروع می کنیم و وضعیت آن را پایدار قرار می دهیم
#بعد از آن گره هایی که با گره مبدا یال مستقیم دارند را بروز می کنیم و مقدار هزینه و گره قبلی آن ها را تغییر می دهیم
#در مرحله بعد یکی از گره های که تا کنون بررسی نشده اند را انتخاب و آن را در حالت پایدار قرار می دهیم
#سپس مجددا وضعیت گره های همسایه آن را بررسی می کنیم تا ببینیم ایا این گره می تواند .
#در کوتاه تر شدن مسیر مبدا تا همسایه ها تاثیر گذار باشد یا خیر این روال تا پیدا شدن مسیر نهایی ادامه دارد
while source_node != end_node:
    try:
        path[source_node] = 0
        in_dict = graph[source_node]

        short = min(in_dict.values())
        s = None

        for k in graph[source_node]:
            if(graph[source_node][k] == short and (k not in status)):
                distance.append(short)
                status.append(k)
                s = k

        print("Visited now : {}".format(s))
        source_node = s
        print("Changed source : {}".format(source_node))

        if(source_node == end_node):
            print("You reached your station.")
            final_status = ' -> '.join([str(item) for item in status])
            print("Path followed : {} -> {}".format(final_source, final_status))
            print("Cost : {}".format(sum(distance)))

    except KeyError:
        print("You can reach to your end point from this source because there is not path available.")
        break
