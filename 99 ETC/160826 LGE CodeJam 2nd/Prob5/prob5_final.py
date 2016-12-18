import os
import sys
import math

PATH=os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)
input_filename = sys.argv[1] ## ON for final implelementation
ouput_filename = os.path.splitext(input_filename)[0] + '.out' ## ON for final implelementation

def is_reachable(position_of_person,position_of_shelter,reachable_range) :
    """
    - input
    position_of_person = [ px, py]
    position_of_shelter = [sx , sy]
    reachable_range : reachable range of each person

    - return
    1 : if reachable
    0 : if reachable
    """
    px , py = position_of_person[0] , position_of_person[1]
    sx , sy = position_of_shelter[0], position_of_shelter[1]
    distance = abs(px-sx) + abs(py-sy)

    if distance > reachable_range :
        return 0
    else :
        return 1

def is_all_person_has_available_shelter(evacuation_check) :
    """
    check if all person has at least on more shelter available
    """
    for p in evacuation_check :
        if sum(p) < 1 :
            return False

    return True

def is_there_saturated_shelter(evacuation_check , capacity_of_shelter) :
    """
    check if a shelter's capacity and it's assigned number of persons
    who has only one available shelter doesn't exeed shelter's capacity.
    """

    ## filter person who has only one shelter
    evacuation_check_filtered = []
    for p in evacuation_check :
        if sum(p) <= 1 :
            evacuation_check_filtered.append(p)
    ## Test code
    print("evacuation_check_filtered")
    print(evacuation_check_filtered)

    ## check if capacity is saturated
    M_shelters = len(capacity_of_shelter)
    N_persons = len(evacuation_check_filtered)

    for s in range(M_shelters) :
        capacity = 0
        for p in range(N_persons) :
            capacity += evacuation_check_filtered[p][s]

        print("shelter # ={0} , capacity ={1} , available capacity ={2}".format(s,capacity,capacity_of_shelter[s]))
        if capacity > capacity_of_shelter[s] :
            return True

    return False



## solution function of problem
def is_evacuation_possible(N_persons,M_shelters,position_of_person,position_of_shelter,capacity_of_shelter,reachable_range) :
    """
    check if evacuation is possible or not

    - input parameters
    N_persons : number of persons
    M_shelters : number of shelters
    position_of_person : 2D list containing position of each person
    position_of_shelter : 2D list containing position of each shelter
    capacity_of_shelter : 1D list containing capacity of each shelter
    reachable_range : reachable range of each person

    - return value
    1 : if evacuation is possible
    0 : if evacuation is impossible

    """
    ## test code
    print("\n")
    print("N_persons = %s" %  N_persons)
    print("M_shelters = %s" %  M_shelters)
    print("position_of_person =")
    print(position_of_person)
    print("position_of_shelter = " )
    print(position_of_shelter)
    print("capacity_of_shelter = ")
    print(capacity_of_shelter)
    print("reachable_range = ")
    print(reachable_range)


    ## make evacuation checking matrix : N_persons x M_shelters
    evacuation_check = []
    for p in range(N_persons) :
        evacuation_check.append( [ is_reachable(position_of_person[p],position_of_shelter[s],reachable_range) for s in range(M_shelters) ] )

    print("evacuation_check matrix")
    print(evacuation_check)

    ## check for evacuation is possible
    if (sum(capacity_of_shelter) < N_persons) :
        print("shelter capacity is not enough\n")
        return 0
    elif not is_all_person_has_available_shelter(evacuation_check) :
        print("certain person has no shelter available\n")
        return 0
    elif is_there_saturated_shelter(evacuation_check , capacity_of_shelter) :
        print("certain shelter is saturated\n")
        return 0

    return 1


#######################  main ##########################################

# with open("test5.in", "r") as f:  ## ON for test
with open(input_filename, "r") as f: ## ON for final implelementation
    T =  int((f.readline().split())[0]) ## Total test cases
    # print("Test Cases = %d\n " % T)

     ## loop in each test case
    for t in range(T) :
    # for t in range(1) : ## ON for test
        l = list(map(int,f.readline().split()))   ## read parameters
        N_persons , M_shelters = l[0], l[1]           ## set parameters

        ## read position of people
        position_of_person = []  ## store position of each person
        for person in range(N_persons) :
            l = list(map(int,f.readline().split()))
            position_of_person.append( [l[0], l[1]] )

        ## read position of shelter
        position_of_shelter = []  ## store position of each shelter
        for shelter in range(M_shelters) :
            l = list(map(int,f.readline().split()))
            position_of_shelter.append( [l[0], l[1]] )

        ## read capacity of shelter
        capacity_of_shelter = []  ## store capacity of each shelter
        l = list(map(int,f.readline().split()))
        for c in range(M_shelters) :
            capacity_of_shelter.append(l[c])

        ## read reachable_range
        reachable_range = list(map(int,f.readline().split()))[0]

        # print(position_of_person)  ## test code if parameters is read well
        # print(position_of_shelter)  ## test code if parameters is read well
        # print(capacity_of_shelter)  ## test code if parameters is read well
        # print(reachable_range)  ## test code if parameters is read well

        evacuation_check = is_evacuation_possible(N_persons,M_shelters,position_of_person,position_of_shelter,capacity_of_shelter,reachable_range)  ## get solutiion
        print("Test {0} Result = {1} ".format(t,evacuation_check)) ## ON for test : screen print

        ######################################## print result to file
        # with open("test5.out", "a") as f1: ## ON for test : file print test

        # ## ON for final implelementation
        with open(ouput_filename, "a") as f1:
            f1.write(str(evacuation_check))
            f1.write("\n")
        ##############################################
