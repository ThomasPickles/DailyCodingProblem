from string import ascii_lowercase
import math
from typing import Set
from collections import defaultdict

letters = defaultdict(lambda: '')
for index, letter in enumerate((ascii_lowercase)):
    letters[index+1]=letter # list must be one-indexed not zero-indexed

def get_decoding(code: int) -> Set[str]:
    digits = 1 + math.floor(math.log(code, 10))
    s = set()
    if digits <= 0:
        return s
    if digits <= 2:
        if letters[code]:
            s.add(letters[code])
    if digits > 1:
        all_but_last, last = code // 10, code % 10 
        for _, prefix in enumerate(get_decoding(all_but_last)):
            for _, suffix in enumerate(get_decoding(last)):
                s.add(prefix + suffix)
    if digits > 2:
        all_but_last_two, last_two = code // 100, code % 100
        for _, prefix in enumerate(get_decoding(all_but_last_two)):
            for _, suffix in enumerate(get_decoding(last_two)):
                s.add(prefix + suffix)
    return s


    
print(get_decoding(11135))
