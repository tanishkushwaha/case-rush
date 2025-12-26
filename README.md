# Case Rush

A lightweight gacha lootbox game with custom tier-based rewards.

## Installation

Make sure you have Python 3.10+ installed.

1. Clone the repo and `cd` into it.

   ```bash
   git clone https://github.com/tanishkushwaha/case-rush.git

   cd case-rush
   ```

2. Install `pipx` for global isolated installation.

   ```bash
   sudo apt install pipx
   pipx ensurepath
   ```

3. Run the following command for the installation.

   ```bash
   pipx install .
   ```

4. At this point, the application would be successfully installed. Run the application by running `case-rush` in the terminal.

## Uninstall

1. `pipx uninstall case-rush`

2. Delete the following directories:

   1. `~/.local/share/case-rush`
   2. `~/.config/case-rush`
   3. `~/.cache/case-rush`

   Either manually or by using the following command:

   ```bash
   rm -rf ~/.local/share/case-rush ~/.config/case-rush ~/.cache/case-rush
   ```

**Note:** This command permanently deletes all Case Rush user data and configuration.

## Development

1. Create a virtual environment.

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment.

   ```bash
   source venv/bin/activate
   ```

3. Install the required modules.

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application.

   ```bash
   python -m case_rush.app
   ```

## Docs

### Add Rewards

Add your reward image files to the `items` directory.

To reveal the `items/` directory path, run the application and go to `Settings > Help`.

The `items` directory consists of 5 sub-directories `A, B, C, D, S`.

```
items/
    ├── A/
    ├── B/
    ├── C/
    ├── D/
    └── S/

```

Each sub-directory represents a tier as follows:

```
S: Legendary
A: Epic
B: Rare
C: Uncommon
D: Common
```

Paste your reward image files in those sub directories based on their corresponding tiers and restart the application.

### Import & Export Data (Player Progress)

#### Export

To export your data, go to `Settings > Export Data`.

#### Import

Extract the contents of the exported `.zip` into the `data/` directory and restart the application.

To reveal the `data/` directory path, go to `Settings > Help`.

### Config

All the configuration such as drop rates a claim cooldown are stored in the `config.toml` file.

To reveal `config.toml` path, go to `Settings > Help`.

The file contents look as follows:

```
[drop_rates]
legendary = 0.02
epic = 0.06
rare = 0.12
uncommon = 0.3
common = 0.5

[delays]
case_opening = 5  # seconds
claim_cooldown = 3600  # seconds

```

**Note:** The drop rates must add up exactly to 1.

After making changes to the config file, restart the application for them to take effect.
