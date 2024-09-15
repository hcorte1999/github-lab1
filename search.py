import json

def search_json(json_data, search_string):
    results = []

    # Place your search code here
    # you will have to loop through the json_data file you created earlier

    for user_data in json_data:
        if search_string in user_data:
            results.append(user_data)
        elif search_string in user_data.values():
            results.append(user_data)
            

    # finally you can store the match in the result list and return it
    return results