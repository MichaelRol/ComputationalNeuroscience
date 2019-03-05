#for the submission uncomment the submission statements
#see submission.README

import math

#from submission import *

weight_matrix = [[0 for x in range(11)] for y in range(11)] 
N = 3.0


six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]


for i in range(0, 11):
    for j in range(0, 11):
        if i != j:
            weight_matrix[i][j] = 1/N * (six[i]*six[j] + three[i]*three[j] + one[i]*one[j])


def hopfield(x):
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 11):
        val = 0
        for j in range(0, 11):
            if i != j:
                val += weight_matrix[i][j]*x[j]
        if val > 0:
            y[i] = 1
        if val < 0:
            y[i] = -1
    return y

def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False
    

    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")
    
    def vert(d1,d2,d3):
        word=""

        if d1:
            word="|"
        else:
            word=" "
        
        if d3:
            word+="_"
        else:
            word+=" "
        
        if d2:
            word+="|"
        else:
            word+=" "
        
        print(word)

    

    pattern_b=map(to_bool,pattern)

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))
        
#submission=Submission("michael_rollins")
#submission.header("Michael Rollins")

six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(three)
seven_segment(six)
seven_segment(one)

##this assumes you have called your weight matrix "weight_matrix"
#submission.section("Weight matrix")
#submission.matrix_print("W",weight_matrix)

print("test1")
#submission.section("Test 1")

test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]

while(1):
    next = hopfield(test)
    if next == test:
        break
    else:
        test = next
        seven_segment(test)

#submission.seven_segment(test)
##for COMSM0027

##where energy is the energy of test
#submission.qquad()
#submission.print_number(energy)

##this prints a space
#submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step

print("test2")
#submission.section("Test 2")

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]
    

while(1):
    next = hopfield(test)
    if next == test:
        break
    else:
        test = next
        seven_segment(test)

#submission.seven_segment(test)

##for COMSM0027
##where energy is the energy of test
#submission.qquad()
#submission.print_number(energy)

##this prints a space
#submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step


#submission.bottomer()
