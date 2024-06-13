<div align="center">
<h1>Difference Generator</h1>

<p>
Calculate the difference between two files
</p>

### Hexlet tests and linter status:
[![Actions Status](https://github.com/shizomanya/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shizomanya/python-project-50/actions)
[![Python CI](https://github.com/shizomanya/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/shizomanya/python-project-50/actions/workflows/main.yml)
<a href="https://codeclimate.com/github/shizomanya/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/6528a021231449c7b4a7/maintainability" /></a>
<a href="https://codeclimate.com/github/shizomanya/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/6528a021231449c7b4a7/test_coverage" /></a>

<p>
<a href="#about">About</a> •
<a href="#installation">Installation</a> •
<a href="#usage">Usage</a> •
<a href="#demo">Demo</a> •
</p>
</div>

<details><summary style="font-size:larger;"><b>Table of Contents</b></summary>

* [About](#about)
  * [Features](#features)
  * [Built With](#built-with)
  * [Makefile Commands](#makefile-commands)
* [Installation](#installation)
  * [Package](#package)
* [Usage](#usage)
* [Demo](#demo)
  * [Stylish format](#stylish-format)
  * [Plain format](#plain-format)
  * [JSON format](#json-format)

</details>

# GENDIFF (Difference Generator)
### About:
The package contains the program that outputs the differences between two files (JSON or YAML) in several possible formats.
Available formats: stylish (default), plain, json. A similar mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.
### Features:

* Supported file formats: JSON, YAML.
* Output as plain text, structured text or JSON.
* Can be used as CLI tool or external library.

### Built With:

* Python
* Poetry
* PyYAML
* JSON
* Pytest
* flake8
* argparse

### Makefile Commands:

Build the Poetry package: ```make build```

Install the package in the user's environment: ```make package-install```

Reinstall the package in the user's environment: ```make package-reinstall```

Check code with flake8 linter: ```make lint```

Run tests: ```make test```

Validate structure of pyproject.toml file, check code with tests and linter: ```make check```

---

## Installation

#### Python

Before installing the package make sure you have Python version 3.10 or higher installed:

```bash
>> python --version
Python 3.10.12
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

### Package

To use the package, you need to clone the repository to your computer. This is done using the ```git clone``` command. Clone the project:

```bash
>> git clone https://github.com/shizomanya/python-project-lvl2.git
```

Then you have to build the package and install it:

```bash
>> cd python-project-lvl2
```

```bash
>> poetry build
>> python3 -m pip install --user dist/*.whl
```

---

## Usage

Difference Generator can be used as CLI tool or as an external library.

```python
from gendiff import generate_diff
diff = generate_diff(file_path1, file_path2, file_format)
```
### As CLI tool

The general usage is (both absolute and relative paths to files are supported):

```bash
>> gendiff [-f file_format] file_path1 file_path2
```

Difference Generator provides help command as well:

```bash
>> gendiff --h

usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output (default: 'stylish')
```
[![asciicast](https://asciinema.org/a/gMh0PLOkydsTaMlcbqxGAgG7h.svg)](https://asciinema.org/a/gMh0PLOkydsTaMlcbqxGAgG7h)
## Demo:
### **Stylish format**
**Running a script with default settings:** `gendiff <file_path1> <file_path2>
If no format option is provided, output will be provided in _stylish_ format.

The difference is based on how the files have changed relative to each other, the keys are rendered in alphabetical order.

The absence of a plus or minus indicates that the key is in both files, and its values coincide. In all other situations, the value of the key is either different, or the key is only in one file.

```bash
>> gendiff file_path1.json file_path2.json

{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

**Comparing two files with a recursive structure: JSON.**

[![asciicast](https://asciinema.org/a/navH14NXTpHdp8sk9NCljU0Sh.svg)](https://asciinema.org/a/navH14NXTpHdp8sk9NCljU0Sh)

**Comparing two files with a recursive structure: YAML(YML).**

[![asciicast](https://asciinema.org/a/NOGewkSqrHp4Fnu4tNeSmTRYI.svg)](https://asciinema.org/a/NOGewkSqrHp4Fnu4tNeSmTRYI)


### **Plain format**
_Plain_ format reflects the situation as if we had combined the second object with the first one.

* If the new value of the property is a complex value, ```[complex value]``` is provided.
* If the property is nested, then the entire path to the root is displayed, not just including the parent.

```bash
>> gendiff --format plain file_path1.json file_path2.json

Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

[![asciicast](https://asciinema.org/a/3An1lox6Dy9CxmWp6sggqMPlL.svg)](https://asciinema.org/a/3An1lox6Dy9CxmWp6sggqMPlL)

### **JSON format**

In addition to an unstructured output (as a text), often an output in a structured format, such as JSON, is needed.

JSON (JavaScript Object Notation) is a standard text format for representing structured data based on JavaScript object syntax. It is usually used to transfer data in web applications (e.g. sending some data from the server to the client so that it can be displayed on a web page or vice versa).

```bash
>> gendiff --format json file_path1.json file_path2.json

{
    "follow": {
        "value": false,
        "type": "removed"
    },
    "host": {
        "value": "hexlet.io",
        "type": "unchanged"
    },
    "proxy": {
        "value": "123.234.53.22",
        "type": "removed"
    },
    "timeout": {
        "value": 50,
        "new value": 20,
        "type": "updated"
    },
    "verbose": {
        "value": true,
        "type": "added"
    }
}
```
[![asciicast](https://asciinema.org/a/kvOjLQ2YQwHQBpNsGov49XCuc.svg)](https://asciinema.org/a/kvOjLQ2YQwHQBpNsGov49XCuc)
