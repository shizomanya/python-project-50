### Hexlet tests and linter status:
[![Actions Status](https://github.com/shizomanya/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shizomanya/python-project-50/actions)

[![Python CI](https://github.com/shizomanya/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/shizomanya/python-project-50/actions/workflows/main.yml)

<a href="https://codeclimate.com/github/shizomanya/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/1dd0509a1bde548c87e2/maintainability" /></a>

<a href="https://codeclimate.com/github/shizomanya/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/6528a021231449c7b4a7/test_coverage" /></a>

# GENDIFF (Difference Generator)
### Description:
The package contains the program that outputs the differences between two files (JSON or YAML) in several possible formats.
Available formats: stylish (default), plain, json. A similar mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.
### Requirements:
```
python = "^3.10"
```
### Installation Instruction:
```
$ python3 -m pip install git+https://github.com/shizomanya/python-project-50
```
```python
install: make install

build: make build

package-install: python3 -m pip install --user --force dist/*.whl

lint: poetry run flake8
```
### Ascinema

**Launching Help:**

`gendiff -h`

**Running a script with default settings:**

`gendiff <file_path1> <file_path2>`

**Comparing two plain files: JSON.**



**Comparing two plain files: YAML(YML).**



**Comparing two files with a recursive structure: YAML(YML) или JSON.**


