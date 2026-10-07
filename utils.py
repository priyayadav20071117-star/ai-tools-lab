"""A small collection of beginner-friendly utility functions."""


def is_palindrome(s):
    """Check whether a string reads the same forwards and backwards.

    Spaces, punctuation, and capital letters are ignored, so
    "A man, a plan, a canal: Panama" counts as a palindrome.

    Args:
        s: The text to check.

    Returns:
        True if the text is a palindrome, otherwise False.
    """
    # Keep only letters and numbers, and make them lowercase
    cleaned = ""
    for character in s:
        if character.isalnum():
            cleaned += character.lower()

    # Compare the cleaned text with its reverse
    return cleaned == cleaned[::-1]


def count_words(text):
    """Count how many words are in a piece of text.

    Words are groups of characters separated by spaces, tabs, or new lines.

    Args:
        text: The text to count words in.

    Returns:
        The number of words as an integer.
    """
    # split() with no arguments splits on any whitespace
    # and ignores extra spaces automatically
    words = text.split()
    return len(words)


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit.

    Formula: F = C * 9/5 + 32

    Args:
        c: The temperature in degrees Celsius.

    Returns:
        The temperature in degrees Fahrenheit.
    """
    return c * 9 / 5 + 32


# This block only runs when you execute this file directly
# (python utils.py). It is a quick way to try out the functions.
if __name__ == "__main__":
    print(is_palindrome("Racecar"))                         # True
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("Hello"))                           # False

    print(count_words("The quick brown fox"))               # 4
    print(count_words("  extra   spaces   here  "))         # 3

    print(celsius_to_fahrenheit(0))                         # 32.0
    print(celsius_to_fahrenheit(100))                       # 212.0