def read_file_to_array(file_path: str) -> list:
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data = list(map(int, [row.strip() for row in file]))
    return file_data


if __name__ == "__main__":
    data = read_file_to_array("files/36.txt")
    counter = 0
    max = float("-inf")
    max_element = float("-inf")

    for num in data:
        if num > max_element and abs(num) % 10 == 3:
            max_element = num
    max_element = max_element ** 2

    for i in range(len(data) - 1):
        if ((abs(data[i]) % 10 == 3 and abs(data[i + 1]) % 10 != 3) or (abs(data[i + 1]) % 10 == 3 and abs(data[i]) % 10 != 3)) and data[i] ** 2 + data[i + 1] ** 2 >= max_element:
            counter += 1
            if data[i] + data[i + 1] > max:
                max = data[i] + data[i + 1]

    print(counter, max)
            
