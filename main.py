def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def wordcount():
    whole = f"{main()}"
    words = whole.split()
    return len(words)

def charactercount():
    whole = f"{main()}"
    characters = {}
    for character in whole:
        lowcharacter = character.lower()
        if not lowcharacter in characters:
            characters[lowcharacter] = 1
        else:
            characters[lowcharacter] += 1
    return characters

def printreport():
    a_list = []
    a_dict = charactercount()
    for character in a_dict:
        if character.isalpha():
            a_list.append({"character" : character, "num" : a_dict[character]})
            
    def sort_on(dict):
        return dict["num"]
    a_list.sort(reverse=True,key=sort_on)
    
    print(f"GREATEST REPORT ON THE BOOK: FRANKENSTEIN")
    print(f"The whole book was written in {wordcount()} words.")
    print(" ")
    for i in range(0,len(a_list)):
        b_dict = a_list[i]
        print(f"The '{b_dict["character"]}' character was found {b_dict["num"]} times")
    print("FINALLY FINISHED THIS TOOK ME 3 HOURS")

    

printreport()