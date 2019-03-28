def make_grid():
    draw= [
        '.  .  .  1',
        '.  x  . -1',
        's  .  .  .'
    ]

    height= len(draw)
    width= len(draw[0].split())
    print("Height is {} and Width is {}".format(height, width))
    
    grid= [['.' for x in range(width)] for y in range(height)]

    for i in range(len(draw)):
        g= draw[i]
        gs= g.split()
        for j in range(len(gs)):
            gg= gs[j]
            if(gg!= '.' and gg!= 'x' and gg!= 's'):
                gg= int(gg.strip())
            grid[i][j]= gg 

    print("\n---------------")
    for g in grid:
        print(g)

    start= (0,0)
    rewards= {}
    for i in range(height):
        for j in range(width):
            value= grid[i][j]
            ii= height- i- 1
            if(value=='s'):
                start= (j,ii)
            if(type(value)==int):
                rewards[(j,ii)]= value
    print(start)
    print(rewards)











make_grid()
