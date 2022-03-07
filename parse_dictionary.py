import json, time
from wordfreq import zipf_frequency

start_time = time.time()

dict_file = "./data/dictionary_compact.json"
output_directory = "./data/"
min_length = 4
max_length = 11
zipf_threshold = 2.5

f = open(dict_file)

data = json.load(f)

for i in range(min_length, max_length + 1):
    normal = []
    hard = []
    for word in data.keys():
        # Parse out invalid words (contains a " " or "-")
        if len(word) is i and " " not in word and "-" not in word:
            if zipf_frequency(word, 'en') >= zipf_threshold:
                normal.append(word)
            else:
                hard.append(word)
    with open(output_directory + str(i) + "_letters_normal.json", "w") as outfile:
        outfile.write(json.dumps(normal))
    with open(output_directory + str(i) + "_letters_hard.json", "w") as outfile:
        outfile.write(json.dumps(hard))

print("--- %s seconds ---" % (time.time() - start_time))