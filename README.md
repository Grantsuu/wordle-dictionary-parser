# wordle-dictionary-parser
## Usage
Includes usage and examples of included scripts.
### **parse_dictionary.py**
Parses out and separates words based on lengths and then writes them to .json files.

### **frequency.py**
Utility script to look up the zipf frequency of a word quickly.
#### CLI
`frequency.py [-h] [-l LANG] [-L LIST] [-m MIN] [-wf] W [W ...]`
#### Usage
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
