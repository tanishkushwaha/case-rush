"""
Provides application info.
"""

import case_rush.__version__ as meta

from rich import print as rprint


def about_menu():
    rprint("\n[bold]----- About -----[/bold]\n")
    rprint(f"App Name: {meta.__app_name__}")
    rprint(f"Version: {meta.__version__}")
    rprint(f"Author: {meta.__author__}")
    rprint(f"\n[bold]{meta.__copyright__}[/bold]")
