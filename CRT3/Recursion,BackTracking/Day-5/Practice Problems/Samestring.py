def is_same(s1,s2):
    if s1=="" and s2=='':
        return True 
    if s1=="" or s2=="":
        return False
    if s1[0] == s2[0]:
        return True
    
    return is_same(s1[1:],s2[1:])
    
    

string1=input()
string2=input()
print(is_same(string1,string2))