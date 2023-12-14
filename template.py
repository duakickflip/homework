def read_file_to_array(file_path: str) -> list:
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data = list(map(int, [row.strip() for row in file]))
    return file_data


if __name__ == "__main__":
    data = read_file_to_array("files/.txt")
    counter = 0
    
    for i in range(len(data)):
        for j in range(len(data)):
            if :
            counter += 1

    print(counter)