import re


def is_applicable(substitution, word):
    return substitution[0] in word


def apply_substitution(substitution, word):
    index = word.find(substitution[0])
    return word[:index] + substitution[1] + word[index + len(substitution[0]):]


def apply_scheme_once(scheme, word):
    for substitution in scheme:
        if is_applicable(substitution, word):
            return [apply_substitution(substitution, word), substitution[2]]
    return [word, True]


def apply_scheme(scheme, word):
    while True:
        word, stop = apply_scheme_once(scheme, word)
        if stop:
            return word


def read_from_file(index):
    file_in_name = str(index) + ".in"
    file_in = open("tests/" + file_in_name, "r")
    word = file_in.readline()
    substitutions = file_in.readlines()
    return [word, substitutions]


def parse_substitutions(substitutions):
    list_of_substitutions = []
    substitution_reg = r"([a-zA-Z\\\|\/]+)?( ?\-\>\.? ?)([a-zA-Z\\\|\/]+)?"
    for substitution in substitutions:
        groups = re.findall(substitution_reg, substitution)[0]
        find_string, arrow, replace_string = groups
        is_terminal = 0
        if "." in arrow:
            is_terminal = 1
        list_of_substitutions.append([find_string, replace_string, is_terminal])
    return list_of_substitutions


def main():
    for index in range(4):
        print("Test #" + str(index))
        data = read_from_file(index)
        word = data[0].strip()
        substitutions = data[1]
        scheme = parse_substitutions(substitutions)
        word = apply_scheme(scheme, word)
        print(word)


main()
