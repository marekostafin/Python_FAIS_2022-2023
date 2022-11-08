def odwracanie(L, left, right):
    while left < right:
        tmp = L[left]
        L[left] = L[right]
        L[right] = tmp
        left += 1
        right -= 1
    return L

def odwracanie_rekurencyjne(L, left, right):
    if left < right:
        tmp = L[left]
        L[left] = L[right]
        L[right] = tmp
        odwracanie_rekurencyjne(L, left+1, right-1)
    return L