# Tic-Tac-Tython

This is a game of Tic-Tac-Toe in Python where you can 
play against an unbeatable computer opponent. Good luck!

## Installation

### Prerequisites

Check if you have Python 3 installed (minimum version 3.10 required):
`python3 --version`

If not installed, you have a couple options:

**Option 1: Using Homebrew (macOS/Linux)**

`brew install python`

**Option 2: Download from python.org**

Download and install [Python](https://www.python.org/downloads/) using the installation wizard.

### Install the Game

Clone the repository:
```
git clone https://github.com/yourusername/tic-tac-tython.git
cd tic-tac-tython
```

Install the package:
`pip install .`

Or for development mode:
`pip install -e '.[dev]'`

## Usage

To play the game:

`python -m tic_tac_toe.main`

## Development

### Install Development Dependencies
`pip install -e '.[dev]'`

### Running Tests

Run all tests:

`pytest -v`

Run a specific test file:

`pytest tests/test_board.py -v`

### Development

To import and install test dependencies, run:
`python -m pip install -e '.[dev]'`

