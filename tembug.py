def repete_vogal(word):
    """Retorna a palavra com as vogais repetidas."""
    final_word = ""
    for letter in word:
        if letter.lower() in "aeiouãõâôêáéíó":
            final_word = letter * 2
        else:
            final_word = letter
    return final_word

print(repete_vogal("banana"))
