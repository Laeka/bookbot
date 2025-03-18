"""
Este modulo contiene funciones para leer y procesar archivos de texto
"""

import sys
from stats import get_number_words, get_number_char, sorted_chars


def get_book_text(path):
    """
    Lee el contenido de un archivo de texto en una ruta
    Args:
        path(str): La ruta del archivo
    Returns:
        str: El contenido del archivo
    """
    print("============ BOOKBOT ============")
    file_contents = ""
    with open(path, encoding="utf-8") as f:
        file_contents = f.read()
        print(f"Analyzing book found at {path}...")

    return file_contents


def main():
    """
    Funcion principal que ejecuta el programa
    """
    if len(sys.argv) - 1 < 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_content = get_book_text(sys.argv[1])

    get_number_words(file_content)

    char_dict = get_number_char(file_content)

    sorted_chars(char_dict)


main()
