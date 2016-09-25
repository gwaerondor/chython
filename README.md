# Chython - Python in Chinese
## About
This is a hackathon project in which I try to make a "natural programming language" make sense even if your native language does not happen to be English.

- In the scope of the hackathon project: Make it possible to write code in Chinese and run it.
- Not in the scope of the hackathon project: Make the Chinese code compile natively.

## Limitations
As this project was written over a very short time, there are plenty of limitations and shortcomings.

- The "build script" is horrible and assumes that you have the same file structure I did.
- Only a tiny subset of the Python language with all of its standard library has been translated.
- Some of the Chinese grammar is weird because I focused on making it work with Chinese characters, rather than making it work with Chinese grammar. Therefore some keywords are very awkward, because they have been shoe-horned to fit the same word order as in English so that the source can be translated "word by word". I'd like to switch around the word order in Chinese to make it sound less stilted in the future.

## Running it
- A python script is used to translate the source code to another separate source file which does not contain Chinese characters.
- UTF8 ordinal numbers are used to rename variables that are not Python keywords so there should not be any collisions.
- The python script reads the Chinese Python source file and translates it word-by-word.
- A new file that has the same file name as the Chinese source is created and output to the same directory with the file ending .translated.py. This new source file is run with python as normal.
- I recommend that you use the .chy file ending for Chinese source code. This is completely optional but I like it. :)