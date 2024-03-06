def binary_search(arr, low, high, tree_need):
    saw_height = int(low + (high - low) / 2)
    need = cut_tree(arr, saw_height)
    if low > high:
        return saw_height

    if need == tree_need:
        return saw_height
    elif need < tree_need:
        return binary_search(arr, low, saw_height - 1, tree_need)
    else:
        return binary_search(arr, saw_height + 1, high, tree_need)


def cut_tree(arr, saw_height):
    len_tree = 0
    for i in arr:
        if i - saw_height > 0:
            len_tree += i - saw_height
    return len_tree


n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

print(binary_search(tree, 0, max(tree), m))