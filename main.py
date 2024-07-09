import argparse
import json
import xml.etree.ElementTree as ET
import yaml
import os


def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji danych.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego.')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego.')
    return parser.parse_args()

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return ET.tostring(root, encoding='unicode')

def write_xml(data, file_path):
    root = ET.fromstring(data)
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='unicode')

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def convert_data(input_file, output_file):
    input_ext = os.path.splitext(input_file)[1]
    output_ext = os.path.splitext(output_file)[1]
    
    if input_ext == '.json':
        data = read_json(input_file)
    elif input_ext == '.xml':
        data = read_xml(input_file)
    elif input_ext in ['.yml', '.yaml']:
        data = read_yaml(input_file)
    else:
        raise ValueError("Nieobsługiwany format pliku wejściowego")
    
    if output_ext == '.json':
        write_json(data, output_file)
    elif output_ext == '.xml':
        write_xml(data, output_file)
    elif output_ext in ['.yml', '.yaml']:
        write_yaml(data, output_file)
    else:
        raise ValueError("Nieobsługiwany format pliku wyjściowego")

if __name__ == "__main__":
    args = parse_arguments()
    convert_data(args.input_file, args.output_file)
