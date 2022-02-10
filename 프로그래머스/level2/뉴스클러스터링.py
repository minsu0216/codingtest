import re

def solution(str1, str2):
    
    str1 = [str1[i:(i+2)] for i in range(len(str1)-1)]
    str2 = [str2[i:(i+2)] for i in range(len(str2)-1)]
    
    set1 = [s.lower() for s in str1 if re.findall('[a-zA-Z]{2}', s)]
    set2 = [s.lower() for s in str2 if re.findall('[a-zA-Z]{2}', s)]
    
    if not set1 and not set2: return 65536

    set1_copy = set1.copy()
    set2_copy = set2.copy()
    set_and = []
    for s1 in set1:
        if s1 in set2_copy:
            set_and.append(s1)
            set1_copy.remove(s1)
            set2_copy.remove(s1)
    
    n_and = len(set_and)
    n_or = len(set1_copy) + len(set2_copy) + len(set_and)
    
    return int(n_and/n_or * 65536)