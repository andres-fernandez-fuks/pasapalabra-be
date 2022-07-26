import io

FILE_NAME = 'scores.csv'

def get_data():
    data = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            data.append(line.strip().split(","))
    return data

def add_data(data):
    current_data = get_data()
    current_data.append(data)
    data = sorted(current_data, key=lambda x: (-int(x[1]), int(x[2])))[:10]
    with open(FILE_NAME, "w") as f:
        for line in data:
            f.write(",".join(line) + "\n")

def update_log(log_data):
    with io.open("log.txt", "a", encoding="utf-8") as f:
        for key in log_data:
            f.write(f'{key}: {log_data[key]}' + "\n")