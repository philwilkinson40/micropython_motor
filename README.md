# micropython_motor
really basic overview of how to get started controlling motors using micropython

Stepper motors offer good control and torque. 
I bought a very cheap starter motor with controller board for under $10 to check the basics.

!(BYJ48-StepperMotor_ULN2003Driver.jpg)

I connected: 

| BYJ48  | Wemos |
| ------------- | ------------- |
| -  | GND  |
| +  | 5V  |
| INT1 | GPIO5 |
| INT2 | GPIO4 |
| INT3 | GPIO0 |
| INT4 | GPIO2 |

 
 

A few people had written drivers in Python but I am not sure why they bothered.  
The stepper motor script is really basic, no I2C or SPI   
just turn on then off each GPIO in sequence, for each available step in the motor.

to reverse the direction of the motor, just reverse the switching sequence.  
I did this by putting the GPIOs in a list then simply reversing the list order

!(https://www.youtube.com/watch?v=7Vcm3LxTMI8)