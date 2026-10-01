import json


def new_game():
    return {'amount': 0, 'events': {1: (5, 6), 2: (1, 2)}, 'items': [], 'cap': 2, 'count': 0, 'closed': False, 'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}, 'src': 10, 'dst': 0, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_10(state):
    amount = -5
    if amount < 0:
        return False
    state["amount"] += amount
    return True

def bug_17(state):
    amount = -5
    if amount < 0:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_24(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def bug_1(state):
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True

def bug_8(state):
    state["count"] = 0
    return True

def bug_15(state):
    if state["closed"]:
        return False
    return True

def bug_22(state):
    for a, b in state["edges"]:
        if a in state["nodes"] and b in state["nodes"]:
            return True
    return False

def bug_29(state):
    state["nodes"].pop(1, None)
    state["edges"] = {k: v for k, v in state["edges"].items() if 1 not in k}
    return True

def bug_6(state):
    return len(state["items"])

def bug_13(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def bug_30(state):
    for op in state["log"]:
        if op[1] == "failed":
            state["value"] = state["snapshot"]
            return False
    return True

def bug_31(state):
    if state["settled"]:
        return False
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
