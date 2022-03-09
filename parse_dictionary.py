import json, time, sys, argparse
from wordfreq import zipf_frequency

def main (args):
    parser = argparse.ArgumentParser(description="Outputs a .json file of words based on length and word frequency from a dictionary .json file.")
    parser.add_argument('-i', '--input', required=True,
                        help="Input file (.json dictionary). Required")
    parser.add_argument('-o', '--output', required=True,
                        help="Output file directory. Required")
    parser.add_argument('-fn', '--filename', default='letters',
                        help="Output file name.")
    parser.add_argument('--min', type=int, default=4,
                        help="Minimum word length to be parsed into a file.")
    parser.add_argument('--max', type=int, default=11,
                        help="Maximum word length to be parsed into a file.")
    parser.add_argument('-t', '--threshold', type=float, default=2.5,
                        help="Zipf frequency threshold to use if parsing out hard words.")
    parser.add_argument('-l', '--lang', default='en',
                        help="language of the word being checked (default: english 'en')")
    parser.add_argument('-c', '--combine', action='store_true',
                        help="Parse out words of same length into single file. I.e. don't parse out 'hard' words.")
    args = parser.parse_args()

    start_time = time.time()

    f = open(args.input)
    data = json.load(f)

    for i in range(args.min, args.max + 1):
        normal = []
        hard = []
        for word in data.keys():
            # Parse out invalid words (contains a " " or "-")
            if len(word) is i and " " not in word and "-" not in word:
                if args.combine:
                    normal.append(word)
                else:
                    if zipf_frequency(word, args.lang) >= args.threshold:
                        normal.append(word)
                    else:
                        hard.append(word)
        if args.combine:
            with open(args.output + str(i) + "_" + args.filename + ".json", "w") as outfile:
                outfile.write(json.dumps(normal))
        else:
            with open(args.output + str(i) + "_" + args.filename + "_normal.json", "w") as outfile:
                outfile.write(json.dumps(normal))
            with open(args.output + str(i) + "_" + args.filename + "_hard.json", "w") as outfile:
                outfile.write(json.dumps(hard))

    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == "__main__":
   main(sys.argv[1:])

