#!/usr/bin/python3
"""
Using a REST API return information about an employee
"""
import sys
import requests
import csv


if __name__ == "__main__":
    user_id = sys.argv[1]
    csv_file = user_id + ".cvs"

    open_file = open(csv_file, 'w+')
    csv_writer = csv.writer(open_file, quoting=csv.QUOTE_ALL)

    user_response = requests.get("https://jsonplaceholder" +
                                 ".typicode.com/users?id=" + user_id)

    user_name = user_response.json()[0]["name"]
    user_username = user_response.json()[0]["username"]

    todos_response = requests.get("https://jsonplaceholder" +
                                  ".typicode.com/todos?userId=" + user_id)

    todos = todos_response.json()
    total_num_tasks = 0
    num_done_tasks = 0
    done_tasks = []
    for task in todos:
        if task["completed"] is True:
            num_done_tasks = num_done_tasks + 1
            done_tasks.append(task["title"])

        row = (user_id, user_username, str(task["completed"]), task["title"])
        csv_writer.writerow(row)

        total_num_tasks = total_num_tasks + 1

    open_file.close()

    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          num_done_tasks,
                                                          total_num_tasks))
    for task in done_tasks:
        print("\t {}".format(task))
