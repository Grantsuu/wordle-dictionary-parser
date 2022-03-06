import json, time
from wordfreq import zipf_frequency

start_time = time.time()

f = open('./data/5_letters.json')

data = json.load(f)

normal_words = []
hard_words = []

#print(zipf_frequency('copts', 'en'))

for word in data:
    if zipf_frequency(word, 'en') < 2.5:
        hard_words.append(word)
    else:
        normal_words.append(word)

json_object1 = json.dumps(hard_words, indent = 4)
json_object2 = json.dumps(normal_words, indent = 4)

with open("./data/5_letters_hard.json", "w") as outfile:
    outfile.write(json_object1)

with open("./data/5_letters_normal.json", "w") as outfile:
    outfile.write(json_object2)

print("--- %s seconds ---" % (time.time() - start_time))