def reverse_string(characters):
    reversedString = ''
    for char in characters:
        reversedString = char + reversedString
    return reversedString


print(reverse_string("GCTAGCT"))
