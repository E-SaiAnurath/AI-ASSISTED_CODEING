"""
Task 3: Modular string reversal using a user-defined function.

This file provides a reusable `reverse_string` function that returns the
reversed version of its input. The main block demonstrates usage and runs
simple sample tests.
"""

def reverse_string(s):
    """Return the reversed copy of the input string `s`.

    Uses Python slicing which runs in O(n) time and produces a new string.
    This function is small and explicit so it can be imported and reused
    throughout an application where string reversal is needed.
    """
    return s[::-1]


if __name__ == "__main__":
    # Interactive usage
    user_input = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(user_input))

    # Sample test cases
    tests = [
        ("Hello World", "dlroW olleH"),
        ("abc123", "321cba"),
        ("", ""),
        ("a", "a"),
    ]

    print("\nRunning sample tests:")
    for i, (inp, expected) in enumerate(tests, 1):
        out = reverse_string(inp)
        status = "PASS" if out == expected else "FAIL"
        print(f"Test {i}: input={inp!r} expected={expected!r} got={out!r} -> {status}")
