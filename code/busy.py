# -*- coding: utf-8 -*-
import math
import random
from math import pow, sqrt

input = u'./iw.in'
output = u'./iw.out'

def readfile(filename):
    """
    load file, init users and projects
    """
    users = []
    projects = []
    demand = {}
    for line in file(filename):
        if line.strip() == "0 0":
            break

        cols=line.strip().split(' ')

        if (cols[0] not in users):
            users.append(cols[0])

        if (cols[1] not in projects):
            projects.append(cols[1])
            demand[cols[1]] = []

        demand[cols[1]].append(cols[0])

    print "users:"
    print users
    print "projects:"
    print projects
    print "demand {project:[users]}:"
    print demand
    print ""

    return users, projects, demand

def writefile(projects, schedule_projects):
    #clear
    file = open(output, 'w')
    file.write("")
    file.close()

    file = open(output, 'w+')
    max = 0
    for project in projects:
        schedule = schedule_projects[project]
        if len(schedule) > max:
            max = len(schedule)

    for project in projects:
        schedule = schedule_projects[project]
        if len(schedule) < max:
            for i in range(max - len(schedule)):
                schedule.append("0")
        line = " ".join(schedule)
        file.write(line + "\n")

    file.close()

def get_cost(waste_of_user, waste_of_projects, duration):
    """
    calculate the cost
    """

    cost = pow(waste_of_user, 2) + waste_of_projects + sqrt(duration)
    print ("users wait for %s, projects wait for %s, duration is %s, score is %s" \
           % (waste_of_user, waste_of_projects, duration, cost))
    return cost

def main():
    users, projects, demand = readfile(input)

    # get first random result
    first_schedule_projects, first_schedule_users, first_max = get_random_result(users, projects, demand)
    first_waste_of_users = get_waste_of_users(first_schedule_users)
    first_waste_of_projects = get_waste_of_projects(first_schedule_projects)
    first_cost = get_cost(first_waste_of_users, first_waste_of_projects, first_max)

    final_schedule_projects = first_schedule_projects
    final_cost = first_cost

    T = 10000.0 #int temperatrue
    while T > 0.1:
        print ""
        schedule_projects, schedule_users, max = get_random_result(users, projects, demand)
        waste_of_users = get_waste_of_users(schedule_users)
        waste_of_projects = get_waste_of_projects(schedule_projects)
        cost = get_cost(waste_of_users, waste_of_projects, max)

        if (cost < final_cost or random.random() < pow(math.e, -(cost-final_cost)/T)):
            final_cost = cost
            final_schedule_projects = schedule_projects

        # cool
        T = T * 0.90

    print ""
    print "final result:"
    print final_schedule_projects
    print "final cost:"
    print final_cost

    writefile(projects, final_schedule_projects)

def get_waste_of_users(schedule_users):
    """
    count zero from each user's schedule
    """
    zero = 0
    for (k,v) in schedule_users.items():
        keys = v.keys()
        zero += (keys[-1] - keys[0] + 1) - len(keys)
    return zero

def get_waste_of_projects(schedule_projects):
    """
    count zero from each project's schedule
    """
    zero = 0
    for (k,v) in schedule_projects.items():
        for user in v:
            if int(user) == 0:
                zero += 1
    return zero


def get_random_result(users, projects, demand):
    """
    get a random result set
    """
    schedule_projects = {} # projects' schedule
    schedule_users = {} # users' schedule
    max = 0 # max time from start to end
    free = {} # free users each clock

    for (k,v) in demand.items():
        schedule_projects[k] = [] # k's schedule
        pending = [val for val in v] # pending users

        i = 1
        while len(pending) > 0:
            if not free.has_key(i):
                free[i] = [val for val in users]

            waiting = [val for val in free[i] if val in pending] # merge free and pending

            if len(free[i]) == 0:
                break

            # no one free at the moment
            if len(waiting) == 0:
                schedule_projects[k].append("0")
                i += 1
                continue

            #waiting.append("0") # or nobody

            index = random.randint(0, len(waiting)-1)
            user = waiting[index]

            # update project
            schedule_projects[k].append(user)

            if int(user) != 0:
                # update user
                if not schedule_users.has_key(user):
                    schedule_users[user] = {}
                schedule_users[user][i] = k
                # delete the user from pending
                pending.remove(user)
                # delete the user from free list of this clock
                free.get(i).remove(user)

            i += 1

        if (i > max):
            max = i - 1

    print "schedule_projects:"
    print schedule_projects

    print "schedule_users:"
    print schedule_users

    print "max:"
    print max

    return schedule_projects, schedule_users, max

if __name__ == '__main__':
    main()
