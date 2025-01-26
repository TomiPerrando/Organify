
"""
members_type2 = {
    1: {
        "name": "member1",
        "id": 1,
        "role": "Director",
        "parent": 0,
        "childs": [2, 4]
    },
    2: {
        "name": "member1A",
        "id": 2,
        "role": "Manager",
        "parent": 1,
        "childs": [3]
    },
    3: {
        "name": "member1AA",
        "id": 3,
        "role": "Analyst",
        "parent": 2,
        "childs": []
        },
    4: {
        "name": "member1B",
        "id": 4,
        "role": "Manager",
        "parent": 1,
        "childs": []
       }          
}
"""

elements = {}

def add_element (elements, id, name, type, role, parent, childs):
    elements[id] = {}
    elements[id]["id"] = id
    elements[id]["element_type"] = type
    elements[id]["element_name"] = name
    elements[id]["role"] = role
    elements[id]["parent"] = parent
    elements[id]["childs"] = childs
    return elements

add_element(elements, 1, "B", "A", "C", 3, [4,2])
add_element(elements, 2, "E", "D", "F", 1, [90,23])
add_element(elements, 3, "E", "D", "F", 0, [1, 4])
print(elements)


def move_element (elements, moving, new_parent):
    old_parent = elements[moving]["parent"]
    elements[old_parent]["childs"].remove(moving)
    elements[moving]["parent"] = new_parent
    elements[new_parent]["childs"].append(moving)
    return elements

print (move_element(elements, 2, 3))

def delete_element (elements, id):
    del elements[id]
    return elements

print(delete_element(elements, 2))