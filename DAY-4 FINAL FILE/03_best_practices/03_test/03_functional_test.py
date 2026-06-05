"""
Functional Test:

Checking if a part of a program (or the entire subprogram) performs
the intended function according to the requirements.
"""

def is_palindrome(s):
    return s == s[::-1]

def test_is_palindrome():
    assert is_palindrome("racecar")
    assert not is_palindrome("package")
    assert not is_palindrome("A man a plan a canal Panama")
    print("All functional tests passed!")

test_is_palindrome()