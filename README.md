# WritingBuddy

A small scale commandline program for generating random text.

---

## Usage

Use the code with following command.
```
writingbuddy.py "path to datafile" "amount of generated words" "cleaner file"
```
A more concrete example.
```
writingbuddy.py D:\users\username\path\to\file.txt 30 D:\user\username\path\to\file.txt
```

Example of proper datafile and cleaner file can be found from ```files``` folder.  
The Cleaner file is an optional argument.

---

## Requirements

[python 3.7 or newer](https://www.python.org/), might work with older versions, but not tested.  
[numpy library for python](https://numpy.org/)

I might make setup file for python later.

---

## Why is this not an executable file?

Because I am lazy, deal with it.

---

## Known Issues

The program crashes if it doesn't find next word in the Markov Chain.

Formatting of the output is pretty obnoxious.