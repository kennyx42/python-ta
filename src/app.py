import sys
import os

import argparse


def palindrome(s):
    s = s.replace(' ', '').lower()
    check_palindrome = list(s)
    reverse_s = ''.join(check_palindrome[::-1]) 
    if s == reverse_s:
        return(True)
    else:
        return(False)
    
    
def solution(s):
    return palindrome(s)



if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))
