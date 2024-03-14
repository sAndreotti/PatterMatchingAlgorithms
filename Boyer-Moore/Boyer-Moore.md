# Boyer-Moore

Algorithm for exact search of a pattern P in a text T, this implementation use the Bad Character Heuristic

## How it works
This algorithm work using the Bad Character Heuristic. The idea of the heuristic is simpple, the character of the text that have a mismatch with the current character of the pattern is a bad character. When there is a mismatch we shift the pattern unitl the mismatch become a match or the pattern moves past the mismatched character

## Requirements
This program use only the basic function of python and the built-in library os

## Parameters
The program doesn't require any parameter, pattern and text can be set in the txt files

```
boyer-moore.py
```

## Time
O(n*m), where n is equal to the lenght of the text and m is equal to the lenght of the pattern