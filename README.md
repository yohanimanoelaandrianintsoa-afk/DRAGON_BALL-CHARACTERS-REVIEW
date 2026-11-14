# 🐉 Dragon Ball Z Characters Explorer

A small command-line app built with **Python** and **pandas** to explore a dataset of Dragon Ball Z characters: search a character, filter by race, check power levels, and more.

I built this project to practice data manipulation with pandas and to write an interactive terminal menu from scratch.

## Features

| Option | What it does |
|--------|--------------|
| **1. Search a character** | Look up a character by name and get their gender, race, affiliation, ki, and a link to their picture |
| **2. Filter by race** | List every character belonging to a race (Saiyan, Human, Namekian, Frieza Race, Android, Majin, God, Evil) |
| **3. Character ki** | Show the base ki and the max ki of a character |
| **4. Understand column features** | Short explanation of the main dataset columns |
| **5. All characters** | Display the full list of characters |
| **6. Exit** | Quit the app |

The menu handles invalid input (letters, out-of-range numbers) without crashing.

## Dataset

The app reads `dragon_ball_z_characters.csv`, which contains the following columns:

- `name`: character's full name
- `ki`: base power level
- `maxKi`: maximum power level
- `race`: species or racial background
- `gender`
- `description`
- `image`: link to a picture of the character
- `affiliation`: main group or allegiance (e.g. Z Fighter)

> Note: `ki` and `maxKi` are stored as text (e.g. `60.000.000`, `90 Septillion`), not as numbers.

## Getting started

### Requirements

- Python 3.10 or newer
- pandas

### Installation

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

python3 -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
pip install pandas
```

### Run

```bash
python3 myapp.py
```

## Example

```text
*** Here is what you can do ? ***

 1- Search a character
 2- Filter by race
 3- Character ki
 4- Understand column features
 5- All characters
 6- Exit

 Please enter your choice: 1

 Enter your character name : Goku

 Goku is a Male Saiyan from the Z Fighter side, with a ki of 60.000.000.
```

## Project structure

```text
.
├── myapp.py                          # The application
├── dragon_ball_z_characters.csv      # Characters dataset
├── dragon_ball_z_column_descriptors.txt
└── README.md
```

## What I learned

- Reading and filtering CSV data with pandas (`read_csv`, boolean masks, `iloc`)
- Building an interactive menu with `input()`, loops, and `try/except`
- Handling file encoding (UTF-8) and messy real-world data

## Roadmap

- [ ] Case-insensitive search and "did you mean...?" suggestions
- [ ] Convert `ki` values to numbers to compare two characters ("who is stronger?")
- [ ] Charts with matplotlib (power levels, races distribution)
- [ ] Web interface with Streamlit

## Author

**Yohan** — Computer Science student at Université de Bordeaux.
