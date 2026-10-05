# PLP Python Week 6 - Safe Functions and Exception Handling

## Files Included
* `safe_tools.py`: Contains functions that handle potential division, type conversion, and key lookup errors using `try...except` blocks.
* `unbreakable.py`: A script that imports and executes the safe functions to demonstrate crash-free execution.

## Reflection Question
### Why can the `if` check not catch "abc" on its own?
An `if` check can easily check if a string consists only of numeric digits (like `"123"`), but it fails to reliably detect complex numeric formats like floating-point decimals, negative numbers, or non-digit characters without complex regex. Using `try...except` allows Python to attempt the actual type conversion and gracefully handle any `ValueError` if the format is invalid.