def compute_cross_product(arr1, arr2):
    if len(arr1) != 3 or len(arr2) != 3:
        raise ValueError("Both input arrays must have exactly three elements.")
    result = [
        arr1[1] * arr2[2] - arr1[2] * arr2[1],
        arr1[2] * arr2[0] - arr1[0] * arr2[2],
        arr1[0] * arr2[1] - arr1[1] * arr2[0],
    ]
    return result

vec1 = [1, 2, 3]
vec2 = [4, 5, 6]
cross_product = compute_cross_product(vec1, vec2)
print("Cross Product:", cross_product)
