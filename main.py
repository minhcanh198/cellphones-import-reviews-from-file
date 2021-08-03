# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import csv
import datetime


def get_file_content(path, write_to):
    # Use a breakpoint in the code line below to debug your script.
    file = open(path, "r")

    row_number = 0
    for line in file:
        row_number += 1
        line_json = json.loads(line)
        print(line_json)
        row = list()
        row.append(row_number)
        row.append(None)
        row.append(None)
        row.append(line_json['productId'])
        row.append(line_json['content'])
        row.append(line_json['rating'])
        row.append(line_json['customerId'])
        row.append('accepted' if line_json['recordStatus'] == 'Active' else 'pending')
        row.append(None)
        row.append('cellphones')
        row.append(0)
        row.append('[]')
        row.append(format_timestamp(line_json['reviewedAt']))
        row.append(format_timestamp(line_json['reviewedAt']))
        row.append(None)
        write_to_csv(write_to, row)


def write_to_csv(file, data):
    with open(file, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)


def format_timestamp(time):
    return datetime.datetime.fromtimestamp(time / 1e3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_file_content('review_cps.txt', write_to='review_customer_service.csv')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
