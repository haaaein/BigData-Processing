import tree
f = open('lenses.txt')
lenses = [str.strip(inst).split('\t') for inst in f.readlines()]
lenseLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = tree.createTree(lenses, lenseLabels)
print(lensesTree)