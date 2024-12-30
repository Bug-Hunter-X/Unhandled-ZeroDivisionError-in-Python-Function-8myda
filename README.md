# Unhandled ZeroDivisionError in Python Function
This repository demonstrates an example of an unhandled ZeroDivisionError in a Python function.  The function `function_with_uncommon_bug` attempts to divide by zero, which causes an exception if not handled properly.

## Bug Description
The bug occurs when the input to `function_with_uncommon_bug` is 0. The function does not handle this case, leading to a `ZeroDivisionError`.  This is an uncommon bug because it highlights a specific instance of exception handling that is often overlooked.

## Solution
The solution involves adding a `try-except` block to handle the `ZeroDivisionError` gracefully. This prevents the program from crashing and allows for alternative behavior, such as returning a specific value or raising a custom exception.