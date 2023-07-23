import argparse
import os


from graph_builder import GraphBuilder
from graph_parser import GraphParser


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build a graph from input file and visualize it.')
    parser.add_argument('input_file', type=str, help='Input file path.')
    parser.add_argument('-o', '--output', type=str, default='graph.png', help='Output file path.')
    parser.add_argument('-f', '--format', type=str, default='json', help='Input file format. Options: json, txt.')
    parser.add_argument('-p', '--parse', action='store_true', help='Parse input file to json.')

    # Add options for text format
    parser.add_argument('-s', '--style', type=str, default='standard', help='Graph style. Options: standard, clean.')
    parser.add_argument('--node-shape', type=str, default='rectangle', help='Node shape. Options: ellipse, rectangle.')
    parser.add_argument('--node-color', type=str, default='lightgray', help='Node color.')
    parser.add_argument('--edge-color', type=str, default='gray', help='Edge color.')
    parser.add_argument('--font', type=str, default='Helvetica', help='Font used in the graph')
    parser.add_argument('--font-size', type=int, default=12, help='Font size used in the graph')
    parser.add_argument('--node-width', type=float, default=0.75, help='Width of nodes')
    parser.add_argument('--node-height', type=float, default=0.5, help='Height of nodes')
    parser.add_argument('--edge-width', type=float, default=1.0, help='Width of edges')
    parser.add_argument('--edge-arrow-size', type=float, default=0.5, help='Size of edge arrows')
    parser.add_argument('--rankdir', type=str, default='TB', help='Direction of the layout (TB, LR, BT, RL)')
    parser.add_argument('--layout', type=str, default='grid', help='Layout type. Options: grid, cartesian.')

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print("Input file does not exist.")
        exit()

    if args.format not in ['json', 'txt']:
        print("Invalid input file format.")
        exit()

    if args.parse:
        output_file = args.output.split('.')[0] + '.json'
        graph_parser = GraphParser(args.input_file, output_file)
        text_format_data = graph_parser.parse()
        print(f"Graph data parsed and saved to {output_file}")
    else:
        if args.format == '.txt':
            graph_parser = GraphParser(args.input_file)
            graph_data = graph_parser.parse_txt()
        else:
            graph_data = args.input_file.split('.')[0] + '.json'
            graph_parser = GraphParser(args.input_file, graph_data)
            graph_parser.parse()
            print(f"Graph data parsed and saved to {graph_data}")
            graph_builder = GraphBuilder(graph_data)
            graph_builder.load_graph_data(graph_data)
            graph_builder.build_graph()
            # Add text formatting options
            format_options = {
                'fontname': args.font,
                'fontsize': str(args.font_size),
                'nodeshape': args.node_shape,
                'nodecolor': args.node_color,
                'edgecolor': args.edge_color,
                'width': str(args.node_width),
                'height': str(args.node_height),
                'penwidth': str(args.edge_width),
                'arrowsize': str(args.edge_arrow_size),
                'rankdir': args.rankdir,
            }

            graph_builder.visualize(args.output, format_options=format_options)

"""
Usage:
    main.py <input_file> [-o <output_file>] [-f <file_format>] [-p] [--<format_option> <option_value> ...]

Build a graph from an input file and visualize it.

Arguments:
    <input_file>            Input file path.

Options:
    -h --help               Show this screen.
    -o --output <output_file>
                            Output file path. [default: graph.pdf]
    -f --format <file_format>
                            Input file format. Options: json, txt. [default: json]
    -p --parse              Parse input file to json.
    --style <graph_style>   Graph style. Options: standard, clean. [default: standard]
    --node-shape <node_shape>
                            Node shape. Options: ellipse, rectangle. [default: ellipse]
    --node-color <node_color>
                            Node color. [default: lightgray]
    --edge-color <edge_color>
                            Edge color. [default: gray]
    --font <font>           Font used in the graph. [default: Helvetica]
    --font-size <font_size>
                            Font size used in the graph. [default: 12]
    --node-style <node_style>
                            Node style. Options: filled, dashed, dotted. [default: filled]
    --node-width <node_width>
                            Width of nodes. [default: 0.75]
    --node-height <node_height>
                            Height of nodes. [default: 0.5]
    --edge-style <edge_style>
                            Edge style. Options: solid, dashed, dotted. [default: solid]
    --edge-width <edge_width>
                            Width of edges. [default: 1.0]
    --edge-arrow-size <edge_arrow_size>
                            Size of edge arrows. [default: 0.5]
    --rankdir <rankdir>     Direction of the layout. Options: TB, LR, BT, RL. [default: TB]

"""