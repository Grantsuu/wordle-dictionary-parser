import sys, argparse
from wordfreq import word_frequency, zipf_frequency

def main (args):
    parser = argparse.ArgumentParser(description="Check a single word's or multiple words frequency. Default uses Zipf.",
                                    epilog="See Wordfreq's usage here: https://pypi.org/project/wordfreq/")
    parser.add_argument('word', metavar='W', nargs='+',
                        help='word(s) to check the frequency of')
    parser.add_argument('-l', '--lang', default='en',
                        help="language of the word being checked (default: english 'en')")
    parser.add_argument('-L', '--list', default='best',
                        help="list of frequencies to use (default: 'best')")
    parser.add_argument('-m', '--min', type=float, default=0.0,
                        help="If the word is not in the list or has a frequency lower than minimum, return minimum instead (default: 0.0)")
    parser.add_argument('-wf', '--wfreq', action='store_true',
                        help="Use the word frequency function instead (default is zipf)")
    args = parser.parse_args()

    for word in args.word:
        if args.wfreq:
            print(word.upper(), "wordf:", word_frequency(word, args.lang, args.list, args.min))
        else:
            print(word.upper(), "zipf:", zipf_frequency(word, args.lang, args.list, args.min))

if __name__ == "__main__":
   main(sys.argv[1:])   
