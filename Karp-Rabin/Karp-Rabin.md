# Karp-Rabin

Algorithm for exact search of a pattern P in a text T, it is probabilistic because the use of hash function cannot ensure the exact search.

## How it works
It calculate the hash value of the pattern, iterate from the starting of the string then calculate the hash value of the current substring having length m.
If the hash value of the current substring and the pattern are same check if the substring is same as the pattern.
If they are same, store the starting index as a valid answer. Otherwise, continue for the next substrings.
Return the starting indices as the required answer.

## Requirements
This program use only the basic function of python and the built-in library os

## Parameters
The program doesn't require any parameter, pattern and text can be set in the txt files

```
karp-rabin.py
```

## Time
The average time is O(n+m) and the worst time in O(n*m), where n is equal to the lenght of the text and m is equal to the lenght of the pattern