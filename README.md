# Rubik’s cube solver

We made a bot which can solve Rubik’s cube. We have used two motors for achieving this. A stepper motor is used on which scrambled  Rubik’s cube is placed. It can rotate the cube in an angle that we need. A hand like structure made of ice cream sticks is attached to the servo motor which can push if moved a certain angle forward  followed by backwards.  Pushing makes the cube’s front face to go top, top face to back and similarly for the other two faces. It can be made to hold the top two rows of the cube by decreasing some  angle. When the cube is made to rotate while the hand is holding, only the down row will be rotated. From this, we wrote three basic functions: 
*	Rotate
*	Push
*	Hold and rotate
## Software description:
Input is to be given in a user-friendly GUI window made using PyQt. Then, the program converts it to a 54 character string  of orientations of the cube . We have used a library called Kociemba. It has a function which takes input as the current state of Rubik's cube as a string and returns the steps to be followed to solve the cube. The output steps can be: rotate Left, Right, Up, Down, Front, Back. They can also be the reverse of each these steps or double of these steps respectively. So, totally there are 18 possibilities. Two – phase algorithm is used to find the best possible combination of m   oves to solve the cube. On an average, it takes 19 moves to solve. Now, our python code formats this output. It sends the message to Arduino using functions from PySerial module. The C++ code written in Arduino IDE will receive  the steps one by one and executes them. As this bot cannot rotate the cube in all directions, the algorithm is written in such a way that, by pushing and rotating , it places the face that is to be turned on the stepper motor and then hold and rotate is performed. Again by some sequence of pushes and rotates, the cube is put in initial position. 

# Libraries used:
* [Kociemba]  - Algorithm for solving Rubik's cube
* [PyQt] - GUI for input
* [pyserial] - To send instructions to Arduino IDE from Python

This is the video of our bot solving Rubik's cube: https://www.youtube.com/watch?v=iySgEFEIhY4

[Kociemba]: <https://pypi.python.org/pypi/kociemba/1.1>
[PyQt]: <https://riverbankcomputing.com/software/pyqt/intro>
[pyserial]: <https://pypi.python.org/pypi/pyserial>
