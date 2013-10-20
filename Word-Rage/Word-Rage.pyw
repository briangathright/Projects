'''Version 1.0 by Brian Gathright'''

from graphics import *
import time, random, pickle

entry = Entry(Point(150, 15), 16)


'''Sets up list to be used based off difficulty''' #Complete

def pickWords(dif):                             
    file = open(dif + 'Words.txt', 'r')
    words = file.read()
    words = words.splitlines()
    random.shuffle(words)
    file.close()
    return words

'''The actual falling of the words and score recording''' #Complete

def wordFall(words, speed, dif):
    win = GraphWin('Word-Rage', 300, 600)
    background(win)
    entry.draw(win)
    wL = 50
    wordsText = Text(Point(245, 40), wL)
    wordsText.setSize(10)
    wordsText.draw(win)
    score = 0
    scoreText = Text(Point(117, 40), score)
    scoreText.setSize(10)
    scoreText.draw(win)
    text = str(entry.getText())
    instruct = Text(Point(win.width/2, 350),
                    'Type "Start" to Begin')
    instruct.draw(win)
    
    while text.lower() != 'start':
        time.sleep(speed)
        text = str(entry.getText())
    instruct.undraw()
    entry.setText('')
    
    for word in words:
        y = 542
        point = (Point(win.width/2, y))
        invader = Text((point), word)
        invader.draw(win)
        while text != word:
            if y > 50:
                time.sleep(speed)
                invader.move(0, -5)
                y = y - 5
                text = str(entry.getText())
            else:
                invader.undraw()
                gameOver = Text(Point(win.width/2, 350), 'GAME OVER \n Click to Continue')
                gameOver.draw(win)
                wordLost = Text(Point(win.width/2, win.height/2), 'You lost on: \n "{}"'.format(word))
                wordLost.draw(win)
                win.getMouse()
                win.close()
                highScores(checkScores(score, dif), dif)
                return
                
        invader.undraw()
        scoreText.undraw()
        wordsText.undraw()
        if y >= 425:
            score = score + 100
        elif y >= 272:
            score = score + 75
        elif y >= 137:
            score = score +50
        else:
            score = score + 25
        scoreText = Text(Point(117, 40), score)
        scoreText.setSize(10)
        scoreText.draw(win)
        wL = wL - 1
        wordsText = Text(Point(245, 40), wL)
        wordsText.setSize(10)
        wordsText.draw(win)
        entry.setText('')
        if wL == 0:
            break
        
    winner = Text(Point(win.width/2, 350),
                  'YOU WIN \n Click to Continue')
    winner.draw(win)
    win.getMouse()
    win.close()
    highScores(checkScores(score, dif), dif)

'''Displays High Scores''' #Complete

def highScores(highScoresList, dif):
    win = GraphWin('High Scores', 300, 300)
    
    win.yUp()
    win.setBackground('green4')
    text = Text(Point(win.width/2, 250), 'High Scores')
    text.draw(win)
    x = 100
    y = 200
    
    for a,b in highScoresList:
        scoreText = Text(Point(x, y), a)
        scoreText.draw(win)
        nameText = Text(Point(x + 100, y), b)
        y = y - 50
        nameText.draw(win)
    text2 = Text(Point(win.width/2, 50),
                 'Thanks for Playing!\n Click to Quit')
    text2.draw(win)
    win.getMouse()
    win.close()
    
'''Checks to see if new highscore''' #Complete

def checkScores(score, dif):
   oldScores = open(dif + 'Scores.txt', 'rb')
   scoresList = pickle.load(oldScores)
   oldScores.close()
   lowScore, dummy = scoresList[-1]
   name = 'Anonymous'
   if score > lowScore or scoresList == list():
       win = GraphWin('New High Score!', 300, 300)
       win.yUp()
       win.setBackground('green4')
   
       text = Text(Point(win.width/2, 275),
               'New High Score!')
       text2 = Text(Point(win.width/2, 25), 'Enter Your Name then Click')
   
       entry = Entry(Point(win.width/2, win.height/2), 9)
       entry.draw(win)
       entry.setText('Anonymous')
       text.setSize(20)
       text.draw(win)
       text2.setSize(14)
       text2.draw(win)
       win.getMouse()

       name = str(entry.getText())
       win.close()
                
   newScore = (score, name)
       
   scoresList.append(newScore)
   scoresList.sort(reverse=True)
   scoresList.pop(3)   
   oldScores = scoresList
   saveOver = open(dif + 'Scores.txt', 'wb')
   pickle.dump(oldScores,saveOver)
   saveOver.close()
   return scoresList
                
''' Sets up the Background ''' #Complete

def background(win):
    win.yUp()
    win.setBackground('green4')

    background = list()

    title = Text(Point(win.width/2, 578), 'Word-Rage')
    title.setSize(30)
    background.append(title)
    
    rec = Rectangle(Point(50, 550), Point(250, 50))
    rec.setFill('white')
    background.append(rec)
    
    scoreLine100 = Line(Point(50, 425), Point(250, 425))
    scoreLine75 = Line(Point(50, 272), Point(250, 272))
    scoreLine50 = Line(Point(50, 137), Point(250, 137))
    background.append(scoreLine100)
    background.append(scoreLine75)
    background.append(scoreLine50)

    wordsRemainingText = Text(Point(195, 40), 'Words Left: ')
    wordsRemainingText.setSize(10)
    background.append(wordsRemainingText)
    scoreText = list()
    text1 = Text(Point(25, 425), '100')
    text2 = Text(Point(25, 272), '75')
    text3 = Text(Point(25, 137), '50')
    text4 = Text(Point(25, 50), '25')
    scoreText.append(text1)
    scoreText.append(text2)
    scoreText.append(text3)
    scoreText.append(text4)
    
    for text in scoreText:
        text.setSize(20)
        background.append(text)
        text = text.clone()
        text.move(250, 0)
        text.setSize(20)
        background.append(text)
    
    score = Text(Point(75, 40), 'Score:')
    score.setSize(10)
    background.append(score)

    for shape in background:
        shape.draw(win)

