# wordle-dictionary-parser
## Usage
Includes usage and examples of included scripts.
### **parse_dictionary.py**
Parses out and separates words based on lengths and then writes them to .json files.

### **zipf.py**
Utility script to look up the zipf frequency of a word quickly.
#### CLI
`python3 zipf -w <word>`
#### Arguments
`-w, --word`

The word to check the frequency of.
#### Example
```
% zipf.py -w sting
Zipf frequency for STING is: 3.8
```
