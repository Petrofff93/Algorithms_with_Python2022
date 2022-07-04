def vector_gen(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[idx] = num
        vector_gen(idx + 1, vector)


n = int(input())
vector = [0] * n
vector_gen(0, vector)
