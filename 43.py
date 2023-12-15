def read_file_to_array(file_path: str) -> list:
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data = list(map(int, [row.strip() for row in file]))
    return file_data


if __name__ == "__main__":
    data = read_file_to_array("files/43.txt")
    counter = 0
    min = float("inf")
    min_element = float("inf")

    for num in data:
        if num < min_element and abs(num) % 10 == 5 and len(str(num)) == 3:
            min_element = num

    for i in range(len(data) - 1):
        if (len(str(data[i])) == 3) and (len(str(data[i])) != 3) or ((len(str(data[i + 1])) == 3) and (len(str(data[i])) != 3)) and ((data[i] + data[i + 1]) % min_element == 0):
            counter += 1
            if data[i] + data[i + 1] < min:
                min = data[i] + data[i + 1]

    print(counter, min)
            
