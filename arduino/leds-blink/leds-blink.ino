// declare pins to blink leds
int led1=13;

//array of leds
int leds[5]={led1};

void setup() {
// setting all declared pins as outputs
    pinMode(led1,OUTPUT);
}

void loop() {
//function to blink leds
  //blink_leds();
   digitalWrite(led1,HIGH);
    delay(200);
    digitalWrite(led1,LOW);
    delay(200); 
}
//void blink_leds(){
//// loop over the pins in the array and perform writing the high and low
//  for (int i=0;i<sizeof(leds);i++){
//    digitalWrite(leds[i],HIGH);
//    delay(70);
//    digitalWrite(leds[i],LOW);
//    
//    }
//  }
