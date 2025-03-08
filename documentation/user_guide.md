# User guide

## Installation and launching
Clone the project repository from GitHub to your local computer. In the root directory of the project, run the command

```bash
poetry install
```

to install the dependencies of the project. Activate the virtual environment with the command

```bash
poetry shell
```

The application can now be launched by running the command

```bash
python3 src/index.py
```

## How to use the application
The user gets to make the first move and plays as X. The AI plays as O and it may take a couple of seconds before the AI responds to the move made by the user. A messagebox announcing the winner appears once the game has concluded. The game can be restarted by pressing the RESTART button in the lower left corner of the window.