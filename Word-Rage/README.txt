README.txt

Word-Rage.pyw is the main function. Run this to play the game.
Once opened, the player picks a difficulty, easy/medium/hard.
The player follows in game instructions to start the game.
Words will fall from the top of the screen to the bottom.
The player must type them to "destroy" them before they reach
the bottom. If they reach the bottom the player loses.
The word they lost on is displayed for their frustration.
The faster a word is typed the more points the player receives.
If the player has a high score (top 3) they will be prompted for
their name. They will then be shown the high scores, with their name
included. The words used and the way they fall are based off the
difficulty the choose. Each difficulty has their own high scores.

resetScores.pyw resets the high scores used in Word-Rage.pyw.
Run it if you want all scores to reset to "0000 Anonymous".
Note: running the program (outside of idle) will show no indication
it ran. Rest assured it did. Simply play the game again and see the scores
have been reset.

easyScores.txt, mediumScores.txt, and hardScores.txt hold the
lists of high scores used in Word-Rage.pyw and can be reset by
running resetScores.pyw. These CANNOT be hand edited because they
are in "pickled" format. These files should not be opened or messed 
with. If you DO open them, make sure not to make any changes or they
will become corrupt. If they DO become corrupt, simply delete the file
and run resetScores.pyw to recreate the default lists.

easyWords.txt, mediumWords.txt, and hardWords.txt hold the
lists used for the different difficulties in Word-Rage.pyw.
You can open these files to view the words and even add your
own words(one per line).

graphics.py and graphics.pyc are needed for the graphics module.



