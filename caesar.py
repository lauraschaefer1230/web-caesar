
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

def alphabet_position(letter):
    for ch in letter:
        pos = alphabet.index(ch)
        return pos


def rotate_character(char, rot):
    # check to see if the char is a letter
    if char.isalpha():
        Is_Upper = False
        if char.isupper():
            Is_Upper = True
            char = char.lower()
        # idx = int(alphabet.index(char))
        idx = alphabet_position(char)
        # rot = int(argv)
        new_idx = (idx + rot) % 26
        new_char = alphabet[new_idx]

        if Is_Upper:
            return new_char.upper()

        return new_char

    return char

def encrypt(text, rot):
    #alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                #'v', 'w', 'x', 'y', 'z']
    newmsg = []
    # rot = argv[1]
    for char in text:
        if char.isalpha() is False:
            newmsg.append(char)
        else:
            new_char = rotate_character(char, rot)
            newmsg.append(new_char)

    return ''.join(newmsg)
