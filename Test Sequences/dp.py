#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix
# ------------------------------------------------------------

#scoring system
A = 4
C = 3
G = 2
T = 1
MISS = -3
GAP = -2

def c(x, y):
    if x == y:
        if x == 'A':
            return A
        elif x == 'C':
            return C
        elif x == 'G':
            return G
        else:   #x == 'T'
            return T
    else:
        return MISS


# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 

#Initialise scoring and backtrack matrices
scoring = [[None for i in range(len(seq1))] for j in range(len(seq2))]
backtrack = [[None for i in range(len(seq1))] for j in range(len(seq2))]

#Fill in matrices row by row
for j in range(len(seq2)):
    for i in range(len(seq1)):
        if i == 0 or j == 0:
            #deal with base cases
            if i == 0:
                scoring[j][i] = GAP * j
                backtrack[j][i] = 'U'
            elif j == 0:
                scoring[j][i] = GAP * i
                backtrack[j][i] = 'L'
            
            if i == 0 and j == 0:
                backtrack[j][i] = 'END'

        else:
            #calculate maximum score for cell
            charScore =  c(seq1[i], seq2[j])
            D = charScore + scoring[j-1][i-1]

            if charScore > 0:
                scoring[j][i] = D
                backtrack[j][i] = 'D'
            else:

                L = scoring[j][i-1] + GAP
                U = scoring[j-1][i] + GAP
                maxScore = max(D, L, U)

                if D == maxScore:
                    scoring[j][i] = D
                    backtrack[j][i] = 'D'
                elif L == maxScore:
                    scoring[j][i] = L
                    backtrack[j][i] = 'L'
                    if charScore > 0:
                        print("oof")
                else:   #U == maxScore
                    scoring[j][i] = U
                    backtrack[j][i] = 'U'
                    if charScore > 0:
                        print("ouchie")

#build alignment
i = len(seq1) - 1
j = len(seq2) - 1
best_alignment = ['','']
best_score = 0

while not backtrack[j][i] == 'END':
    if backtrack[j][i] == 'D':
        
        nextSeq1Char = seq1[-1]
        seq1 = seq1[:-1]
        nextSeq2Char = seq2[-1]
        seq2 = seq2[:-1]

        i -= 1
        j -= 1

        best_score += c(nextSeq1Char, nextSeq2Char)
        
    elif backtrack[j][i] == 'L':
        
        nextSeq1Char = seq1[-1]
        seq1 = seq1[:-1]
        nextSeq2Char = '-'

        i -= 1

        best_score += GAP
        
    else:   #backtrack[j][i] == 'U'

        nextSeq1Char = '-'
        nextSeq2Char = seq2[-1]
        seq2 = seq2[:-1]

        j -= 1

        best_score += GAP


    best_alignment[0] = nextSeq1Char + best_alignment[0]
    best_alignment[1] = nextSeq2Char + best_alignment[1]
    
        

        

#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

