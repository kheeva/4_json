import sys
import json


def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf8') as json_file:
        loaded_data = json.load(json_file)
    return loaded_data


def pretty_print_json(loaded_data):
    print(json.dumps(loaded_data, indent=4, ensure_ascii=False))


def main():
    if len(sys.argv) != 2:
        exit("Usage: python pprint_json.py path_to_json_file.")

    try:
        loaded_data = load_json_data(sys.argv[1])
    except FileNotFoundError as error:
        exit(error)
    except json.JSONDecodeError as error:
        exit(error)
    else:
        pretty_print_json(loaded_data)


if __name__ == '__main__':
    main()
