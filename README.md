# Engineering 4 Notebook
##What I've Learned
1) 0.125 inches (the thickness of acrylic) is 3.125mm
2) Support material costs a lot of money and your parts should be designed/oriented to minimize its use
3) Having a plan and not following it is better than not having a plan at all; uit's important to organize your ideas and find the order of operations of fabrication that will streamline your workflow.
4) Things always take longer than you think they will.
5) Take pride in your work, even if it's not perfect.
## Dice Roller
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/Atomic%20Dice%20Roller.py)
### Lessons Learned
This was our first python assignment, so we learned about 'while' loops, the randint function, and the basic syntax of python. Our main issue was how to get the loop to stop, how to get the Pi to detect input, or, more accurately, how to use that input to impact the code. 

## Calculator
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/MrModulo.py)
### Lessons Learned
Following the rousing success of our first assignment we moved onto our calculator, which we so aptly name Mr. Modulo. The main lesson to be gained from this assignment is that the little stuff matters. We had been completely done with this for about thirty minutes, just trouble shooting nonstop, until we were told our issue was we needed a space between some numbers and some commas. And that fixed it. Gotta pay attention to that sweet, sweet syntax. Along that same line, we learned about str vs int, which is an interesting difference for someone coming over from Arduino.

## Quadratic Solver
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/Quadratic%20Solver%202.py)
### Lessons Learned
We made this assignment twice. The first time we did it, we made an adequate quadratic solver that solved all the equations, hurray we did it, hurrah. But as it turns out, we did it using the incorrect terminology. We hadn't used a formula. So we just defined one and told it to do it. The fix wasn't that complicated, but we did learn to read the canvas page more carefully, because that's a real time saver, not having to do an assignment over again. Also, ^ does not mean to the power. ** is powers. Who knew?

## String and Loops
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/Split.py)
### Lessons Learned
We made this assignment more complicated than it needed to be, trying to have for loops inside of for loops inside of for loops, which we attempted but realized was very unnecessary. We learned how to properly use strings in this assginment, which I guess was kind of the point.

## Hangman
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/Hangman.py)
### Lessons Learned
We spent a lot of time on this assignment, simply because we had a lot of fun doing it. The biggest problem we faced was getting the guessed letters to display once they had guessed. But because we did this assignment in little chunks, this didn't affect the rest of the code. This one was a lot of fun.

## GPIO Assignment - Bash
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Scripts/GPIOPins1.sh)
### Lessons Learned
This assignment basically gave us the code, but we learned the basics of GPIO stuff with the Pi while doing it. Jack also got to solder, Jack loves soldering.

## GPIO Assignment - Python
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/GPIOPins.py)
### Lessons Learned
We merged GPIO and Python for this assignment, which once again was prety straightforward. It was interesting to see the differences between the two types of pin numbering.

## GPIO Assignment - SSH
### Code
There ain't none.
### Lessons Learned
We had trouble connecting the phone, we tried all sorts of stuff but it didn't work until we downloaded a different app, because the three others we tried weren't good enough apparently.

## Hello Flask
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/Flask/hello_world/app.py)
### Lessons Learned
Flask is cool! This assignment gave us the code too, but it was still neat to be able to control a Pi over the internet! It was also important to learn that the IP address changes a lot. 

## GPIO Assignment - Flask
### [Code](https://github.com/Engineering_4_Notebook/blob/master/Python/Flask/gpio)
### Lessons Learned
We had a couple typos in the first half of the assignment where it gave us the code, which tripped us up but was solved fairly quickly. The other issue we ran into was with the switches on the site. How they worked and if we were going to use a toggle, buttons, or whatever else. We ended up using radio buttons and a submit button.

## GPIO Assignment - I2C
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/GPIOPinsI2C.py)
### Lessons Learned
A lot of this assignment was getting the libraries set up, these I2C devices are super cool and it was great to learn about them. Once everything worked, we just had to go through the example code and find out what did what in order to mash them together.

## Headless
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/Headless.py)
### Lessons Learned
We didn't do this assignment as well as we could have, personally I'd like to come back and do a better job of it. It was cool to have the code run automatically without a monitor or mouse or keyboard, but the code was super simple and less visually interesting than it could have been.

## Pi Camera 
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/Camera.py)
### Lessons Learned
We had some trouble getting the preview of the camera to disappear, we ended up using CTRL + C but that often didn't work, meaning we had to reboot the Pi every time it got stuck. The rest of the assignment wasn't too bad, and now we know how to use the camera. The effects were a lot of fun.

## Hack Your Stuff
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/AlarmHacking.py)
### Lessons Learned
The sound the alarm makes is the worst thing in the world. We first used a different type of buzzer, which didn't work because it required an oscillating current, but once we found the correct one the only difficulty was finding the value of the photoresistor which we could read and use in the code. 

## Copypasta - Parent Detector
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/ParentDetector.py)
### Lessons Learned
This assignment was just following a tutorial, we had a little trouble because the motion detector would always detect motion, or rather, infared radiation. The code, as far as we can tell, though, works.

## Copypasta - Push Button Stop Motion
### [Code](https://github.com/jantes86/Engineering_4_Notebook/blob/master/Python/StopAnimation.py)
### Lessons Learned
This took a while simply because downloading the avconv stuff took AGES to download. Other tha that, this was a lot of fun and we quickly used up all the memory on our Pi by making stop-motion videos.
