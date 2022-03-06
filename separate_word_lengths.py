import json, time

start_time = time.time()

f = open('./data/valid_words.json')

data = json.load(f)

three_or_less_letters = []
four_letters = []
five_letters = []
six_letters = []
seven_letters = []
eight_letters = []
nine_letters = []
ten_letters = []
eleven_letters = []
twelve_or_more_letters = []

for word in data:
    if len(word) < 4:
        three_or_less_letters.append(word)
    elif len(word) is 4:
        four_letters.append(word)
    elif len(word) is 5:
        five_letters.append(word)
    elif len(word) is 6:
        six_letters.append(word)
    elif len(word) is 7:
        seven_letters.append(word)
    elif len(word) is 8:
        eight_letters.append(word)
    elif len(word) is 9:
        nine_letters.append(word)
    elif len(word) is 10:
        ten_letters.append(word)
    elif len(word) is 11:
        eleven_letters.append(word)
    else:
        twelve_or_more_letters.append(word)

json_object1 = json.dumps(three_or_less_letters, indent = 4)
json_object2 = json.dumps(four_letters, indent = 4)
json_object3 = json.dumps(five_letters, indent = 4)
json_object4 = json.dumps(six_letters, indent = 4)
json_object5 = json.dumps(seven_letters, indent = 4)
json_object6 = json.dumps(eight_letters, indent = 4)
json_object7 = json.dumps(nine_letters, indent = 4)
json_object8 = json.dumps(ten_letters, indent = 4)
json_object9 = json.dumps(eleven_letters, indent = 4)
json_object10 = json.dumps(twelve_or_more_letters, indent = 4)

with open("./data/3_letters_or_less.json", "w") as outfile:
    outfile.write(json_object1)

with open("./data/4_letters.json", "w") as outfile:
    outfile.write(json_object2)

with open("./data/5_letters.json", "w") as outfile:
    outfile.write(json_object3)

with open("./data/6_letters.json", "w") as outfile:
    outfile.write(json_object4)

with open("./data/7_letters.json", "w") as outfile:
    outfile.write(json_object5)

with open("./data/8_letters.json", "w") as outfile:
    outfile.write(json_object6)

with open("./data/9_letters.json", "w") as outfile:
    outfile.write(json_object7)

with open("./data/10_letters.json", "w") as outfile:
    outfile.write(json_object8)

with open("./data/11_letters.json", "w") as outfile:
    outfile.write(json_object9)

with open("./data/12_or_more_letters.json", "w") as outfile:
    outfile.write(json_object10)

print("--- %s seconds ---" % (time.time() - start_time))