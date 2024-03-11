# Knuth-Morris-Pratt

Algorithm for exact search of a pattern P in a text T, it preprocess the pattern using a prefix function.

## How it works
It calculate a fialure function to optimize search, it can bee seen in the function "preprocessing", after the calculus the real serch program start and look for every occurency in the text

## Requirements
This program use only the basic function of python and the built-in library os


## Parameters
The program doesn't require any parameter, pattern and text can be set in the txt files

```
kmp.py
```

## Time
O(n+m), where n is equal to the lenght of the text and m is equal to the lenght of the pattern