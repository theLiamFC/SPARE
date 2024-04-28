import json

documentation = {}
documentation['spike'] = json.load(open("query_dict.json", "r"))
documentation['openmv'] = json.load(open("openMV_Doc.json", "r"))

def searchDoc(device,query):
    noResults = (
        "No available information on "
        + query
        + ". Query help to get a list of available modules."
    )

    helpSplit = query.split(" ")
    try:
        if helpSplit[0] == "help" and len(helpSplit) == 1:
            return documentation[device].keys()
        elif helpSplit[0] == "help" and len(helpSplit) > 1:
            return documentation[device][helpSplit[1]].keys()
    except KeyError as e:
        return noResults

    querySplit = query.split(".")
    for module in documentation[device]:
        if module == querySplit[0] and len(querySplit) == 1:
            return documentation[device][module]
        elif module == querySplit[0] and len(querySplit) > 1:
            for secondaryModule in documentation[device][module]:
                if secondaryModule == querySplit[1]:
                    return documentation[device][module][secondaryModule]

    return noResults

print(searchDoc('openmv','help audio'))
