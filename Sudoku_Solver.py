#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 23:27:22 2021

@author: leon
"""

import numpy as np
 
class Sudoku_Solver:
    
    def Solve(self,Sudoku):
        
        for x in range(81):
    
            for i in range(len(Sudoku[0,:,0])):
                for j in range(len(Sudoku[0,0,:])):
                    
                    if Sudoku[0,i,j] == 0 :
               
                        for z in range(1,len(Sudoku[:,0,0])):
                            
                            if (Sudoku[0,:,j] == z).any() or (Sudoku[0,i,:] == z).any() :
                                Sudoku[z,i,j] = 0
                                
                            elif i in range(0,3) and j in range(0,3) and (Sudoku[0,0:3,0:3] == z).any() :
                                Sudoku[z,i,j] = 0
                            elif i in range(0,3) and j in range(3,6) and (Sudoku[0,0:3,3:6] == z).any() :
                                Sudoku[z,i,j] = 0
                            elif i in range(0,3) and j in range(6,9) and (Sudoku[0,0:3,6:9] == z).any() :
                                Sudoku[z,i,j] = 0
                            elif i in range(3,6) and j in range(0,3) and (Sudoku[0,3:6,0:3] == z).any() :
                                Sudoku[z,i,j] = 0
                            elif i in range(3,6) and j in range(3,6) and (Sudoku[0,3:6,3:6] == z).any() :
                                Sudoku[z,i,j] = 0
                            elif i in range(3,6) and j in range(6,9) and (Sudoku[0,3:6,6:9] == z).any() :
                                Sudoku[z,i,j] = 0
                            elif i in range(6,9) and j in range(0,3) and (Sudoku[0,6:9,0:3] == z).any() :
                                Sudoku[z,i,j] = 0
                            elif i in range(6,9) and j in range(3,6) and (Sudoku[0,6:9,3:6] == z).any() :
                                Sudoku[z,i,j] = 0
                            elif i in range(6,9) and j in range(6,9) and (Sudoku[0,6:9,6:9] == z).any() :
                                Sudoku[z,i,j] = 0
                            
                            if list(Sudoku[:,i,j] != 0).count(1) == 1 and Sudoku[z,i,j] == z :
                                Sudoku[0,i,j] = z
                        
                    else:    
                        Sudoku[1:10,i,j] = 0
                        
            del i,j            
            Sudoku = self.find_disjunction(Sudoku)
                    
        return Sudoku
                    
                        
    def find_disjunction(self,Sudoku):
                   
        for i in range(len(Sudoku[0,:,0])):
            for j in range(len(Sudoku[0,0,:])):
                
               for mode in range(3):
                
                    if mode == 0:
                        c = j
                        Fields = Sudoku[:,i,:]
                    elif mode == 1:
                        c = i
                        Fields = Sudoku[:,:,j]
                    elif mode == 2:
                        borders = self.ret_square(i,j)
                        c = 3 * (i - borders[0]) + j - borders[2]
                        Fields = np.concatenate([Sudoku[:,borders[0]  ,borders[2]:borders[3]],
                                                 Sudoku[:,borders[0]+1,borders[2]:borders[3]],
                                                 Sudoku[:,borders[0]+2,borders[2]:borders[3]]],axis=1)
                       
                    L = np.delete(Fields[1:9,c],np.where(Fields[1:9,c]==0))
                    
                    L = np.array([L,[np.count_nonzero(Fields[1:10,:] == x) for x in L]])
                    
                    if not any([np.count_nonzero(L[1,:] == x) == x for x in range(1,10)]):
                        
                        break
                            
                    for x in range(1,10):
                        
                        if np.count_nonzero(L[1,:] == x) == x:
                            
                            k = []
                            
                            L2 = np.delete(L,np.where(L[1,:]!=x),axis = 1)

                            for y in range(9):
                                
                                L3 = np.delete(Fields[1:9,y],np.where(Fields[1:9,y]==0))
                        
                                if all([any(L3 == x) for x in L2[0]]):
                                    
                                    k.append(y)
                                    
                            if x == len(k) :
                                
                                for y in k:
                                    
                                    Fields[:,y] = 0
                                    
                                    for z in L2[0]:
                                      
                                        z = int(z)
                                        Fields[z,y] = z 
                              
                                break
                                    
                            
# =============================================================================
#                     if mode == 0:
#                         Sudoku[:,i,:] = Fields
#                     elif mode == 1:
#                         Sudoku[:,:,j] = Fields
#                     elif mode == 2:
#                         Sudoku[:,borders[0]  ,borders[2]:borders[3]] = Fields[:,0:3]
#                         Sudoku[:,borders[0]+1,borders[2]:borders[3]] = Fields[:,3:6]
#                         Sudoku[:,borders[0]+2,borders[2]:borders[3]] = Fields[:,6:9]
# =============================================================================
                        
                    return Sudoku
                                
                    
    def ret_square(i,j):
        
        if i in range(0,3) and j in range(0,3) :
            k = (0,3,0,3)
        elif i in range(0,3) and j in range(3,6) :
            k = (0,3,3,6)
        elif i in range(0,3) and j in range(6,9) :
            k = (0,3,6,9)
        elif i in range(3,6) and j in range(0,3) :
            k = (3,6,0,3)
        elif i in range(3,6) and j in range(3,6) :
            k = (3,6,3,6)
        elif i in range(3,6) and j in range(6,9) :
            k = (3,6,6,9)
        elif i in range(6,9) and j in range(0,3) :
            k = (6,9,0,3)
        elif i in range(6,9) and j in range(3,6) :
            k = (6,9,3,6)
        elif i in range(6,9) and j in range(6,9) :
            k = (6,9,6,9)
            
        return k
                        

if __name__ == "__main__":
    
    
    Sudoku = np.zeros([10,9,9])
    
    for i in range(10):
        
        Sudoku[i,:,:] = i
        
    del i
    
    Sudoku[0,:,:] = np.array([[0,0,0, 0,0,0, 0,0,0],
                              [0,0,0, 0,0,0, 0,0,0],
                              [0,0,0, 0,0,0, 0,0,0],
                     
                              [0,0,0, 0,0,0, 0,0,0],
                              [0,0,0, 0,0,0, 0,0,0],
                              [0,0,0, 0,0,0, 0,0,0],
                     
                              [0,0,0, 0,0,0, 0,0,0],
                              [0,0,0, 0,0,0, 0,0,0],
                              [0,0,0, 0,0,0, 0,0,0]])
                  
                  
    Sudoku[0,:,:] = np.array([[0,3,0, 0,0,0, 0,0,0],
                              [0,0,0, 1,9,5, 0,0,0],
                              [0,0,8, 0,0,0, 0,6,0],
                     
                              [8,0,0, 0,6,0, 0,0,0],
                              [4,0,0, 8,0,0, 0,0,1],
                              [0,0,0, 0,2,0, 0,0,0],
                     
                              [0,6,0, 0,0,0, 2,8,0],
                              [0,0,0, 4,1,9, 0,0,5],
                              [0,0,0, 0,0,0, 0,7,0]])
    
    Sudoku2 = np.copy(Sudoku)
    
    Sudoku = Sudoku_Solver().Solve(Sudoku)          
    
    print(Sudoku[0,:,:])
    print(Sudoku[0,:,:] == Sudoku2[0,:,:])