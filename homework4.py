# Jason Zhang
# jasozhang
# 112710259
# CSE 101
# Homework 4

# Part I
def build_dict_regions_by_state(filename):
    state = {}
    z = open(filename)
    y = z.readlines()[0:1]
    for line in open(filename):
        if line != y[0]:
            x = (line.split(','))
            state.setdefault(x[1], []).append(x[0])
    return state





# Part II
def build_dict_stats_by_state(filename, stat):
    state = {}
    z = open(filename)
    y = z.readlines()[0:1]
    if stat == 'cases':
        j = 2
    elif stat == 'deaths':
        j = 3
    elif stat == 'recovered':
        j = 4
    else:
        j = 5
    for line in open(filename):
        if line != y[0]:
            x = (line.split(','))
            h = int(x[j])
            if x[1] not in state.keys():
                state[x[1]] = h
            else:
                state[x[1]] += h
    return state






# Part III
def get_region_max_deaths(filename, state):
    region = ("")
    most_death = 0
    for line in open(filename):
        x = line.split(',')
        if state == x[1]:
            if int(x[3]) >= most_death:
                most_death = int(x[3])
                region = x[0]
    return region





# Part IV
def highest_death_rate_by_state(filename):
    deathdic = {}
    casedic = {}
    z = open(filename)
    y = z.readlines()[0:1]
    for line in open(filename):
        if line != y[0]:
            x = (line.split(','))
            h = int(x[3])
            j = int(x[2])
            if x[1] not in deathdic.keys():
                deathdic[x[1]] = h
            else:
                deathdic[x[1]] += h
            if x[1] not in casedic.keys():
                casedic[x[1]] = j
            else:
                casedic[x[1]] += j
    most = 0
    region = ""
    for i in deathdic:
        u = 100*deathdic[i]/(casedic[i])
        if u > most:
            most = u
            region = i
    return (region, most)





# Part V
def iterative_num_of_pushups(cur_push_ups, days):
    numberpushup = 0
    for i in range(days):
        if i == 0:
            numberpushup += cur_push_ups
        elif  4 >= i > 0:
            numberpushup *= 2
        elif 5 <= i <= 9:
            numberpushup += 10
        elif 10 <= i <= 19:
            numberpushup += 8
        else:
            numberpushup += 5
    return numberpushup





# Part VI
def recursive_num_of_pushups(cur_push_ups, days):
    if days == 1:
        return cur_push_ups
    elif 5 >= days > 1:
        return recursive_num_of_pushups(cur_push_ups * 2, days-1)
    elif 5 < days <= 10:
        return recursive_num_of_pushups(cur_push_ups, days-1) + 10
    elif 10 < days <= 20:
        return recursive_num_of_pushups(cur_push_ups, days-1) + 8
    elif days > 20:
         return recursive_num_of_pushups(cur_push_ups, days-1) + 5
    else:
        return recursive_num_of_pushups(cur_push_ups, days-1)
