# wordle-dictionary-parser
## Usage
A little rough now but use the scripts on the files in order.
### dictionary_compact.json
Remove all of the definitions by just parsing out all of the keys.
```
python remove_definitions.py
```
### all_words.json
Separate all of the words into valid or invalid words (contains spaces " " or dashes "-").
```
python separate_valid_characters.py
```
### valid_words.json
Separate all of the remaining valid words into lists of words by length.
```
python separate_word_lengths.py
```
## Next Steps
Separate out each list of words into hard words based on word frequency.