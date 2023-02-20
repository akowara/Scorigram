import pandas as pd
from array import *
from datetime import datetime
from random import random

class Game:
    def __init__(self, ptsW, ptsL, count, lastGame):
        self.ptsW = ptsW
        self.ptsL = ptsL
        self.count = count
        self.lastGame = lastGame

def downloadScores():
    url = "https://www.pro-football-reference.com/boxscores/game-scores.htm"
    html_content = pd.read_html(url)
    table = html_content[0]
    table.to_csv("csv/scores.csv")

def getScores():
    df = pd.read_csv('csv/scores.csv')
    scores = []
    for i in df.index:
        scores.append(Game(df['PtsW'][i],df['PtsL'][i],df['Count'][i],df['Last Game'][i]))
    return scores

def scoresMatch(input1, input2, ptsW, ptsL):
    if input1 == ptsW and input2 == ptsL:
        return True
    elif input1 == ptsL and input2 == ptsW:
        return True
    else:
        return False
       
# getGames()
score1 = int(input("Enter the home team score: "))
score2 = int(input("Enter the away team score: "))
scores = getScores()

for i in range(len(scores)):
    if scoresMatch(score1, score2, scores[i].ptsL, scores[i].ptsW) == True:
        answer = "The score happened " + str(scores[i].count) + " times. Most recently: " + scores[i].lastGame
        print(answer)
        exit()

print("This is a scorigram.")
    



