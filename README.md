# LOZ10
Making Items  

In this lesson we will be making items for the game.  Start by using game1.7.1.py because it has some bug fixes that I talk about in the video, it is coded to work with python_functions7.  All png files should be downloaded and placed in the same folder as your game file.  If you get stuck then the completed code from the video is game1.8.

Video - YouTube - https://youtu.be/m8Eb5ySOoPM  
Video - EdPuzzle - https://edpuzzle.com/media/5f1b3923b5381c3f2cf05bd7   
Slides - https://docs.google.com/presentation/d/1uO5lS8YK4p_66i0E2oaMRunPzeWOfrFp1fQsVdKIKF4/edit?usp=sharing  

Extensions-  
1. Create Items for the bomb, fairy, and clock.  Make classes for them inheriting the Item class.   
  -Bomb should have the parameter self.bomb=1.  It is not animated.  
  -Fairy should have the parameter self.health = 15.  It is animated.  
  -Clock should have the parameter self.time =1.  It is not animated.  
2. Code the if block so that enemies drop these items if they are killed.
3. Add a parameter to each of your enemies called self.type.  Make some of your enemies be types "A" through "D".
4. In the if block when calling dropChart, use enemy.type for the second parameter

Challenge-
1. In the fairy class add to the animate method so that it randomly moves all of the screen after it is dropped by an enemy.
2. You will need to add a speed parameter to the fairy class.  You don't want it to be faster than link.
3. Fairies actually can move through walls and leave the scene so don't worry about controlling for those collisions.
