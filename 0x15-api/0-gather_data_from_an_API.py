#!/bin/env/python3
"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

if __name__ == '__main__':

    from requests import get
    from sys import argv
    
    

    employer_id = argv[1]
    apiurl = "https://jsonplaceholder.typicode.com/users/"

    if int(employer_id):
        payload = {'userId': employer_id}
        response = get(apiurl + "todos", params=payload)
        json_response = response.json()
        # All user info fetching
        response_usr = get(apiurl + "users")
        usr_json_response = response_usr.json()
        # Brings user name
        for user in usr_json_response:
            if user.get('id') == int(employer_id):
                name = user.get('name')
        # List with done tasks
        mydone_list = [task for task in json_response
                       if task.get('completed') is True]
        # print(mydone_list)
        print("Employee {} is done with tasks({}/{}):".
              format(name, len(mydone_list), len(json_response)))
        for task in mydone_list:
            print("\t {}".format(task.get('title')))
