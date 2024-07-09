import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji danych.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego.')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego.')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(f'Input file: {args.input_file}')
    print(f'Output file: {args.output_file}')
