# Happy Number Checker

This is a simple Python program that checks whether a given number is a **happy number** or not.

## 🤔 What is a Happy Number?

A **happy number** is a number that eventually reaches `1` when replaced by the sum of the squares of its digits repeatedly.

- If the process results in `1`, the number is happy.
- If it enters a cycle that does **not** include `1`, the number is **not** happy.

**Example:**

- Input: `19`
- Process: `1^2 + 9^2 = 82`, `8^2 + 2^2 = 68`, `6^2 + 8^2 = 100`, `1^2 + 0^2 + 0^2 = 1`
- Output: `19 is a happy number.`

- Input: `4`
- Process: `4^2 = 16`, `1^2 + 6^2 = 37`, `3^2 + 7^2 = 58`, `5^2 + 8^2 = 89`, `8^2 + 9^2 = 145`, `1^2 + 4^2 + 5^2 = 42`, `4^2 + 2^2 = 20`, `2^2 + 0^2 = 4`
- Output: `4 is not a happy number.`

## 🧮 How it works

The program:
1. Gets a number from the user.
2. Repeatedly replaces the number by the sum of the squares of its digits.
3. Stops when the number becomes `1` (happy) or `4` (known loop, unhappy).
4. Prints the process step-by-step.

## 🚀 How to run

Make sure you have Python installed, then run:

``` bash
python happy_number.py
```

## ✅ Sample Happy Numbers

1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100
## 📂 File Structure

```bash
happy_number.py        # Python file that checks for happy numbers
README.md              # This file
```
📌 This is a basic algorithm useful for learning number theory, loops, and digit manipulation in Python.

