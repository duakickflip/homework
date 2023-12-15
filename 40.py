def read_file_to_array(file_path: str) -> list:
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data = list(map(int, [row.strip() for row in file]))
    return file_data


if __name__ == "__main__":
    data = read_file_to_array("files/40.txt")
    counter = 0
    max = float("-inf")
    min_element = float("inf")

    for num in data:
        if num < min_element and abs(num) % 10 == 3:
            min_element = num
    min_element = min_element ** 2

    for i in range(len(data) - 1):
        if (min(abs(data[i]), abs(data[i + 1])) % 10 == 3) and data[i] ** 2 + data[i + 1] ** 2 < min_element:
            counter += 1
            if data[i] + data[i + 1] > max:
                max = data[i] + data[i + 1]

    print(counter, max)
            
