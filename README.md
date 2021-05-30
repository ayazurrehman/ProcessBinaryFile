# Python Version - 3.9.5

# Steps to run

- keep the `my_file.bin` file in the same directory as the `process_binary_file.py` file
- run the `process_binary_file.py` using the above mentioned python version
- (optional) in order to use a different file, update the file path in `process_binary_file.py` at line number `70`

# Expected output

- Output will be printed to the screen or standard output device as follows -

```
    =====Example Output for humans:==========
    {5, 17}: ' world'
    {45, 54}: ' place'
    {6, 18}: 'world'
    {46, 55}: 'place'
    ======Output for binary file:============
    {5, 17}: 32, 119, 111, 114, 108, 100
    {45, 54}: 32, 112, 108, 97, 99, 101
    {6, 18}: 119, 111, 114, 108, 100
    {46, 55}: 112, 108, 97, 99, 101
```

# Assumptions

- File path is a valid file path that can be decoded to a valid string

# Objective

Develop a program

Input:

- path to binary file
- character length is 8bit, 16bit or 32bit
- optional length parameter

Output:
Show and count substring (space is not a delimiter, not even on ascii files), which occur more than once and are longer than an optional parameter (default 5).
This should also function efficiently with big files.

---

Example:
If the input is an ascii file and the character length a character:
"""
Hello world, this world is a really beautiful place. A place like home.
"""

Example Output for humans:
{5, 17}: ' world'
{6, 18}: 'world'
{45, 54}: ' place'
{46, 55}: 'place'

Output for binary file:
{5, 17}: [32, 119, 111, 114, 108, 100]
{6, 18}: [119, 111, 114, 108, 100]
{45, 54}: [32, 112, 108, 97, 99, 101]
{46, 55}: [112, 108, 97, 99, 101]
