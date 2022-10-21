from numpy import array, reshape
#Forma fortran(idonea)
# U = array( [1, 2, 3, 4] )
# U = reshape(U, (2,2))
# print('U', U)

# U[[0,1],:] = U[[0,1],:]

# print(U)

#Lo habitual
U = array( [1, 2, 3, 4] )
U = reshape(U, (2,2))
(U[:,0], U[:,1]) = (U[:,1].copy() , U[:,0].copy()) 
print(U)
