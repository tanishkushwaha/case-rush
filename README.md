# Case Rush

A lightweight lootbox simulator game with tier-based rewards.

## Installation

Make sure you have Python 3.10+ installed.

1. Install `pipx` for global isolated installation.

   ```bash
   sudo apt install pipx
   pipx ensurepath
   ```

2. `cd` into the root directory.

   ```bash
   cd case-rush
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

---
