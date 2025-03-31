# Input Shuffler

This Python script takes two user inputs (either numbers or words), processes them into arrays, and combines them in an alternating pattern. If the arrays are of different lengths, the remaining elements from the longer array are appended to the end of the combined array.

## Features

- Accepts two inputs from the user.
- Supports both numbers and words as input.
- Converts numbers into an array of integers and words into an array of characters.
- Combines the two arrays in an alternating pattern.
- Handles inputs of different lengths gracefully.

## How to Use

1. Clone this repository or download the script.
2. Run the script using Python:
   ```sh
   python app.py
3.Follow the prompts:
  Enter either numbers (e.g., 12345) or words (e.g., hello) for the first input.
  Enter either numbers or words for the second input.
4.The script will output the combined array.

# Example
## Input:
Please enter either numbers or words: 12345
Please enter either numbers or words: abc

## Output
[1, 'a', 2, 'b', 3, 'c', 4, 5]

# Notes
 If the input is neither numbers nor words, the script will print an error message.
 Ensure you have Python installed to run the script.