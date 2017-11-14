# Prettify JSON

The program takes a json file, and returns a formatted json file in console.

# Quickstart

You need to download and install python3 if you already haven't: http://python.org .

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
{
    "title": "Person",
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "age": {
            "description": "Age in years",
            "type": "integer",
            "minimum": 0
        }
    },
    "required": [
        "firstName",
        "lastName"
    ]
}
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
