l = ['it', 'was', 'monday', 'morning', 'swaminathan', 'is', 'reluctant', 'to', 'open' ,'his', 'eyes' ,'he',
     'considared' ,'monday' ,'specially' ,'unpleasant' ,'in', 'the', 'calenfer' ,'after' ,'the' ,'delicious',
     'freedom', 'of', 'saturday' ,'and' ,'sunday', 'it' ,'was', 'difficult' ,'to' ,'get' ,'into', 'the',
     'monday' ,'mood', 'of' ,'work', 'and', 'discipline' ,'he', 'shudderd' ,'at' ,'the' ,'very' ,'thought',
     'of' ,'school' ,'the' ,'dismal' ,'yellow', 'building' ,'the' ,'fire' ,'eyed', 'vedanayagam' ,'his' ,'class',
     'teacher', 'and' ,'headmaster' ,'with' ,'his' ,'thin' ,'long', 'can']

s = set(l)

d = {}
max = 0
for i in s:
     d[i]=0

for i in l:
     d[i] += 1
     if (d[i]>max):
          max = d[i]
          answer_word = i

print(d)
print(max)
print(answer_word)
print(d['his'])