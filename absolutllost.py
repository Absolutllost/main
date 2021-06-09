#testfile.txt
def count_words(path):
    with open(path, "r") as f:
        words = len(f.read().split(" "))
    return words

def count_caracter(path):
    with open(path, "r") as f:
        #characters als die Länge des ausgelesenen strings ohne Zeilenumsprung und Leerzeichen
        caracters = len(f.read().replace("\n", "").replace(" ", ""))
    return caracters

def count_lines(path):
    with open(path, "r") as f:
        lines = len(f.readlines())
    return(lines)

def count_words_from_line(path, line):
    with open(path, "r") as f:
        words = len(f.readlines()[line-1].split(" "))
    return words

def count_sentences(path):
    with open(path, "r") as f:
        content = f.read().replace("!", ".").replace("?", ".")
        if "..." in content:
            content.replace("...", "")
        if ".." in content:
            content.replace("..", "")
        sentences = content.count(".")
    return sentences

def count_quotes(path):
    with open(path, "r") as f:
        content = f.read().replace("“","\"").replace("”", "\"")
        quotes = content.count("\"")/2
    return int(quotes)

def count_character_all(path):
    with open(path, "r") as f:
        #chars als die Länge des Strings ohne Zeilenumbruch
        chars = len(f.read().replace("\n", ""))
    return chars

print(count_quotes("testfile.txt"))
