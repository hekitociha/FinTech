def isAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    return s == t

s="abracadabra"
t="cadabraabra"
print(isAnagram(s, t))
