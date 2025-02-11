import os
#print(os.environ)

env_var = ['OS', 'PATH', 'USERPROFILE', 'HOMEPATH', 'NUMBER_OF_PROCESSORS']

for key in env_var:
    #for key, val in os.environ.items():
    if key in os.environ:
        print(f"{key} => {os.environ.get(key)[:80]}")
    else:
        "Key not found"

#print("Path is: ", os.environ.get('PATH'))
#print("User Profile: ", os.environ.get('USERPROFILE'))
#print("Homepath: ", os.environ.get('HOMEPATH'))
#print("Number of Processors", os.environ.get('NUMBER_OF_PROCESSORS'))