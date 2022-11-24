def Google (inputText):    
    openApp("Google Chrome") #opening chrome
    wait(Pattern("1648822475483.png").similar(0.87), 20)
    click(Pattern("1648822475483.png").similar(0.87))
    paste(inputText)  
    type(Key.ENTER)

def setDifficulty(difficulty):
    game = Region(165,273,734,486)
    game.findText("Medium").click()
    wait(Pattern("1650054624341.png").similar(0.75), 20)
    game.findText(difficulty).click()
    
def play():
    Google("tic tac toe")
    wait("1648833948007.png", 20) #wait for the game to load up

    #allowing the user to specify the game difficulty
    difficulty = select("Select the difficulty", options = ("Medium", "Impossible"))
    setDifficulty(difficulty)
    wait(Pattern("1650050887130.png").similar(0.82), 20)
    
    #setting up the important game parameter patterns 
    board = find(Pattern("1650050887130.png").similar(0.82))
    board.setRaster(3,3)
    empty = Pattern("empty.png").exact()
    x = "xCell.png"
    o = "oCell.png"
    
    
    click(board.getCell(1,1)) #first move is always in the middle
    
    wait(Pattern("1648834461359.png").exact(), 20) #start of turn 2
    
    if board.getCell(2,2).has(empty):
            click(board.getCell(2,2))
    else: 
        click (board.getCell(2,0))        
    
    while not exists("1648838289970.png"):
        wait(Pattern("1648834461359.png").exact(), 20)
        #checking for possible wins in a row or column
        if board.exists(Pattern("1648837428731.png").similar(0.72)):
            board.click(Pattern("1648837428731.png").similar(0.72).targetOffset(2,1))
        elif board.exists(Pattern("1648837512453.png").similar(0.72)):
            board.click(Pattern("1648837512453.png").similar(0.72))
            
        #checking for diagonal wins
        elif board.getCell(2,2).has(x) and board.getCell(0,0).has(empty):
                click(board.getCell(0,0))
        elif board.getCell(2,0).has(x) and board.getCell(0,2).has(empty):
                click(board.getCell(0,2))
        elif board.getCell(0,2).has(x) and board.getCell(2,0).has(empty):
                click(board.getCell(2,0)) 
        elif board.getCell(0,0).has(x) and board.getCell(220).has(empty):
                click(board.getCell(2,2))
    
        #checking whether the oponent is about to win next
        elif board.exists(Pattern("1649473011844.png").similar(0.92)):
            click(Pattern("1649473011844.png").similar(0.92))
        elif board.exists(Pattern("1649471460572.png").similar(0.92).targetOffset(0,75)):
                click(Pattern("1649471460572.png").similar(0.92).targetOffset(0,75))
        elif board.exists(Pattern("1649471555389.png").similar(0.73).targetOffset(72,-1)):
                click(Pattern("1649471555389.png").similar(0.73).targetOffset(72,-1))
        elif board.exists(Pattern("1649471621028.png").similar(0.92).targetOffset(-71,-5)):
            click(Pattern("1649471621028.png").similar(0.92).targetOffset(-71,-5))
        elif board.exists(Pattern("1649471945668.png").similar(0.92).targetOffset(1,-72)):
                click(Pattern("1649471945668.png").similar(0.92).targetOffset(1,-70))
        elif board.exists(Pattern("1650055700469.png").similar(0.83)):
            click(Pattern("1650055700469.png").similar(0.83))
        elif board.exists(Pattern("1650055853588.png").similar(0.84)):
            click(Pattern("1650055853588.png").similar(0.84))
    
        #if neither us nor our opponent can win on this turn, we populate the empty cells, prioritizing the corners, to make the game more predictible
        elif board.getCell(2,1).has(o) and board.getCell(0,2).has(empty):
            click(board.getCell(0,2))
        elif board.getCell(2,1).has(o) and board.getCell(0,1).has(empty):
            click(board.getCell(0,1))
        elif board.getCell(2,0).has(empty):
                click(board.getCell(2,0))
        elif board.getCell(2,2).has(empty):
                click(board.getCell(2,2))    
        else: board.click(empty)
                                                                                                                                                         
    
    #figuring out and storing the outcome of the game
    if exists(Pattern("1648839894974.png").similar(0.80)):
        result = "won"
    elif exists("1648838367087.png"):
        result = "tied"
    else: result = "lost"
    
    global screenshot     #declaring the screenshot as a global variable to be able to paste it outside of the function
    screenshot = capture(board) #we take a screenshot of the outcome 

#running the program
play()   
wait(3)   #we wait for a few seconds to observe the result