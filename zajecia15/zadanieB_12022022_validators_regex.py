import unidecode
import re


def remove_accents(string):

    # removes accents-> ł->l, ń-n etc
    str_decoded = unidecode.unidecode(string)

    return str_decoded


def remove_special_char_beginning(string):

    # remove special characters from beginning of a string
    str_no_special_char_b = re.sub(r"^\W+", "", string)

    return str_no_special_char_b


def remove_special_char_end(string):

    # remove special characters from end of a string
    str_no_special_char_e = re.sub(r"[^\w\s]+$", "", string)

    return str_no_special_char_e


def remove_special_char_beg_end(string):

    # remove special characters from beginning and end of string
    str_no_special_char_b_e = re.sub(r'^[^\w\s]+|[^\w\s]+$', '', string)

    return str_no_special_char_b_e


def remove_spec_char_inside_but_leave_some(string):

    # removes all special characters from inside string besides ._-
    str_only_spec_sp_char_inside = re.sub(r"[^a-zA-Z0-9 ._-]+", '', string)

    return str_only_spec_sp_char_inside
