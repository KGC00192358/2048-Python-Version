This is a project about machine learning. I am trying to see if I can design a program in such a way that it can determine a way to play and win a game of 2048.
For anyone unfamiliar, 2048 is a game that is played on a 4 by 4 grid or cells, starting with a 2 or 4 in one of the cells. Then the player can select a direction(Up, Down, left, right) 
and that two goes to farthest possible cell in a straight line from where it started along the chosen direction. Then another 2 or 4 is added somewhere in the grid.
The player is then free to select another direction. Whenever two numbers of the same value meet, they are added together in the cell of the farthest on along the direction.
(ie [2][][][] down [][][][] ).  
(   [2][][][]      [][][2][])              
(   [][][][]       [][][][] )
(   [][][][]       [4][][][])

The objective is to add numbers in this way to obtain a cell equaling 2048 and the lose is condition is a full board and if there are no moves  
that would add two numbers to make a space.My version is simplified, I am only adding in 2s instead of 2s and 4s.
Currently, I only have a wide hueristic for determining a moved based off of a numeric value, I am planning on adding in more huerstics, as well a "memory"
file for the computer to look at and determine a good move. Hopefully, I can eventaully have a computer learn and guess correct moves to win a game from any given 
starting two position.
