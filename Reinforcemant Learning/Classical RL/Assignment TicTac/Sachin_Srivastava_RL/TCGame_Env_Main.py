# Since we were given the option to use the given environment file or create our own,I decided to do this assignment with my own enviornment and agent files.


from gym import spaces
import numpy as np
import random



def plot_agent_reward(rewards, agent_type):
    """ Function to plot agent's accumulated reward vs. episode """
    plt.plot(rewards)
    if agent_type == 'q':
        plt.title('Q-Learning Agent Cumulative Reward vs. Episode')
    else:
        plt.title('Sarsa Agent Cumulative Reward vs. Episode')
    plt.ylabel('Reward')
    plt.xlabel('Episode')
    plt.show()

class TicTacToe:
    def __init__(self):
        
        self.board = [0]*9
        
         # Agent player has only options [1, 3, 5, 7, 9]
        self.player1_agent = None # These values are passed as input to the QLearning process
        # Environment player has only options [2, 4, 6, 8]
        self.player2_envt = None # These values are passed as input to the QLearning process

    #reset the game
    def reset(self):
        self.board = [0] * 9

   #evaluate function to judge winning combination
    def evaluate(self):
       
        for i in range(3):
            if (self.board[i * 3] + self.board[i * 3 + 1] + self.board[i * 3 + 2]) == 15:
                return 1.0, True
        
        # "col checking"
        for i in range(3):
            if (self.board[i + 0] + self.board[i + 3] + self.board[i + 6]) == 15:
                return 1.0, True
        
        # diagonal checking
        if (self.board[0] + self.board[4] + self.board[8]) == 15:
            return 1.0, True
        if (self.board[2] + self.board[4] + self.board[6]) == 15:
            return 1.0, True

        # "if filled draw"
        if not any(space == 0 for space in self.board):
            return 0.0, True

        return 0.0, False

    #return remaining possible moves
    def possibleMoves(self):
        blank_spots =  [moves + 1 for moves, spot in enumerate(self.board) if spot == 0]
        return blank_spots

    #pick a possible move based on the odd(agent) or even(envionment) player
    def pickMove(self, isX):
        # we will shuffle the set of remaining options and pop the first from the list to be used for our move.
        if(isX):
            self.player1_agent.options = random.sample(self.player1_agent.options, len(self.player1_agent.options))
            return self.player1_agent.options.pop()
        # in our setup we have one set of player playing odd and the other even, 
        # so we need to switch between the two to determine the next move pick
        else:
            self.player2_envt.options = random.sample(self.player2_envt.options, len(self.player2_envt.options))
            return self.player2_envt.options.pop()

    #take next step and return reward
    def step(self, isX, move):
        self.board[move-1]= self.pickMove(isX)
        reward, done = self.evaluate()
        return reward, done

    #begin training
    def startTraining(self, player1, player2, episodes, odd=True, verbose = False):
        statetrack = {}
        self.player1_agent=player1
        self.player2_envt=player2
        print ("Training Started")
        for i in range(episodes):
            if verbose: print("Episode ", i)
            self.player1_agent.game_begin()
            self.player2_envt.game_begin()
            self.reset()
            done = False

            # Note that the odd player always begins the game for our simulation and is set to true by default
            isX = odd
            while not done:
                if isX:
                    move = self.player1_agent.epsilon_greedy(self.board, self.possibleMoves())
                else:
                    move = self.player2_envt.epsilon_greedy(self.board, self.possibleMoves())

                # 'reward' value is binary 0 or 1 and 'done' is True if game ends (win, lose, draw) False otherwise
                reward, done = self.step(isX, move)

                if (reward == 1):  # won, reward 10 for the agent winning the game and -10 otherwise
                    if (isX):
                        self.player1_agent.updateQ(10, self.board, self.possibleMoves())
                        self.player2_envt.updateQ(-10, self.board, self.possibleMoves())
                    else:
                        self.player1_agent.updateQ(-10, self.board, self.possibleMoves())
                        self.player2_envt.updateQ(10, self.board, self.possibleMoves())
                elif (done == False):  # a move was made which did not end the game yet, hence reward -1 for the move
                    if (isX):
                        self.player1_agent.updateQ(-1, self.board, self.possibleMoves())
                       # else:
                        #self.player2_envt.updateQ(-1, self.board, self.possibleMoves())

                else: #(reward == 0):  draw
                    self.player1_agent.updateQ(reward, self.board, self.possibleMoves())
                    self.player2_envt.updateQ(reward, self.board, self.possibleMoves())
                
          

                isX = not isX  # switch players
        print ("Training Completed")
 
    #save Qtables
    def saveStates(self):
        self.player1_agent.saveQ("AgentPolicy")
        self.player1_agent.saveS("Sates_Tracked")
        self.player2_envt.saveQ("EnvironmentPolicy")

    #return Qtables
    def getQ(self):
        return self.player1_agent.Q, self.player2_envt.Q


