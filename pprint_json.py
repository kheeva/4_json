import sys
import json


def load_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf8') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError as error:
        print(error)
    except json.JSONDecodeError as error:
        print(error)
    else:
        return json_data
    return {}


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


def main():
    if len(sys.argv) != 2:
        print("Usage: python pprint_json.py path_to_json_file.")
        exit(1)

    file_path = sys.argv[1]
    json_data = load_data(file_path)

    if not json_data:
        print('No data!')
        exit(1)

    pretty_print_json(json_data)

if __name__ == '__main__':
    main()
