
#-------------------------------------------------------------------------
# Note: please don't use any additional package except the following packages
import numpy as np
#-------------------------------------------------------------------------
'''
    Problem 1: TicTacToe and MiniMax 
    In this problem, you will implement a version of the TicTacToe game and a minimax player.
    You could test the correctness of your code by typing `nosetests -v test1.py` in the terminal.
'''

#-------------------------------------------------------
class PlayerRandom:
    '''a random player, who choose valid moves randomly. '''
    # ----------------------------------------------
    def play(self,s):
        '''
           The policy function, which chooses one move in the game.  
           Here we choose a random valid move.
           Input:
                s: the current state of the game, an integer matrix of shape 3 by 3. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by you. 
                    (for example, if you are the "O" player, then i, j-th slot is taken by "O") 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the opponent.
           Outputs:
                r: the row number, an integer scalar with value 0, 1, or 2. 
                c: the column number, an integer scalar with value 0, 1, or 2. 
        '''
        #########################################
        ## INSERT YOUR CODE HERE




        #########################################
        return r,c


#-------------------------------------------------------
class TicTacToe:
    '''TicTacToe is a game engine. '''
    # ----------------------------------------------
    def __init__(self):
        ''' Initialize the game. 
            Input:
                self.s: the current state of the game, a numpy integer matrix of shape 3 by 3. 
                        self.s[i,j] = 0 denotes that the i-th row and j-th column is empty
                        self.s[i,j] = 1 denotes that the i-th row and j-th column is "X"
                        self.s[i,j] = -1 denotes that the i-th row and j-th column is "O"
        '''
        self.s = np.zeros((3,3))


    # ----------------------------------------------
    def play_x(self, r, c):
        '''
           X player take one step with the location (row and column number)
            Input:
                r: the row number, an integer scalar with value 0, 1, or 2. 
                c: the column number, an integer scalar with value 0, 1, or 2. 
        '''
        assert  self.s[r,c]==0
        #########################################
        ## INSERT YOUR CODE HERE

        #########################################

    # ----------------------------------------------
    def play_o(self, r, c):
        '''
           O player take one step with the location (row and column number)
            Input:
                r: the row number, an integer scalar with value 0, 1, or 2. 
                c: the column number, an integer scalar with value 0, 1, or 2. 
        '''
        assert  self.s[r,c]==0
        #########################################
        ## INSERT YOUR CODE HERE

        #########################################

    # ----------------------------------------------
    @staticmethod
    def check(s):
        '''
            check if the game has ended.  
            Input:
                s: the current state of the game, an integer matrix of shape 3 by 3. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by you. (for example, if you are the "O" player, then i, j-th slot is taken by "O") 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the opponent.
            Outputs:
                e: the result, an integer scalar with value 0, 1 or -1.
                    if e = None, the game doesn't end yet.
                    if e = 0, the game is a draw.
                    if e = 1, X player won the game.
                    if e = -1, O player won the game.
        '''
        #########################################
        ## INSERT YOUR CODE HERE


        # check the 7 lines in the board to see if the game has ended.









        #########################################
        return e



    # ----------------------------------------------
    def game(self,x,o):
        '''
            run a tie-tac-toe game starting from the current state of the game, letting X and O players to play in turns.
            Here we assumes X player moves first in a game, then O player moves.
            Input:
                x: the "X" player (the first mover), such as PlayerRandom, you could call x.play() to let this player to choose ome move.
                o: the "O" player (the second mover)
            Outputs:
                e: the result of the game, an integer scalar with value 0, 1 or -1.
                    if e = 0, the game ends with a draw/tie.
                    if e = 1, X player won the game.
                    if e = -1, O player won the game.
        '''
        #########################################
        ## INSERT YOUR CODE HERE















        #########################################
        return e


