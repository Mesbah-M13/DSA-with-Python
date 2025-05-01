# s = 'abc'
# t = 'ahbgdc'


# def isSubsequence(self, s: str, t: str) -> bool:
#     S = len(s)
#     T = len(t)
#     if s == '': 
#         return True
#     if S > T: 
#         return False

#     j = 0
#     for i in range(T):
#         if t[i] == s[j]:
#             if j == S-1:
#                 return True
#             j += 1
        
#         return False
#       # Time: O(T)
#       # Space: O(1)
# result = isSubsequence(s,t)
# print(result)

s = 'abc'
t = 'ahbgdc'

def isSubsequence(s: str, t: str) -> bool:
    S = len(s)
    T = len(t)
    if s == '': 
        return True
    if S > T: 
        return False

    j = 0
    for i in range(T):
        if t[i] == s[j]:
            j += 1
            if j == S:
                return True
    return False  # <-- This should be **after the loop**

# Time: O(T)
# Space: O(1)

result = isSubsequence(s, t)
print(result)
