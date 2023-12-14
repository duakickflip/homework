def read_file_to_array(file_path: str) -> list:
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data = list(map(int, [row.strip() for row in file]))
    return file_data


if __name__ == "__main__":
    data = read_file_to_array("files/27.txt")
    counter = 0
    max = float("-inf")

    for i in range(len(data) - 1):
        if (data[i] % 5 == 0 or data[i + 1] % 5 == 0) and ((data[i] + data[i + 1]) % 7 == 0):
            counter += 1
            if data[i] + data[i + 1] > max:
                max = data[i] + data[i + 1]
            
    print(counter, max)