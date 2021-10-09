opcoes = list(map(int, input().split()))

resp = "N"
for idx in range(len(opcoes)):
    next_val_idx = idx + 1
    prev_val_idx = idx - 1
    if next_val_idx < len(opcoes):
        next_val = opcoes[next_val_idx]
    else:
        next_val = opcoes[0]

    if prev_val_idx >= 0:
        prev_val = opcoes[prev_val_idx]
    else:
        prev_val = opcoes[len(opcoes) - 1]


    val = opcoes[idx]

    if val == next_val or val == prev_val:
        resp = "S"
        break

    if val == abs(next_val + prev_val) or val == abs(next_val - next_val):
        resp = "S"
        break


print(resp)




