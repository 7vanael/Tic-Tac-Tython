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

### Get the Game

Clone the repository:
For macOS & Linux:
```
git clone https://github.com/7vanael/tic-tac-tython.git
cd tic-tac-tython
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
for Windows:

```
git clone https://github.com/7vanael/tic-tac-tython.git
cd tic-tac-tython
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Usage

To play the game:
`python main.py`

### Running Tests

Run all tests:

`pytest -v`

Run a specific test file:

`pytest tests/test_board.py -v`