def read_file_to_array(file_path: str) -> list:
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data = list(map(int, [row.strip() for row in file]))
    return file_data


if __name__ == "__main__":
    data = read_file_to_array("files/31.txt")
    counter = 0
    max = float("-inf")
    avg = sum([num for num in data if num > 0]) / len([num for num in data if num > 0])
    for i in range(len(data) - 1):
        if (data[i] % 3 == 0 or data[i + 1] % 3 == 0) and (data[i] < avg or data[i + 1] < avg):
            counter += 1
            if data[i] + data[i + 1] > max:
                max = data[i] + data[i + 1]
            
    print(counter, max)