function solution(clothes) {
    var answer = 1;
    var cloth_category = {
    };

    for (let i=0; i < clothes.length; i++) {
        let [cloth_name, cloth_type] = clothes[i];
        console.log(Object.keys(cloth_category));
        if (cloth_category[cloth_type] !== undefined) {
            cloth_category[cloth_type].push(cloth_name);
        }
        else {
            cloth_category[cloth_type] = Array(cloth_name);
        }
    }

    console.log(cloth_category);

    for (let [key, value] of Object.entries(cloth_category)) {
        answer *= (value.length + 1)
    }

    return answer - 1;
}

examples = [
    [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],
    [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]],
]

for (example of examples) {
    console.log(solution(example))
}