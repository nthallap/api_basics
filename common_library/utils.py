from pathlib import Path
import csv

BASE_PATH = Path(__file__).parent.parent
csv_path = BASE_PATH.joinpath('test_data').joinpath("data.csv")


def read_csv(file_path):
    emp_data = []
    with open(file_path, 'r') as fp:
        data = csv.reader(fp)
        next(data)
        for i in data:
            emp_data.append(i)
        return emp_data


def get_test_data():
    return read_csv(csv_path)


if __name__ == "__main__":
    print(get_test_data())
    print(BASE_PATH, csv_path)
