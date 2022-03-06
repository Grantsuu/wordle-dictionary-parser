import json, time

start_time = time.time()

f = open('./data/all_words.json')

data = json.load(f)

valid_words = []
invalid_words = []

for word in data:
    if " " in word or "-" in word:
        invalid_words.append(word)
    else:
        valid_words.append(word)

json_object1 = json.dumps(valid_words, indent = 4)
json_object2 = json.dumps(invalid_words, indent = 4)

with open("./data/valid_words.json", "w") as outfile:
    outfile.write(json_object1)

with open("./data/invalid_words.json", "w") as outfile:
    outfile.write(json_object2)

print("--- %s seconds ---" % (time.time() - start_time))