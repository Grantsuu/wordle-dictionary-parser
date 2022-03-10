# wordle-dictionary-parser
## Usage
Includes usage and examples of included scripts.
### **parse_dictionary.py**
Parses out and separates words based on lengths and then writes them to .json files.
### Input
`parse_dictionary.py` expects a dictionary .json file as an input. The dictionary .json file contains a single JSON object which is a series of key/value pairs where the **KEY** contains the word and the **VALUE** contains the definition of that word. It resides, by default, in the `input` directory.
```
{
    "WORD1": "DEFINITION1",
    "WORD2": "DEFINITION2",
    "WORD3": "DEFINITION3",
    ...
}
```
For a good dictionary source see: https://github.com/matthewreagan/WebstersEnglishDictionary
#### Usage
`usage: parse_dictionary.py [-h] -i INPUT -o OUTPUT [-fn FILENAME] [--min MIN] [--max MAX] [-t THRESHOLD] [-c]`
```
Outputs a .json file of words based on length and word frequency from a dictionary .json file.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file (.json dictionary). Required
  -o OUTPUT, --output OUTPUT
                        Output file directory. Required
  -fn FILENAME, --filename FILENAME
                        Output file name.
  --min MIN             Minimum word length to be parsed into a file.
  --max MAX             Maximum word length to be parsed into a file.
  -t THRESHOLD, --threshold THRESHOLD
                        Zipf frequency threshold to use if parsing out hard words.
  -l LANG, --lang LANG  language of the word being checked (default: english 'en')
  -c, --combine         Parse out words of same length into single file. I.e. don't parse out 'hard' words.
```
#### Examples
```
python3 parse_dictionary.py -i ./input/dictionary.json -o ./output/
```
Output files:
- 4_letters_hard.json
- 4_letters_normal.json
- 5_letters_hard.json
- 5_letters_normal.json
<br />**...**
- 11_letters_hard.json
- 11_letters_normal.json
### **frequency.py**
Utility script to look up the zipf frequency of a word quickly.
#### Usage
`frequency.py [-h] [-l LANG] [-L LIST] [-m MIN] [-wf] W [W ...]`
```
Check a single word's or multiple words frequency. Default uses Zipf.

positional arguments:
  W                     word(s) to check the frequency of

optional arguments:
  -h, --help            show this help message and exit
  -l LANG, --lang LANG  language of the word being checked (default: english 'en')
  -L LIST, --list LIST  list of frequencies to use (default: 'best')
  -m MIN, --min MIN     If the word is not in the list or has a frequency lower than minimum, return
                        minimum instead (default: 0.0)
  -wf, --wfreq          Use the word frequency function instead (default is zipf)

See Wordfreq's usage here: https://pypi.org/project/wordfreq/
```
#### Examples
Default Usage
```
% python3 frequency.py example
EXAMPLE zipf: 5.27
```
Using word frequency
```
% python3 frequency.py -wf example
EXAMPLE wordf: 0.000186
```
The works
```
% python3 frequency.py -l 'en' -L small -m 0.0 -wf example
EXAMPLE wordf: 0.000186
```
