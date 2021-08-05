# Quantulum3 Test

Simple application, that makes use of quantulum3 package for testing the extraction of mass accumulation rates (MAR) and sedimentation rates.

The Python 3 compatible fork of quantulum by [nielstron](https://github.com/nielstron/quantulum3) is used.

**Work in progress!**

## Table of Contents

- [Getting Started](#getting-started)
- [Built With](#built-with)
- [License](#license)

## Getting Started

These instructions will get you a copy of the project up and running on your local
machine for development and testing purposes.

### Prerequisites

This project is written in Python.

- Python 3.6+

### Installing

Clone project with

```sh
git clone git@github.com:thorge/quantulum3-test.git
```

Create python environment from project directory with

```sh
cd quantulum3-test
python -m venv .venv
```

Activate environment with

```sh
source .venv/bin/activate
```

Install requirements with

```sh
pip install -r requirements.txt
```

### Run the application

You can run the tests from project directory with

```sh
python quantulum-test.py
```

### Testcases

You can find all test sentences to be parsed in the corresponding JSON files:

- [Mass Accumulation Rates](test-mar.json) -
Test data for extraction of mass accumulation rates
- [Sedimentation Rates](test-sr.json) -
Test data for extraction of sedimentation rates

## Built With

- [Quantulum3](https://github.com/nielstron/quantulum3) -
Library for unit extraction

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
file for details.