''' Checks to see which button is clicked ''' #Complete

def isBetween(x, end1, end2): 
    return end1 <= x <= end2 or end2 <= x <= end1

def isInside(point, rect):    
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return isBetween(point.getX(), pt1.getX(), pt2.getX()) and \
           isBetween(point.getY(), pt1.getY(), pt2.getY())

''' Makes the buttons ''' #Complete

def makeButton(corner, color, win):  
    corner2 = corner.clone()
    if color != 'red2':
        corner2.move(100, 400)
    else:
        corner2.move(200, 400)
    rect = Rectangle(corner, corner2)
    rect.setFill(color)
    rect.setOutline(color)
    rect.draw(win)
    return rect

''' The Main Menu + Which Game to Play''' #Complete

def main():
    win = GraphWin('Word-Rage', 300, 300) 
    win.yUp()

    easyBox = makeButton(Point(0, 0), 'green2', win)
    mediumBox = makeButton(Point(100, 0), 'orange2', win)
    hardBox = makeButton(Point(200, 0), 'red2', win)

    title = Text(Point(win.width/2, 250), 'Word-Rage')
    title.setSize(30)
    title.setFill('white')
    title.draw(win)

    instructions = Text(Point(win.width/2, 150),
                        'Choose a difficulty by clicking \n in its box.')
    instructions.setFill('white')
    instructions.draw(win)

    easy = Text(Point(50, 50), 'Easy')
    easy.setFill('white')
    easy.draw(win)

    med = Text(Point(150, 50), 'Medium')
    med.setFill('white')
    med.draw(win)

    hard = Text(Point(250, 50), 'Hard')
    hard.setFill('white')
    hard.draw(win)
    
    pt = win.getMouse()
    
    if isInside(pt, easyBox):
            win.close()
            wordFall(pickWords('easy'), .07, 'easy')
    elif isInside(pt, mediumBox):
            win.close()
            wordFall(pickWords('medium'), .05, 'medium')
    elif isInside(pt, hardBox):
            win.close()
            wordFallHard(pickWords('hard'), .07, 'hard')

'''Sets up special difficulty stuff for hard mode'''

def wordFallHard(words, speed, dif): #Complete
    win = GraphWin('Word-Rage', 300, 600)
    background(win)
    entry.draw(win)
    wL = 50
    wordsText = Text(Point(245, 40), wL)
    wordsText.setSize(10)
    wordsText.draw(win)
    score = 0
    scoreText = Text(Point(117, 40), score)
    scoreText.setSize(10)
    scoreText.draw(win)
    text = str(entry.getText())
    instruct = Text(Point(win.width/2, 350),
                    'Type "Start" to Begin')
    instruct.draw(win)
    
    while text.lower() != 'start':
        time.sleep(speed)
        text = str(entry.getText())
    instruct.undraw()
    entry.setText('')
    
    for word in words:
            y = 542
            x = 150
            point = (Point(x, y))
            invader = Text(point, word)
            invader.draw(win)
            while text != word:
                if y > 50:
                    time.sleep(speed)
                    r = random.randrange(256)
                    b = random.randrange(256)
                    g = random.randrange(256)
                    color = color_rgb(r, g, b)
                    invader.setFill(color)
                    if x > 151:
                      a = -20
                      b = random.randrange(-10, -6)
                      y = y + b
                      x = x + a
                      invader.move(a, b)
                      text = str(entry.getText())
                    elif x < 151:
                      a = 20
                      b = random.randrange(-10, -6)
                      y = y + b
                      x = x + a
                      invader.move(a, b)
                      text = str(entry.getText())
                else:
                      invader.undraw()
                      gameOver = Text(Point(win.width/2, 350), 'Game Over \n Click to Continue')
                      gameOver.draw(win)
                      wordLost = Text(Point(win.width/2, win.height/2), 'You lost on: \n "{}"'.format(word))
                      wordLost.draw(win)
                      win.getMouse()
                      win.close()
                      highScores(checkScores(score, dif), dif)
                      return
                    
            invader.undraw()
            wordsText.undraw()
            scoreText.undraw()
            if y >= 425:
                score = score + 100
            elif y >= 272:
                score = score + 75
            elif y >= 137:
                score = score + 50
            else:
                score = score + 25
            scoreText = Text(Point(117, 40), score)
            wL = wL - 1
            wordsText = Text(Point(245, 40), wL)
            wordsText.setSize(10)
            wordsText.draw(win)
            scoreText.setSize(10)
            scoreText.draw(win)
            entry.setText('')
            if wL == 0:
                break

    winner = Text(Point(win.width/2, 350),
                    'YOU WIN \n Click to Continue')    
    winner.draw(win)
    win.getMouse()
    win.close()
    highScores(checkScores(score, dif), dif)
            
main()   

