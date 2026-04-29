arr = input()
ast = list(map(str, arr.strip()))
rajer = 0
for i in range(len(arr)):
    if arr[i:i+2] == '()':
        print(1)
        rajer += 1
        ast.pop(i+1)
        ast.pop(i)
        print()
print(ast)