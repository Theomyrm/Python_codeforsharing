import json
import re

TEXT_FORMAT_SECTION = "# opciones de formato de texto\n"


class GraphParser:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def parse(self):
        graph_data = {"nodes": [], "edges": []}
        with open(self.input_file, 'r') as f:
            data = f.read()
        print(data)
        if "# nodos" not in data:
            raise ValueError("Sección de nodos no encontrada en el archivo de entrada.")

        if "# aristas" not in data:
            raise ValueError("Sección de aristas no encontrada en el archivo de entrada.")

        nodes_section, edges_and_text_format_section = data.split("# aristas")
        edges_section, text_format_section = edges_and_text_format_section.split(TEXT_FORMAT_SECTION)

        # Parsear sección de nodos
        for node_str in nodes_section.split("\n"):
            if not node_str.strip():
                continue
            node_match = re.match(r'(\d+),\s*(\{.*\})', node_str.strip())
            if node_match:
                node_id, attrs_str = node_match.groups()
                attrs = json.loads(attrs_str.strip())
                graph_data["nodes"].append({"id": node_id.strip(), "attrs": attrs})

        # Parsear sección de aristas
        for edge_str in edges_section.split("\n"):
            if not edge_str.strip():
                continue
            source, target, attrs_str = edge_str.split(",", 2)
            attrs = json.loads(attrs_str.strip())
            graph_data["edges"].append({"from": source.strip(), "to": target.strip(), "attrs": attrs})

        # Parsear sección de opciones de formato de texto
        text_format_data = dict()
        for line in text_format_section.split("\n"):
            if not line.strip():
                continue
            key, value = line.strip().split(":")
            text_format_data[key.strip()] = value.strip()
            graph_data["format_options"] = text_format_data

        with open(self.output_file, 'w') as f:
            json.dump(graph_data, f, indent=4)

        return text_format_data
