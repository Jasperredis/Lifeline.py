# Lifeline.py 1.0
This is a guide to playing and interacting with Lifeline.py, version 1.0!  
Note that this **IS** a stable release, yet it does not have all of the features originally intended for this game.
https://jasperredis.github.io/lifelinepy.github.io/

# Title Screen
* **Start:** Starts a game. Kind of obvious.
* **Options:** The options. Again, kind of obvious. Below is a list of them:
  * *Background:* Changes the background colour.
  * *More coming soon!*
* **Updates:** Takes the GitHub repository for the website and fetches update data. **Basically, tells you info about the latest version, and provides a link to update if you're not running the latest.**
* **Difficulty:** Changes the difficulty. **Note that as of right now in 1.0, the optimal gameplay is only in the default, Normal, or the yellow heart.**

# Gameplay
* **Bar:** Lifeline.py's gameplay takes place on a bar. This bar is at dead centre of the screen.
* **Player:** You, the player, are a white line on the bar. You can move with the A and D keys, and mouse-controlled movement is going to be added in future updates.
* **Life:** You have a life counter. This ticks down every few seconds. Once it hits 0, it's game over. It starts at 5.
* **Heals:** These spawn in random positions. These are green lines, the same size as you, that heal you by one health point to prevent your death.
* **Enemies:** These also spawn in random positions. These are lines, just like heals and the player, but are red, and damage you further than you already have been damaged.
* **Protection:** You get a cooldown after getting hit by an enemy that prevents you from taking enemy damage for a short amount of time, under a second.
* **Scores:**
  * **Main Score:** The score for the game you're currently playing. As of right now, the only way to get it is for 50 points whenever your life ticks down.
  * **Highscore:** Obvious, but the highest score you've ever gotten. It's displayed in-game so you can see your goal to beat.
  * **Totalscore:** This is the collected score of every game you've ever played. This can only be seen at game over.

# Controls
* **Navigate up on GUI:** Up Arrow
* **Navigate down on GUI:** Down Arrow
* **Select one option down in setting on GUI:** Left Arrow
* **Select one option up in setting on GUI:** Right Arrow
* **Move right:** D
* **Move left:** A
* **Pause:** Escape
* **Select option on GUI:** Enter
* **Update on Update menu:** U
https://jasperredis.github.io/lifelinepy.github.io/

# GitHub Info:
* *Lifeline.py* is made **100%** in Python.
* uhhh thats all ig

# MIT License
Copyright (c) 2024 jasperredis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
