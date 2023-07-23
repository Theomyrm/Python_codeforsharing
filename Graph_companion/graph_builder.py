import json
import networkx as nx
from graphviz import Graph, dot


class GraphBuilder:
    def __init__(self, graph_file):
        self.graph = nx.DiGraph()
        self.graph_data = None

    def load_graph_data(self, graph_file):
        with open(graph_file, 'r') as f:
            data = f.read()

        if "# opciones de formato de texto" in data:
            graph_data, text_format_section = data.split("# opciones de formato de texto")
            text_format_data = dict()
            for line in text_format_section.strip().split("\n"):
                key, value = line.split(":")
                text_format_data[key.strip()] = value.strip()
            self.text_format_data = text_format_data
        else:
            graph_data = data

        graph_data = json.loads(graph_data)

        if "edges_separator" not in graph_data:
            nodes_section = graph_data["nodes"]
            edges_section = graph_data["edges"]
        else:
            separator = graph_data.pop("edges_separator")
            nodes_section, edges_section = f.read().split(separator)

        self.graph_data = {"nodes": nodes_section, "edges": edges_section}

    def build_graph(self):
        graph_data = self.graph_data

        for node in graph_data['nodes']:
            self.graph.add_node(node['id'], **{k: str(v) for k, v in node['attrs'].items()})

        for edge in graph_data['edges']:
            self.graph.add_edge(edge['from'], edge['to'], **edge['attrs'])

    def add_edge(self, node1, node2, label="", color="black", weight=None):
        self.graph.add_edge(node1, node2, label=label, color=color, weight=weight)

    def visualize(self, output_file, format_options={}):
        dots = Graph()

        # Establecer opciones de formato predeterminadas
        dots.attr('graph', rankdir=format_options.get('rankdir', 'BT'))

        dots.attr('node', shape=format_options.get('node_shape', 'rectangle'),
                  style='filled', fillcolor=format_options.get('node_color', 'lightgray'),
                  fontname=format_options.get('font', 'Helvetica'),
                  fontsize=str(format_options.get('font_size', 12)),
                  fixedsize='true', width=str(format_options.get('node_width', 2.8)),
                  height=str(format_options.get('node_height', 0.8)))

        dots.attr('edge', arrowhead='vee', arrowsize=str(format_options.get('edge_arrow_size', 0)),
                  penwidth=str(format_options.get('edge_width', 0.8)), color=format_options.get('edge_color', 'white'))

        if format_options.get('layout', 'grid') == 'cartesian':
            pos = nx.spring_layout(self.graph, seed=42)
        else:
            pos = nx.kamada_kawai_layout(self.graph)

        for node in self.graph.nodes(data=True):
            dots.node(str(node[0]), **node[1])

        for edge in self.graph.edges(data=True):
            dots.edge(str(edge[0]), str(edge[1]), encoding='utf-8')

        for edge in self.graph.edges(data=True):
            attrs = dict()
            if 'weight' in edge[2]:
                attrs['weight'] = str(edge[2]['weight'])
            dots.edge(str(edge[0]), str(edge[1]), label=str(edge[2].get('label', '')),
                      color=edge[2].get('color', 'black'), **attrs)

        dots.format = format_options.get('format', 'png')
        dots.render(output_file, view=True)




