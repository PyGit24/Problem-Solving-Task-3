# Python program to print duplicates from 3 given list of integers
dlista = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
unilista = [] 
duplista = []
dlistb = [1, 2, 3, 5, 1, 1, 2, 5, 3, 7, 8, 9, 9]
unilistb = []
duplistb = []
dlistc = [2, 1, 2, 3, 4, 5, 1, 7, 8, 9, 9]
unilistc = []
duplistc = []
dlistd=duplista.copy()
dlistd=duplistb.copy()
dlistd.extend(dlistb)
unilistd =unilista.copy()
unilistd=unilistb.copy()
unilistd.extend(unilistc) 
duplistd = []
 
for i in dlista:
    if i not in unilista:
        unilista.append(i)
    elif i not in duplista:
        duplista.append(i)
for j in dlistb:
    if j not in unilistb:
        unilistb.append(j)
    elif i not in duplistb:
        duplistb.append(j)
for k in dlistc:
    if k not in unilistc:
        unilistc.append(k)
    elif i not in duplistc:
        duplistc.append(k)
for l in dlistd:
    if l not in unilistd:
        unilistd.append(l)
    elif l not in duplistd:
        duplistd.append(l)
print("\tProgram to find the duplicate list")
print("The First list is:",dlista)
print("The Duplicates present in First list are:", duplista)
print("The Unique Value present in First list are:", unilista)
print("\nThe Second list is:",dlistb)
print("The Duplicates present in Second list are:", duplistb)
print("The Unique Value present in Second list are:", unilistb)
print("\nThe Third list is:",dlistc)
print("The Duplicates present in Third list are:", duplistc)
print("The Unique Value present in Third list are:", unilistc)
print("\nThe Duplicates present in Three list are:", duplistd)
print("The Unique Value present in Three list are:", unilistd)