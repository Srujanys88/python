def string_similarity(str1, str2):
    comp_len = len(str1) if len(str1)<len(str2) else len(str2)
    max_len  = len(str1) if len(str1)>len(str2) else len(str2)
    similarity = 0
    for i in range(comp_len):
        if(str1[i] == str2[i]):
            similarity += 1
    return similarity/max_len



ans = string_similarity("srujann","srujan")
print(ans*100)
