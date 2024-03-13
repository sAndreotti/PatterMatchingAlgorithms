# Z-Algorithm

Algorithm for exact search of a pattern P in a text T, using the border of a string it calculate a Array Z wich contains that values

## How it works
Similar to the other algorithms it uses the concept of border of a string wich is the longest prefix taht occurs also as suffix of the same string. In the first steps the Z-algorithm takes the pattern and the string, join them with a character that is not in the alphabet (in the example i've used $), than calculate the Z array as written before, when the value of z is equal to the length of the pattern we have a occurence

## Requirements
This program use only the basic function of python and the built-in library os


## Parameters
The program doesn't require any parameter, pattern and text can be set in the txt files

```
z-al.py
```

## Time
O(n+m), where n is equal to the lenght of the text and m is equal to the lenght of the pattern