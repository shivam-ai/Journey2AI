from grid_world import Grid

def make_grid(obey_prob= 1.0):
    draw= [
        '.  .  .  x  .  2',
        '.  x  . -1  . -1',
        '. -1  .  .  .  .',
        '.  .  x  .  .  .',
        's  .  x  .  .  1'
    ]

    height= len(draw)
    width= len(draw[0].split())
    
    grid= [['.' for x in range(width)] for y in range(height)]

    for i in range(len(draw)):
        g= draw[i]
        gs= g.split()
        for j in range(len(gs)):
            gg= gs[j]
            if(gg!= '.' and gg!= 'x' and gg!= 's'):
                gg= int(gg.strip())
            grid[i][j]= gg 

    start= (0,0)
    rewards= {}
    actions= {}
    for i in range(height):
        for j in range(width):
            value= grid[i][j]
            ii= height- i- 1
            if(value=='s'):
                start= (j,ii)
            if(type(value)==int):
                rewards[(j,ii)]= value

            if(value=='s' or value=='.'):
                moves= []
                if(i>0 and grid[i-1][j]!= 'x'):
                    moves.append('U')
                if(i<height-1 and grid[i+1][j]!= 'x'):
                    moves.append('D')
                if(j>0 and grid[i][j-1]!= 'x'):
                    moves.append('L')
                if(j<width-1 and grid[i][j+1]!= 'x'):
                    moves.append('R')
                actions[(j, ii)]= moves


    print("Height is {} and Width is {}".format(height, width))
    print("Starting Point: {}".format(start))
    print("Rewards: {}".format(rewards))
    print("Actions: ")

    for key, value in actions.items():
        print(key, ":", value)


    final_grid= Grid(width, height, start)
    final_grid.set(rewards, actions, obey_prob)

    return final_grid










make_grid()
