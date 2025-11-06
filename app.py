from menus import main_menu
from db import cursor, connection
from utils import index_items


def main():
    try:
        index_items()
        main_menu()

    except Exception as e:
        print("Some error occured:", e)

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
