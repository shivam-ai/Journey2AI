
def print_values(V, g):
    for j in range(g.width):
        print("----------------------------")
        for i in range(g.height):
            v= V.get((i, j), 0)
            if(v >= 0):
                print(" %.2f|"% v, end= "")
            else:
                print("%.2f|"% v, end= "")
        print("")

def print_policy(P, g):
    for j in range(g.width):
        print("---------------------------")
        for i in range(g.height):
            a= P.get((i, j), ' ')
            print(" %s |"%a, end= "")
        print("")

        
