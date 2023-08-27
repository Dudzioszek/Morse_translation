# Morse Code Translator

## Description

This simple Python script allows users to input a string containing Latin alphabets or numbers and translates it into Morse code.

## Dictionary

The translation is based on the following Morse code dictionary:

| Character | Morse Code |
|-----------|------------|
| A         | .-         |
| B         | -...       |
| C         | -.-.       |
| D         | -..        |
| E         | .          |
| F         | ..-.       |
| G         | --.        |
| H         | ....       |
| I         | ..         |
| J         | .---       |
| K         | -.-        |
| L         | .-..       |
| M         | --         |
| N         | -.         |
| O         | ---        |
| P         | .--.       |
| Q         | --.-       |
| R         | .-.        |
| S         | ...        |
| T         | -          |
| U         | ..-        |
| V         | ...-       |
| W         | .--        |
| X         | -..-       |
| Y         | -.--       |
| Z         | --..       |
| 0         | -----      |
| 1         | .----      |
| 2         | ..---      |
| 3         | ...--      |
| 4         | ....-      |
| 5         | .....      |
| 6         | -....      |
| 7         | --...      |
| 8         | ---..      |
| 9         | ----.      |

## How to Use

1. Run the Python script.
2. Enter the text you want to translate into Morse code.
3. The script will output the translated Morse code.

## Example

**Input:** `HELLO`
**Output:** `.... . .-.. .-.. --- `

## Code

The code utilizes the above dictionary to map each character in the input string to its corresponding Morse code representation. Spaces in the input are preserved in the output.
