fn main() {
    let input: Vec<Vec<i32>> = include_str!("input.txt")
        .split("\n")
        .filter(|x| !x.is_empty())
        .map(|x| x.split("   ").map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>())
        .collect();

    let mut left_values: Vec<i32> = vec![];
    let mut right_values: Vec<i32> = vec![];

    for value in input {
        left_values.push(value[0]);
        right_values.push(value[1]);
    }

    left_values.sort();
    right_values.sort();

    let mut sum = 0;
    let mut part2_sum = 0;
    for i in 0..left_values.len() {
        sum += (left_values[i] - right_values[i]).abs();
        let part2_number = left_values[i];
        let occurrences = right_values.iter().filter(|x| **x == part2_number).count() as i32;
        part2_sum += part2_number * occurrences;
    }
    println!("{}", sum);
    println!("{}", part2_sum);
}
