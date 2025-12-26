from case_rush.menus import main_menu
from case_rush.db import Database
from case_rush.utils import index_items


def main():
    try:
        Database.connect()
        Database.init()

        index_items()
        main_menu()

    except IndexError:
        print("Make sure that rewards exist in the items directory.")

    except Exception as e:
        print("Some error occured:", e)

    finally:
        Database.close()


if __name__ == "__main__":
    main()
