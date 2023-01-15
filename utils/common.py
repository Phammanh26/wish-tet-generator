def listComplementElements(list1, list2):
    storeResults = []
    for num in list1:
        if num not in list2: # this will essentially iterate your list behind the scenes
            storeResults.append(num)
    return storeResults