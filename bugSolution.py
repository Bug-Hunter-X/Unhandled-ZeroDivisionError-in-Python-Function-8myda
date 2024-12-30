def function_with_uncommon_bug(x):
    try:
        if x == 0:
            return 0
        else:
            return 1 / x
    except ZeroDivisionError:
        return float('inf')  # Or handle the error differently

# This will now return inf instead of raising an exception
result = function_with_uncommon_bug(0) 