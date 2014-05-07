s = 'eyghykwelffk'

curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    print( s[i],' ',curString[-1])
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest


def common(a,b):
    longest=''
    buffer=''
    k = 0
    while(k<len(a)):
        for l in range(len(a)):
            l2 = l+k+1
            if a[k:l2] in b:
                buffer = a[k:l2]
                if len(buffer)>len(longest):
                    longest = buffer
            else:
                break
        k += 1
    return longest

'''q1 = 'aalabckot'
q2 = ''.join(sorted(q1))
print q1,' ',q2
print common(q1,q2)'''


buff = ''.join(sorted(s))
print s,' ',buff
print 'Longest substring in alphabetical order is: {}'.format(common(s,buff))