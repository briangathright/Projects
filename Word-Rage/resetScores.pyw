import pickle

'''Resets the score files used in Word-Rage.pyw'''

def scoreReset(scores):
    for score in scores:
        file = open(score, 'wb')
        reset = list([(0000, 'Anonymous'), (0000, 'Anonymous'),
                      (0000, 'Anonymous')])
        
        pickle.dump(reset,file)
        file.close()
    print('All Scores Have Been Reset!')
        
scoreReset(('easyScores.txt', 'mediumScores.txt', 'hardScores.txt'))

        
    
