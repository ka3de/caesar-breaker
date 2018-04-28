#!/usr/bin/env python

import sys
import string
import getopt


ALPHABET = list(string.ascii_lowercase)
MOST_FREQUENT_LETTER_BY_LANG = {'en': 'e'}


def usage():
    print("Usage: caesar-breaker.py [OPTIONS] \"ciphertext\"")
    print("     -f, --force     - Decrypt using brute force, otherwise shifts are calculated based on the language")
    print("     -l, --lang      - Language that the plaintext is supposed to be in")


def get_letters_frequency(text):
    """
    returns a map containing each text letter and its frequency
    """
    letters_frequency = {}

    for letter in text:
        if letter.isalpha():
            if letter in letters_frequency:
                letters_frequency[letter] += 1
            else:
                letters_frequency[letter] = 1

    return letters_frequency


def calculate_shifts(letters_frequency, lang):
    """
    returns the number of shifts based on the text's letters frequency map
    and the language that the text is supposed to be written in
    """
    most_freq_letter = max(letters_frequency, key=letters_frequency.get)
    return ALPHABET.index(MOST_FREQUENT_LETTER_BY_LANG[lang]) - ALPHABET.index(most_freq_letter)


def decrypt(ciphertext, rotations):
    """
    returns the input text with its letters rotated around the alphabet
    following a forward or backward direction
    """
    global ALPHABET
    plaintext = ""

    for letter in ciphertext:
        if letter.isalpha():
            plaintext += ALPHABET[(ALPHABET.index(letter) + rotations) % len(ALPHABET)]
        else:
            plaintext += letter

    return plaintext


def main():
    force_flag = False
    lang = ""

    if len(sys.argv) < 3:
        usage()
        sys.exit(2)

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hfl:',
                                   ['help', 'force', 'lang'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-f', '--force'):
            force_flag = True
        elif opt in ('-l', '--lang'):
            lang = arg
        else:
            usage()
            sys.exit(2)

    ciphertext = sys.argv[-1].lower()

    # Decrypt by Brute Force
    if force_flag:
        for nshift in range(len(ALPHABET)):
            print(decrypt(ciphertext, nshift))

    # Decrypt based on lang
    else:
        letters_freq = get_letters_frequency(ciphertext)
        shifts = calculate_shifts(letters_freq, lang)
        print(decrypt(ciphertext, shifts))


if __name__ == '__main__':
    main()