import json


def count_space(line):
    return len(line) - len(line.lstrip())


def count_tab(line):
    no_space = count_space(line)
    if no_space % 2 == 0:
        return int(no_space / 2)
    else:
        return -1


class Node:
    def __init__(self, label, line, level=-2):
        self.willRemove = False

        self.line = line
        self.last_line = line
        self.childNodes = []
        self.level = level
        self.isActive = False

        if self.level == -2:
            self.level = count_tab(label)

        self.isValid = self.level != None
        self.label = label.strip()

    def add_children(self, child_node):
        self.childNodes.append(child_node)

    def encode(self):
        # use this function to support JSON lib serialization
        # return self.__dict__
        return {"line": self.line, "last_line": self.last_line, "level": self.level, "isActive": self.isActive,
                    "label": self.label, "childNodes": self.childNodes}

    # for printing
    def __repr__(self):
        # # full
        # return str(self.__dict__)

        # # could experiment
        # return str(self.encode())

        # beautify
        return str({"line": self.line, "last_line": self.last_line, "level": self.level, "isActive": self.isActive,
                    "label": self.label, "childNodes": self.childNodes})


def parse_code(input_lines, isActive):
    def closest_lower(list_compare, value):
        # lower
        for i in range(len(list_compare) - 1, -1, -1):
            if list_compare[i] < value:
                return i
        return None

    # init
    root = Node("root", -1, -1)
    processed_level = [-1]
    processed_nodes = [root]

    for idx, line in enumerate(input_lines):

        current_node = Node(line, idx)

        # invalid node
        if not current_node.isValid:
            return None

        current_level = current_node.level

        # check if isActive
        if idx == isActive:
            current_node.isActive = True

        # get index of parent
        parent_index = closest_lower(processed_level, current_level)

        # invalid input -- have children without parent
        if parent_index == None:
            return None

        # valid input

        # add children
        processed_nodes[parent_index].add_children(current_node)

        # add to processed lists
        processed_nodes.append(current_node)
        processed_level.append(current_level)

    # return
    return processed_nodes


# post process -- only do if processed_nodes not none

def get_last_line(processed_nodes):
    def get_child_last_line(node):
        if len(node.childNodes) == 0:
            return node.line

        return get_child_last_line(node.childNodes[-1])

    if processed_nodes == None:
        return

    for idx, node in enumerate(processed_nodes):

        # check first word in the code
        first_word = node.label.split(' ')[0]

        # if
        if first_word == 'if':
            # if only
            node.last_line = get_child_last_line(node)
            # if with elif or else
            for k in range(len(processed_nodes) - 1, idx - 1, -1):
                if (processed_nodes[k].level == node.level) and (processed_nodes[k].label[:4] in ['else', 'elif']):
                    node.last_line = get_child_last_line(processed_nodes[k])  # update last line of original if
                    break  # find the last one only

        # class, def, for, while, return
        elif first_word in ['class', 'def', 'for', 'while', 'return']:
            node.last_line = get_child_last_line(node)

        # edge cases not removing from tree
        elif (node.isActive) or (node.label == 'root'):
            continue

        # remove from tree
        else:
            node.willRemove = True


def remove_unwanted(node):
    if len(node.childNodes) == 0:
        return

    new_childNodes = []
    for i in range(0, len(node.childNodes)):
        child = node.childNodes[i]

        # remove child of child
        remove_unwanted(child)

        # remove child itself or not
        if (child.willRemove == False):
            new_childNodes.append(child)

    node.childNodes = new_childNodes


def run(inputObj):
    try:

        # parse
        processed_nodes = parse_code(inputObj["input_lines"], isActive=inputObj["isActive"])

        if processed_nodes == None:
            return {"error_code": 1, "data": []}

        # formatting
        get_last_line(processed_nodes)
        remove_unwanted(processed_nodes[0])

        # return json.dumps({"error_code": 0, "data": processed_nodes[0].childNodes})
        return json.loads(
            json.dumps({"error_code": 0, "data": processed_nodes[0].childNodes}, default=lambda o: o.encode(),
                       indent=4))

    except Exception as e:

        return json.loads(json.dumps({"error_code": 0, "data": ""}))
