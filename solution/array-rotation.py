n, k, q = [int(x) for x in input().strip().split(' ')]
arr = [int(x) for x in input().strip().split(' ')]


def rotate(arr, k):
    new_arr = [0] * n
    for i in range(n):
        new_idx = (i + k) % n
        new_arr[new_idx] = arr[i]
    return new_arr

new_arr = rotate(arr, k)
print(new_arr)
print('\n'.join(str(x) for x in new_arr[:q]))