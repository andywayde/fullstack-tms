import time

def getTotal(projects):
    sum = 0
    for project in projects:
        sum += project.total
    return sum