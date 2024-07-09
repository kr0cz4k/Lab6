import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji danych.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego.')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego.')
    return parser.parse_args()

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    args = parse_arguments()
    data = read_json(args.input_file)
    print(data)
