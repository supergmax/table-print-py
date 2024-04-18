
import argparse
import csv
import json
import sys
from rich.console import Console
from rich.table import Table

# Default options
DEFAULT_OPTIONS = {
    "verbose": False,
    "draw_lines": True,
    "table_style": "default",
    "extract": None  # Option for extracting data into a JSON file
}

def lire_csv(nom_fichier, options):
    data = []  # To collect data for JSON extraction
    text_color = options['color'] if options['color'] else "none"  # Default text color for table data
    line_color = options['line_color'] if options['line_color'] else "none"  # Color for table lines

    table = Table(expand=True, show_lines=options['draw_lines'], border_style=line_color)

    with open(nom_fichier, newline='', encoding='utf-8') as fichier_csv:
        lecteur = csv.reader(fichier_csv, delimiter=',')
        for i, ligne in enumerate(lecteur):
            if i == 0:
                for titre_colonne in ligne:
                    table.add_column(titre_colonne)
            else:
                table.add_row(*ligne, style=text_color)
                data.append(ligne)

    console = Console()
    console.print(table)

    if options['extract']:  # Check if JSON extraction is required
        with open(options['extract'], 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)


def parse_args():
    parser = argparse.ArgumentParser(description="Display a CSV file using Rich")
    parser.add_argument('fichier', metavar='fichier', type=str, help='path to the CSV file')
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")
    parser.add_argument("--no-lines", dest="draw_lines", action="store_false", help="Disable drawing lines")
    parser.add_argument("--color", type=str, default=None, help="Choose text color for the table data")
    parser.add_argument("--line-color", type=str, default=None, help="Choose color for the table lines")
    parser.add_argument("--extract", type=str, help="Path to output JSON file")
    
    return parser.parse_args()



def main():
    args = parse_args()
    
    options = {**DEFAULT_OPTIONS, **vars(args)}
    
    if args.verbose:
        print("Options:")
        for key, value in options.items():
            print(f"{key}: {value}")
    
    lire_csv(args.fichier, options)

if __name__ == "__main__":
    main()
