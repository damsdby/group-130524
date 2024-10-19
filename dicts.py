import json
import csv

factory = {
    "It dep": 5,
    "Sales dep": 10,
    "Production dep": 55,
    "Law dep": 10,
    "Construction dep": 25
}


def make_json(data: dict, filepath: str = "factory.json"):
    """
    this func writes the dict to a json file
    :param data: dicr with department data
    :param filepath: name of the file where data is saved
    """
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


def get_json(filepath: str = "factory.json") -> dict:
    """
    this func read data from a json file and return it as a dict
    :param filepath: name of the json file to read
    :return: dict with department data
    """
    with open(filepath, "r") as f:
        return json.load(f)


def make_csv(data: dict, filename: str = "factory.csv"):
    """
    this func writes the dict to a csv file
    :param data: dict with department data
    :param filename: name of the file where data is saved
    """
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["dep", "workers"])
        writer.writerows(data.items())


def get_csv(filepath: str = "factory.csv") -> dict:
    """
    this func reads data from a csv file and return it as a dict
    :param filepath: name of the csv file to read
    :return: dict with department data
    """
    with open(filepath, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        return {row[0]: int(row[1]) for row in reader}


factory["It dep"] = 7
factory["New dep"] = 8
del factory["Sales dep"]

make_json(factory)
make_csv(factory)

dep_workers_json = sum(get_json().values())
dep_workers_csv = sum(get_csv().values())

print(dep_workers_json)
print(dep_workers_csv)
print(factory)
