def sort_on(items):
    return items["num"]

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else: 
            char_dict[char] = 1     
    return char_dict

def get_sorted_dict(dict): 
    sorted_dict=[]
    for char in dict:
        if char.isalpha():
            new_dict={}
            new_dict["char"] = char
            new_dict["num"] = dict[char]
            sorted_dict.append(new_dict)
    sorted_dict.sort(reverse=True, key=sort_on)
    for i in range(0, len(sorted_dict)):
        print(sorted_dict[i]["char"] + ": " + str(sorted_dict[i]["num"]))
    print("============= END ===============")

