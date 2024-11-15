X,Y = input().split()
rule = {
    'R': 'P', 'P': 'S', 'S': 'R'
}
if X == Y:
    print("NULL")
elif rule[X] == Y:
    print("Charan")
else:
    print("Vignesh")
