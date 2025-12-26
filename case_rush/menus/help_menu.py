"""
Provides help info for the app.
"""

from rich import print as rprint

from case_rush.paths import CONFIG_DIR, ITEMS_DIR


def help_menu():
    rprint("\n[bold]----- Help -----[/bold]\n")
    rprint(f"Items Directory: {ITEMS_DIR}")
    rprint(f"Config File: {CONFIG_DIR / 'config.toml'}")
