# DICTIONARIES
# Dictionaries are written with curly brackets, and have keys and values.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""
student_info = {
    "name": "Dele",
    "age": 20,
    "class": "11`"
}
print(student_info["name"])
"""

# DICTIONARY METHODS
# clear() - Removes all the elements from the dictionary
# copy() - Returns a copy of the dictionary
# fromkeys() - Returns a dictionary with the specified keys and value
# get() - Returns the value of the specified key
# items() - Returns a list containing a tuple for each key value pair
# keys() - Returns a list containing the dictionary's keys
# pop() - Removes the element with the specified key
# popitem() - Removes the last inserted key-value pair
# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

# Creating dictionaries within a list
"""
ec2_instances_info = [
    {
        "id": "instance-001",
        "type": "t2.micro",
    },
    {   "id": "instance-002",
        "type": "t2.medium",
    },
    {   "id": "instance-003",
        "type": "t2.large",
    }
]

print(ec2_instances_info[2]["id"])
"""
import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_detail = response.json() 

#print(complete_detail[0]["user"]["login"])
for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])