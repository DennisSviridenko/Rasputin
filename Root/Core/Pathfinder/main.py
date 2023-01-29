class deine_mutter():
    def __init__(self):
        self.frontier = []
        self.explored = []
        self.current = 1, 7
        self.feld = [
            [3,3,3,3,3,3,3,3,3,3,3,3], 
            [3,0,0,0,0,0,0,0,0,0,2,3], 
            [3,0,0,0,0,0,0,0,0,0,0,3], 
            [3,0,0,0,0,0,0,0,0,0,0,3], 
            [3,0,0,0,0,0,0,0,0,0,0,3], 
            [3,0,0,0,0,0,0,0,0,0,0,3], 
            [3,0,0,0,0,0,0,0,0,0,0,3], 
            [3,1,0,0,0,0,0,0,0,0,0,3],
            [3,3,3,3,3,3,3,3,3,3,3,3]]

    # def get_current(self):
    #     for i in 

    def get_next_frontier(self):
        if self.feld[self.current[0]][(self.current[1]-1)] == 0:
            self.x, self.y = self.current[0], self.current[1]
            print(self.x, self.y)
            self.frontier.append = [self.x, self.y]
            print(self.frontier)

        # else:
        #     print(self.frontier)
        #     print(self.feld[self.current[0]-1])

        # if (self.feld[]self.current[1]-1) == 0:
        #     self.frontier.append([(self.current[1]-1), self.current[0]])
        # if (self.current[1]-1) and (self.current[0]+1) == 0:
        #     self.frontier.append([(self.current[1]-1), self.current[0]+1])
        # if (self.current[0]+1) == 0:
        #     self.frontier.append([(self.current[0]+1), self.current[1]])
        # if (self.current[0]+1) and (self.current[1]+1) == 0:
        #     self.frontier.append([(self.current[0]+1), self.current[1]+1])
        # if (self.current[1]+1) == 0:
        #     self.frontier.append([(self.current[1]+1), self.current[0]])
        # if (self.current[0]-1) and (self.current[1]+1) == 0:
        #     self.frontier.append([(self.current[1]-1), self.current[0]])
        # if (self.current[0]-1) == 0:
        #     self.frontier.append([(self.current[1]-1), self.current[0]])
        # if (self.current[0]-1) and (self.current[1]-1) == 0:
        #     self.frontier.append([(self.current[1]-1), self.current[0]])

moin = deine_mutter()
moin.get_next_frontier()



