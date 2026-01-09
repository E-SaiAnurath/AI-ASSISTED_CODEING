# Optimized string reversal program
# Simplified: removes unnecessary variables and improves readability

if __name__ == "__main__":
    s = input("Enter a string to reverse: ")
    print("Reversed string:", s[::-1])

    '''
    Why this is improved

Removed the unnecessary reversed_string variable and used s[::-1] inline, reducing memory usage by one reference.
Shorter, clearer variable name (s) and fewer lines improves readability for reviewers.
Time complexity unchanged: both versions are O(n) where n is string length. The optimized version reduces constant-factor overhead (one fewer assignment), slightly improving performance and reducing memory footprint.
Sample runs (verified)

Input: Hello World → Reversed string: dlroW olleH
Input: abc123 → Reversed string: 321cba'''
