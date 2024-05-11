import base64
from subprocess import run


class Vertex:
    def __init__(self, vertex_id, label):
        self.id = vertex_id
        self.label = label

    def __str__(self):
        return f"({self.id}, {self.label})"


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, vertex_id, label):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = Vertex(vertex_id, label)
            self.edges[vertex_id] = []

    def add_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id in self.vertices and to_vertex_id in self.vertices:
            self.edges[from_vertex_id].append(to_vertex_id)
        else:
            print(f"One or both vertices not found in graph.{from_vertex_id} and {to_vertex_id}")

    def get_vertex(self, vertex_id):
        return self.vertices.get(vertex_id)

    def get_neighbors(self, vertex_id):
        return self.edges.get(vertex_id, [])

    def mm_display(self):
        mermaid_markdown = ""
        mermaid_markdown += "    flowchart BT\n"
        for vertex_id, vertex in self.vertices.items():
            mermaid_markdown += f"""    node{vertex.id}(["{vertex.label}"])\n"""
        for from_vertex_id, to_vertices in self.edges.items():
            for to_vertex_id in to_vertices:
                mermaid_markdown += f"    node{self.vertices[from_vertex_id].id} --> node{self.vertices[to_vertex_id].id}\n"
        print(f"```mermaid\n{mermaid_markdown}\n```")
        encoded = base64.b64encode(mermaid_markdown.encode())
        print(f"\n\nhttps://mermaid.ink/img/{encoded.decode()}")


input_path = input("Enter path of C file (ex. data\\test.c)\n>> ").replace('\\', '\\\\')
data = run("yacc < data\\test.c", capture_output=True, shell=True, text=True)
content = data.stderr.split('\n')
g = Graph()

stk = ["0-0"]
state_num, state_token = '', ''
state_map = {}

# mapping states
for i in range(1, len(content)):
    if len(content[i]) < 1:
        continue
    w = content[i].split()
    if w[0] == "Entering":
        state_num = w[-1]
        if state_num in state_map.keys():
            continue
        state_map[state_num] = content[i - 1].split()[-2]

# derive a tree
vid, token = '', ''
tracking_stack = []
i = 0
while i < len(content):
    w = content[i].split()
    if w[0] == "Now":
        break
    if w[0] != "Stack":
        i += 1
        continue
    current_stack = [x for x in w[2:]]
    top_vid = f"{i}_{current_stack[-1]}"
    if len(current_stack) > len(tracking_stack):
        g.add_vertex(top_vid, state_map[current_stack[-1]])
    else:
        g.add_vertex(top_vid, state_map[current_stack[-1]])
        while len(current_stack) <= len(tracking_stack):
            g.add_edge(tracking_stack.pop(), top_vid)
    tracking_stack.append(top_vid)
    i += 1
g.add_edge(tracking_stack.pop(), tracking_stack.pop())

g.mm_display()
