from json import dumps,loads

def dtj(data):
    #dictinory to json data as string
    try:
        return dumps(data)
    except:
        return False

def jtd(data):
    #json string into dictinory
    try:
        return loads(data)
    except:
        return False
