def solution(clothes):
    answer = 1
    cloth_category = dict()
    for cloth_name, cloth_type in clothes:
        if cloth_type in cloth_category.keys():
            cloth_category[cloth_type].append(cloth_name)
        else:
            cloth_category[cloth_type] = [cloth_name]
    for cloth_names in cloth_category.values(): answer *= (len(cloth_names)+1)
    answer -= 1
    return answer


examples = [
    [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],
    [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]],
]

for example in examples:
    print(solution(example))