# Copter-propeller-project
## Introduction
With the emergence of the MATLAB/Simulink graphical programming  environment, modeling and simulation of various plants and controllers  can be accomplished quite easily by students who might not have  extensive training in digital control and numerical methods. However,  practical implementation of such controllers remains elusive for most  undergraduate students. Therefore, the objective of this project is to  develop a simple physical plant that can be used seamlessly with the  MATLAB/Simulink simulation environment to allow students to  implement and test real-time controllers using implemented in code.  The project described here provides some practical experience for  students, using an inexpensive and portable setup that can be taken  home. The experiment is designed following the principles of variational theory of learning developed by Marton and coworkers [1], [2] and the  approach of guided discovery/interactive-engagement labs  characteristic of several well-known labs, such as the Modeling  Workshop Project [3], Socratic Dialogue Inducing Labs [4], Real Time  Physics [5], and Tools for Scientific Thinking [6]. The portability and low  cost of the setup allows the students to conduct experiments over two  semesters and use the device to complete a semester project. In  addition to significantly reducing the cost of offering an experimental  component, the experimental set up built by the students provides an  opportunity to demonstrate concepts from system identification, digital  control and nonlinear feedback control.
## Led Blink

```cython
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}
```
Sample Video for [Led blink](https://drive.google.com/file/d/1b4jLMXk14badw5VmU_krSFCpEChm_EHU/view?usp=sharing)

## Driving Copter Motor

### components

* copter motor (_**A2212/13T 1000KV**_)
* Arduino UNO 
* Jumper wires
* Motor Driver
* Potentiometer
* Toggle switch
* Breadboard
* Breadboard power supply
* Power adapter

### Schematic 

link to the [schematic]()

To run and control the motor a high level language (python) and C++ codes were necessary.
 ### procedure of uploading the codes

- After doing all the connections from the schematic above, open arduino IDE.
- 