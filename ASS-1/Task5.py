"""
Task 5: Two string-reversal approaches

Prompts (examples to feed Copilot):
- "Generate a loop-based string reversal implementation"
- "Provide a built-in slicing-based string reversal"
- "Explain differences between loop and slicing approaches"

This file contains:
- `reverse_loop(s)`: explicit loop-based reversal (O(n) time)
- `reverse_slice(s)`: slicing-based reversal using `s[::-1]` (O(n) time)

Both implementations return the reversed string.
"""

def reverse_loop(s):
    """Reverse string `s` using an explicit loop.

    Iterates the input string backwards and collects characters into a list,
    then joins them. This is O(n) time and O(n) memory.
    """
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return "".join(chars)


def reverse_slice(s):
    """Reverse string `s` using Python slicing (built-in).

    Very concise: returns `s[::-1]` which is implemented in C and is efficient.
    """
    return s[::-1]


if __name__ == "__main__":
    # Interactive demo
    inp = input("Enter a string to reverse: ")
    print("Loop-based reversal:", reverse_loop(inp))
    print("Slicing-based reversal:", reverse_slice(inp))

    # Sample tests
    tests = [
        ("Hello World", "dlroW olleH"),
        ("abc123", "321cba"),
        ("", ""),
        ("a", "a"),
    ]

    print("\nRunning sample tests:")
    for i, (t, expected) in enumerate(tests, 1):
        out_loop = reverse_loop(t)
        out_slice = reverse_slice(t)
        ok = out_loop == expected and out_slice == expected
        status = "PASS" if ok else "FAIL"
        print(f"Test {i}: input={t!r} loop={out_loop!r} slice={out_slice!r} -> {status}")
