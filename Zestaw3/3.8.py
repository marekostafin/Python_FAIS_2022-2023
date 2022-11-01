seq1 = input()
seq2 = input()
l0 = []
l1 = []
l2 = []

for i in range(0, len(seq1)):
    l0.append(seq1[i])

for j in range(0, len(seq2)):
    if seq2[j] in l0:
        if not seq2[j] in l1:
            l1.append(seq2[j])

print("(a): {}".format(l1))

for k in range(0, len(seq1)):
    if not seq1[k] in l2:
        l2.append(seq1[k])

for m in range(0, len(seq2)):
    if not seq2[m] in l2:
        l2.append(seq2[m])

print("(b): {}".format(l2))