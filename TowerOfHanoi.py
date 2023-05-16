# A way of determining the minimum amount of moves depending on n = disks.
# 2^n - 1 = min amount of moves
# Fun fact: This formula is exactly the same as Mersenne's number 

amountOfMoves = int(0)

print('How many disks are there?')
answerDisks = int(input())
amountOfMoves = 2 ** answerDisks - 1

print('if there are', answerDisks,'disks, then the minimal amount of moves are', amountOfMoves)
