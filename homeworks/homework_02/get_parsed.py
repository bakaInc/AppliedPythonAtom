import json
import csv


def check_csv(filestream):
    reader = csv.reader(filestream, delimiter="\t")
    data = []
    last = 0
    i = 0
    for row in reader:
        if not len(row):
            return False
        if (i and last is not len(row)):
            return False
        else:
            i += 1
        last = len(row)
        data.append(row)
    return data


def check_json(filestream):
    data = []
    try:
        data_json = json.load(filestream)
        data.append(list(data_json[0].keys()))
        for value in data_json:
            data.append(list(value.values()))
    except json.JSONDecodeError:
        filestream.seek(0)
        return False
    return data


def check_format(filestream):
    data_json = check_json(filestream)
    data_csv = check_csv(filestream)
    if data_json:
        return buffer_json
    elif data_csv:
        return buffer_tsv
    else:
        raise Warning
