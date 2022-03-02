L = [ 'aabaabac' , 'cabaabca' , 'aaabbcba' , 'aabacbab' , 'acababba' ] 

s=input("Enter string with one * :")

i=0
check=0
while i<5:
    check=0
    m=0
    if s[m]==L[i][m]:
        check=1
        m=m+1
        while m<len(s)-1 and check==1:
            if s[m]!=L[i][m]:
                check=0
        m=m+1
    if check==1:
        print(L[i])
    i=i+1

if check==0:
    print('No Match')