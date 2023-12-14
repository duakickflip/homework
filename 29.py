def read_file_to_array(file_path: str) -> list:
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data = list(map(int, [row.strip() for row in file]))
    return file_data


if __name__ == "__main__":
    data = read_file_to_array("files/29.txt")
    counter = 0
    max = 0

    for i in range(2, len(data)):
        a = data[i]
        b = data[i - 1]
        c = data[i - 2]
        if a + b > c or b + c > a or a + c > b:
            counter += 1
            if a + b + c> max:
                max = a + b + c
            
    print(counter, max)