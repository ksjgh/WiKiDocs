import os
import sys

PATH=os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)

def update_family_tree(tree,parent,child) :
    tree[child][0] = parent     # update parent in child node
    tree[parent][1].add(child)  # update child in parent node


def calc_generation(tree) :
    max_gen = 1
    for n in tree.keys() :
        if not tree[n][1] :         # if there is no child
            gen = 1
            current_node = tree[n][0]
            while(True) :
                gen+=1
                if tree[current_node][0] == 0 :  # if  origin
                    break
                else :
                    current_node =  tree[current_node][0]

            if gen > max_gen :
                max_gen = gen

    return max_gen


with open("test.txt", "r") as f:

    T =  int((f.readline().split())[0]) # Total test cases
    # print("Test Cases = %d\n " % T)

    for t in range(T) :
        N =  int((f.readline().split())[0]) # number of people in family
        # print("\nN peoples = %d "  % N)

        tree = { n : [0 , set() ] for n in range(1,N+1) } # node : [ parent , {children....}]        # make family tree
        for i in range(N-1) :
            l = list(map(int,f.readline().split()))
            parent , child = l[0] , l[1]
            # print("parent={0} child={1} ".format(parent,child))

            update_family_tree(tree,parent,child)

        # print(tree)
        print("Generation = %d " % calc_generation(tree))

    # print("End of Test")
