"""
Este modulo contiene funciones para retornar el numero total de palabras
"""


def get_number_words(text_content):
    """
    Lee el contenido de un texto para regresar el numero de palabras
    """
    all_words = text_content.split()
    number_of_words = len(all_words)
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    return number_of_words


def get_number_char(text_content):
    """
    Lee el contenido de un texto para regresar el total de cada caracter
    """
    text_lower = text_content.lower()
    char_dictionary = {}
    for c in text_lower:
        if c in char_dictionary:
            char_dictionary[c] += 1
        else:
            char_dictionary[c] = 1

    return char_dictionary


def sorted_chars(char_dir):
    """
    Lee un diccionario y devuelve la lista ordenada de mayor a menor
    """
    chars_list = []
    for char, count in char_dir.items():
        if char.isalpha():
            char_info = {"char": char, "count": count}
            chars_list.append(char_info)

    chars_list.sort(reverse=True, key=lambda dict: dict["count"])

    print("--------- Character Count -------")
    for char_info in chars_list:
        print(f"{char_info['char']}: {char_info['count']}")

    return chars_list
