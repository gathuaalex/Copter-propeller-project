int led1=13,led2=12,led3=11,led4=10,led5=9;

//array of leds
int leds[5]={led1,led2,led3,led4,led5};

void setup() {
    pinMode(led1,OUTPUT);
    pinMode(led2,OUTPUT);
    pinMode(led3,OUTPUT);
    pinMode(led4,OUTPUT);
    pinMode(led5,OUTPUT);
}

void loop() {
  blink_leds();

}
void blink_leds(){
  for (int i=0;i<sizeof(leds);i++){
    digitalWrite(leds[i],HIGH);
    delay(70);
    digitalWrite(leds[i],LOW);
    }
  }
