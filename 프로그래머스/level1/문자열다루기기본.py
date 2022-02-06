def solution(s):
    return (len(s) == 4 or len(s) == 6) and all([i in '1234567890' for i in s])

# def solution(s):
#     try:
#         int(s)
#     except:
#         return False
#     return len(s) == 4 or len(s) == 6