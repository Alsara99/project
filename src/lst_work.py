import re
from collections import Counter


def filter_lst_by_string(operations, string):
    result = []
    for operation in operations:
        for key, value in operation.items():
            key_search = re.search(string, key)
            value_search = re.search(string, str(value))
            if key_search or value_search:
                if operation not in result:
                    result.append(operation)

    return result


def count_operations_by_description(operations, descriptions):
    lst = []

    for operation in operations:
        if operation["description"] in descriptions:
            lst.append(operation["description"])

    result = Counter(lst)
    return result