### Project #2 "Generate Difference"
***

### Hexlet tests and linter status:
[![Actions Status](https://github.com/lion0k/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/lion0k/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/9ecda195d2460865c83f/maintainability)](https://codeclimate.com/github/lion0k/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9ecda195d2460865c83f/test_coverage)](https://codeclimate.com/github/lion0k/python-project-lvl2/test_coverage)
***

This is the second project in the Python learning course [hexlet.io](https://ru.hexlet.io)

This package allows you to compare two files (json/yaml).
Shows the difference between them using different output formats ('stylish', 'plain', 'json')
***
#### Installation
* Install [poetry](https://python-poetry.org/docs/#installation)
* ```git clone https://github.com/lion0k/python-project-lvl2.git```
* ```cd python-project-lvl2/ && make install```
***
#### Usage
* ```python -m gendiff.scripts.gendiff file1.json file2.json```
* ```poetry run gendiff file1.json file2.json```
***
##### Comparing simple files 

[![asciicast](https://asciinema.org/a/HpCEequ6QxQGlbNCbHObK2eHd.svg)](https://asciinema.org/a/HpCEequ6QxQGlbNCbHObK2eHd)

##### Comparing files using 'stylish' output format

[![asciicast](https://asciinema.org/a/8CfNWzQiYi7ro6kUsJ18Ged1p.svg)](https://asciinema.org/a/8CfNWzQiYi7ro6kUsJ18Ged1p)

##### Comparing files using 'plain' output format

[![asciicast](https://asciinema.org/a/MIFRamxTJaa2USYgcChYXxQiZ.svg)](https://asciinema.org/a/MIFRamxTJaa2USYgcChYXxQiZ)

##### Comparing files using 'json' output format

[![asciicast](https://asciinema.org/a/LBe53M5IYFJUNtX85tHpEPMad.svg)](https://asciinema.org/a/LBe53M5IYFJUNtX85tHpEPMad)