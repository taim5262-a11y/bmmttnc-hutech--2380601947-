import itertools

ds = [1, 2, 3]
hoan_vi = list(itertools.permutations(ds))

print("Danh sách các hoán vị:")
for hv in hoan_vi:
    print(hv)