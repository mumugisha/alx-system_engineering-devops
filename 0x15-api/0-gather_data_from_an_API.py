#!/usr/bin/python3
'''script returns information for a given employee ID
about his/her TODO list progress

Attrs:
    URL: endpoint to retrive the iformation from
'''
from requests.exceptions import HTTPError
from requests import get
import sys

URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    EMPLOYEE_ID = sys.argv[1]
    try:
        completed = 0
        user = get(f'{URL}/users/{EMPLOYEE_ID}').json()
        todos = get(f'{URL}/todos?userId={EMPLOYEE_ID}').json()
        for t in todos:
            if t.get('completed'):
                completed += 1
        print('Employee {} is done with tasks({}/{}):'
              .format(user.get('name'), completed, len(todos)))
        for t in todos:
            if t.get('completed'):
                print('\t '+t.get('title'))

    except HTTPError as http_err:
        print(http_err)
    except Exception as e:
        print(e)
