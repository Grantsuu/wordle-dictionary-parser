import json, time

start_time = time.time()

f = open('./data/dictionary_compact.json')

data = json.load(f)

json_object = json.dumps(data.keys(), indent = 4)

with open("./data/all_words.json", "w") as outfile:
    outfile.write(json_object)

print("--- %s seconds ---" % (time.time() - start_time))