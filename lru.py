# coding=utf-8

import sys

pages = ["1","2","3","4","5","1","2","3","4","1","2","3","1","2","1"]
frames,p=3,3
matrix = [[' ' for i in xrange(len(pages))] for i in xrange(frames)]
def printmatrix(matrix):
    for i in range(3):
        print matrix[i]

"""
[0,0][0,1]]0,2][0,3][0,4][0,5]]0,6][0,7]
[1,0][1,1][1,2][1,3][1,4][1,5][1,6][1,7]
[2,0][2,1][2,2][2,3][2,4][2,5][2,6][2,7]
"""
def isinframes(matrix,a,frames,page):
        for j in range(frames):
            #print "page {} is not in matrix[{}][{}]={} ?".format(page,j,a,matrix[j][a])
            if matrix[j][a] == page:
                return True
        #print "page not found"
        return False

def update_matrix(repl,p,i):
    for z in range(0,frames):
        if z == repl:
            #print "update matrice[{}][{}] with  {}".format(i,repl,pages[p])
            matrix[z][i+1] = pages[p]
        else:
            #print "update matrice[{}][{}] with  matrice[{}][{}]".format(z,i+1,z,i)
            matrix[z][i+1] = matrix[z][i]



#start
for i in range(frames):
    for j in range(i+1):
        matrix[j][i] = pages[j]



for i in range(frames-1,len(pages)-1):
    if(not isinframes(matrix,i,frames,pages[p])): # is page available?
        freq = [0]*frames
        for k in range(0,frames):
            count = 0
            for j in range(p-1,-1,-1):
                #print "if {} == {}".format(matrix[k][i],pages[j])
                if matrix[k][i] == pages[j]:
                    break
                else:
                    count+=1
                    freq[k]=count
        repl= freq.index(max(freq))
        #print "replace matrix[{}][{}] with {}".format(i,repl,pages[p])
    else:
        repl=-1
    update_matrix(repl,p,i)
    p+=1

print pages
print "\n"
printmatrix(matrix)
