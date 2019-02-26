import math


w = [[0 for x in range(11)] for y in range(11)] 

def E(pattern):
    e = 0
    for i in range(0, 11):
        for j in range(0, 11):
            if i != j:
                e += pattern[i]*w[i][j]*pattern[j]
    e *= -0.5
    return e


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
        


six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(three)
seven_segment(six)  
seven_segment(one)


N = 3.0


for i in range(0, 11):
    for j in range(0, 11):
        if i != j:
            w[i][j] = 1/N * (six[i]*six[j] + three[i]*three[j] + one[i]*one[j])
            
print(w)

print(E(three))
print("test1")

test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]

seven_segment(test)

#here the network should run printing at each step

print("test2")

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]

seven_segment(test)

#here the network should run printing at each step