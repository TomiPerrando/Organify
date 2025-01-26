
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
    elements["element_id"] = id
    elements["element_type"] = type
    elements["element_name"] = name
    elements["role"] = role
    elements["parent"] = parent
    elements["childs"] = childs
    return elements

print(add_element(elements, 1, "B", "A", "C", 3, [4,2]))
