def checkVowel(s,v,c):
    if len(s) == 0: return v>c
    if s[0] in ['a','e','i','o','u','A','E','I','O','U']:
        return checkVowel(s[1:], v+1,c)
    else:
        return checkVowel(s[1:], v, c+1)
print(checkVowel("Otaviommmm",0,0))