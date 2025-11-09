from src.menus import main_menu
from src.db import Database
from src.utils import index_items


def main():
    try:
        Database.connect()
        Database.init()

        index_items()
        main_menu()

    except Exception as e:
        print("Some error occured:", e)

    finally:
        Database.close()


if __name__ == "__main__":
    main()
