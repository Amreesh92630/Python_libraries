
'''
   The admission fee at a fair is $ 1.50 for children and $4.00 for grown up on a certain day 2200
   people visited and total of $5050 had been collected how many children and how many adults attended?
   
   let x1 be the no of children came to fair and x2 be the no of adults came to fair hence
   x1 + x2 = 2200
   1.5x1 + 4x2 = 5050
'''
a = np.array([[1,1],[1.5,4]])
b = np.array([2200,5050])
np.linalg.solve(a,b)