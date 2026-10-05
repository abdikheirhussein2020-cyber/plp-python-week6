# PLP Python Week 6 - Safe Functions and Exception Handling

## Files Included

* `safe_tools.py`: Contains functions that safely handle potential division, type conversion, and key lookup errors using `try...except` blocks.
* `unbreakable.py`: A script that imports and executes the safe functions to demonstrate crash-free execution.
* `README.md`: Provides an overview of the assignment, the files included, and the reflection answer.

## Reflection Question

### Why can the `if` check not catch "abc" on its own?

An `if` check can check whether a string consists only of numeric digits, such as `"123"`, but it does not perform the actual integer conversion. When Python tries to convert `"abc"` using `int()`, it raises a `ValueError`. Using `try...except` allows Python to attempt the conversion and gracefully handle the error when the input is not a valid number.
