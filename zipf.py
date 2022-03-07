import sys, getopt
from wordfreq import zipf_frequency

def main (args):
    word = ''
    help_message = 'zipf.py -w <word>'
    try:
        opts, args = getopt.getopt(args,"hw:",["word="])
    except getopt.GetoptError:
        print (help_message)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (help_message)
            sys.exit()
        elif opt in ("-w", "--word"):
            word = arg
    print ('Zipf frequency for', word.upper(), 'is:', zipf_frequency(word, 'en'))

if __name__ == "__main__":
   main(sys.argv[1:])   
