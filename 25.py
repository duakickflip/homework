def read_file_to_array(file_path: str) -> list:
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data = list(map(int, [row.strip() for row in file]))
    return file_data


if __name__ == "__main__":
    data = read_file_to_array("files/25.txt")
    counter = 0
    max = float("-inf")

    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
        if (data[i] - data[j]) % 36 == 0 and (data[i] % 13 == 0 or data[j] % 13 == 0):
            counter += 1
            if data[i] - data[j] > max:
                max = data[i] - data[j]

    print(counter, max)
            