#-------------------------------------------------------
class PlayerMiniMax:
    '''
        Minimax player, who choose optimal moves by searching the subtree with min-max.  In order to speed up the search in multiple steps of the game, we store the score and best move in each game state that has been searched into two dictionary v and p as follows. So that we can re-use the results of the previous search directly without searching the same state again.
    '''
    def __init__(self,d=None):
        self.v = {} 
        ''' 
           v is a dictionary storing all the game states that have been searched with the computed scores/values.
           For example, suppose s is the current state of the game, we want to check whether this state has been searched before.
            v[str(s)] will return a None if this game state has never been searched.
            if s has been searched before, v[str(s)] will return a scalar value (1: win, 0: tie, -1: lose) you can get from the best move.
            Initialize this dictionary as empty, and we want to fill this dictionary after search a state of the game.
        ''' 
        self.p = {} 
        ''' 
           p is a dictionary storing all the game states that have been searched with the best move in each state.
           For example, suppose s is the current state of the game, we want to check whether this state has been searched before.
            p[str(s)] will return a None if this game state has never been searched.
            if s has been searched before, p[str(s)] will return (r,c) of the best move. r: row, c: column
            Initialize this dictionary as empty, and we want to fill this dictionary after search a state of the game.
        ''' 
    # ----------------------------------------------
    def update_v(self,s,v):
        '''
           when the value (v) of a state (s) has been computed, update the dictionary self.v by inserting the key value pair: str(s), v. The input key is the string of the state s, i.e., str(s), and the value is the value of the state. 
           Inputs:
                s: the current state of the game, an integer matrix of shape 3 by 3. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by you. (for example, if you are the "O" player, then i, j-th slot is taken by "O") 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the opponent.
                v: the value of the state, an integer scalar. v=1 denotes that you won the game. v=-1 loss, v =0 draw.
        '''

        #########################################
        ## INSERT YOUR CODE HERE

        # if the current state s is already in dictionary self.v, return (end without doing anythign)



        # otherwise, update dictionary v by inserting the key value pair.


       #########################################

    # ----------------------------------------------
    def update_p(self,s,r,c):
        '''
           When the best move of a state (s) has been computed, update the policy dictionary self.p by inserting a key-value pair: the input key is the string of the state s, i.e., str(s), and the value is (r,c). Here r is the row number of the best move. c is the column number of the best move.
           Inputs:
                s: the current state of the game, an integer matrix of shape 3 by 3. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by you. (for example, if you are the "O" player, then i, j-th slot is taken by "O") 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the opponent.
                r: the row number, an integer scalar with value 0, 1, or 2. 
                c: the column number, an integer scalar with value 0, 1, or 2. 
           Hint: you may want to consider rotation and mirror images of the state.
        '''
        #########################################
        ## INSERT YOUR CODE HERE

        # if the current state s is already in dictionary self.p, return (exit this function without doing anything to self.p)



        # otherwise, update dictionary p by inserting the key value pair into self.p


        #########################################


    # ----------------------------------------------
    def compute_v(self,s):
        '''
           compute value of the current state (when it is your turn in the game). use minimax tree search.
           During the tree search, update both dictionary v and p on each node of the search tree.
           Inputs:
                s: the current state of the game, an integer matrix of shape 3 by 3. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by you. (for example, if you are the "O" player, then i, j-th slot is taken by "O") 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the opponent.
           Outputs:
                v: the estimated score of the best move, an integer scalar with value 0, 1 or -1.
                    if v = 0, the best result is a "draw"
                    if v = 1, the best result is a "win"
                    if v =-1, the best result is a "lose"
           Hint: you could use recursion to solve the problem. 
        '''
        #########################################
        ## INSERT YOUR CODE HERE

        # if the current state has been computed before (in the dictionary self.v), return the value. 



        # check if the game has already ended

        # if the game has already ended,  update dictionary self.v and return the result of the game.




        # if the game has not ended yet, recursively search subtree by trying each possible valid move separately, and update dictionary v and p.
        # get a list of all valid moves



        # compute the value of each child node in the search tree
        # iterate through each move

            # make a copy of the current state s, say sc

            # try a move by adding it into the copy of the current state (sc)



            # inverse the values of game state sc, and compute the value of this state

        # among all the values of the valid moves, find the best next move


        # update v by adding the value of the current state

        # update p by adding the best move for the current state

        #########################################
        return v


    # ----------------------------------------------
    def play(self,s):
        '''
           the policy function of the minimax player, which chooses one move in the game.  
           Inputs:
                s: the current state of the game, an integer matrix of shape 3 by 3. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by you. (for example, if you are the "O" player, then i, j-th slot is taken by "O") 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the opponent.
           Outputs:
                r: the row number, an integer scalar with value 0, 1, or 2. 
                c: the column number, an integer scalar with value 0, 1, or 2. 
          Hint: you could solve this problem using 3 lines of code.
        '''
        #########################################
        ## INSERT YOUR CODE HERE

        # if the best move for the current state has not been searched before (not in dictionary p), compute the value of the current state 



        # find the best move in dictionary p


        #########################################
        return r,c


