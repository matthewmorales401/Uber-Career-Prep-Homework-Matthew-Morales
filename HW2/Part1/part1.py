class Tree(object):
    def __init__(self, root):
        self.root = root


class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


# Ex 1 Print Tree recursively

def printTree(node):
    if node is None:
        return
    printTree(node.left)
    print(node.data)
    printTree(node.left)


# Ex 2 Prints All Employees Iteratively


class OrganizationStructure(object):
    def __init__(self, ceo):
        self.employee = ceo

class Employee(object):
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.directReports = []

def printLevel(employees):
    if employees:
        level = [employees]
    while level:
        queue = []
        for employee in level:
            if employee.left:
                queue.append(employee.left)
            if employee.right:
                queue.append(employee.right)
        print("Name: " + employee.name + ", Title: " +  employee.title)
        level = queue


#Ex 3 Similar to ex 2, but just gauging the level depth:

class OrganizationStructure(object):
    def __init__(self, ceo):
        self.employee = ceo

class Employee(object):
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.directReports = []

def printNumberOfLevels(employees):
    number = 0
    if employees:
        level = [employees]
    while level:
        queue = []
        number += 1
        for employee in level:
            if employee.left:
                queue.append(employee.left)
            if employee.right:
                queue.append(employee.right)
        level = queue
    print(number)
