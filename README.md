# monomepi step sequencer

monome + raspberry pi + arduino + python  
(and a bunch of servos, some lego and a glockenspiel)

[![play](http://i.imgur.com/2Xyrm51.png)]
(https://vimeo.com/178279145)

### What's this, then?

This is code for a step sequencer program that uses a monome as input controller, and a toy glockenspiel as the output instrument.


### How does it work?

The brain is a Raspberry Pi 3 which runs the step sequencer program, written in python. The monome is connected to the Pi via USB. An Arduino Uno is also connected to the Pi via USB. The Arduino controls 8 servos, each with a "mallet" attached. (These mallets are actually Lego bricks clumsily taped onto coffee sticks.)

The Arduino is programmed to receive serial commands\* from the python program. A command is one byte or 8 bits, each bit representing 'on' (play the note) and 'off' (do nothing) states of each servo.

The monome is totally controlled by the python program. The program sends serial commands that, for example, tell the monome which buttons need to light up or turn off. It also *receives* serial data from the monome - like, which buttons are getting pressed and depressed.

\* *For raw serial communications, the `pyserial` library has been most invaluable.*


### I like the use of Lego and toy glockenspiel!

My toddler already has them so I just borrowed. She doesn't mind (I think) ;)


### Other related projects?

* Conway's Game of Life https://vimeo.com/65304931
* Twitter Feed Display https://vimeo.com/67579615
* Monome + Arduino + Servo https://vimeo.com/96793877
