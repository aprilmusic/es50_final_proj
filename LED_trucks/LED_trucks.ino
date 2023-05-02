// testshapes demo for RGBmatrixPanel library.
// Demonstrates the drawing abilities of the RGBmatrixPanel library.
// For 32x64 RGB LED matrix.

// WILL NOT FIT on ARDUINO UNO -- requires a Mega, M0 or M4 board

#include <RGBmatrixPanel.h>

// Most of the signal pins are configurable, but the CLK pin has some
// special constraints.  On 8-bit AVR boards it must be on PORTB...
// Pin 11 works on the Arduino Mega.  On 32-bit SAMD boards it must be
// on the same PORT as the RGB data pins (D2-D7)...
// Pin 8 works on the Adafruit Metro M0 or Arduino Zero,
// Pin A4 works on the Adafruit Metro M4 (if using the Adafruit RGB
// Matrix Shield, cut trace between CLK pads and run a wire to A4).

//#define CLK  8   // USE THIS ON ADAFRUIT METRO M0, etc.
//#define CLK A4 // USE THIS ON METRO M4 (not M0)
#define CLK 11 // USE THIS ON ARDUINO MEGA
#define OE   9
#define LAT 10
#define A   A0
#define B   A1
#define C   A2
#define D   A3

RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false, 64);
int pixels[32];
int num_people;
int pixel_index;
String truck_color_1;
String truck_color_2;
String truck_color_3;



char startMarker = ';';
char endMarker = ',';

char integer[4];

byte newData = false;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);

  matrix.begin();
  num_people = 0;
  memset(pixels,0,sizeof(pixels));
  

  // fill the screen with 'black'
  matrix.fillScreen(matrix.Color333(0, 0, 0));
  // matrix.drawPixel(16, 16, matrix.Color333(0, 7, 0));

  
  // draw a pixel in solid white
  //matrix.drawPixel(0, 0, matrix.Color333(7, 7, 7));
  //delay(500);

  // fix the screen with green
  //matrix.fillRect(0, 0, matrix.width(), matrix.height(), matrix.Color333(0, 7, 0));
  //delay(500);

  // draw a box in yellow
  //matrix.drawRect(0, 0, matrix.width(), matrix.height(), matrix.Color333(7, 7, 0));
  //delay(500);

  // draw an 'X' in red
  //matrix.drawLine(0, 0, matrix.width()-1, matrix.height()-1, matrix.Color333(7, 0, 0));
  //matrix.drawLine(matrix.width()-1, 0, 0, matrix.height()-1, matrix.Color333(7, 0, 0));
  //delay(500);

  // draw a blue circle
  //matrix.drawCircle(10, 10, 10, matrix.Color333(0, 0, 7));
  //delay(500);

  // fill a violet circle
 // matrix.fillCircle(40, 21, 10, matrix.Color333(7, 0, 7));
 // delay(500);

  
  //matrix.drawRect(28, 15, 20, 9, matrix.Color333(7,7,0));
  //matrix.drawRect(40, 9, 12, 9, matrix.Color333(0,0,7));
  
  matrix.drawLine(28, 15, 48, 19, matrix.Color333(7,7,0));
  matrix.drawLine(28, 24, 48, 28, matrix.Color333(7,7,0));
  matrix.drawLine(28, 15, 28, 24, matrix.Color333(7,7,0));
  matrix.drawLine(48, 19, 48, 28, matrix.Color333(7,7,0));
  
  matrix.drawLine(34, 9, 48, 12, matrix.Color333(0,0,7));
  matrix.drawLine(34, 15, 48, 18, matrix.Color333(0,0,7));
  matrix.drawLine(34, 9, 34, 15, matrix.Color333(0,0,7));
  matrix.drawLine(48, 12, 48, 18, matrix.Color333(0,0,7));

  //matrix.drawPixel()
  
  
  // draw some text!
  matrix.setTextSize(1);     // size 1 == 8 pixels high
  matrix.setTextWrap(false); // Don't wrap at end of line - will do ourselves

  matrix.setCursor(52, 0);    // start at top right, with 12 pixels of spacing from the right
  uint8_t w = 0;
  char *str = "20";
  for (w=0; w<8; w++) {
    matrix.setTextColor(Wheel(w));
    matrix.print(str[w]);
  }
  // matrix.setCursor(2, 8);    // next line
  // for (w=8; w<18; w++) {
  //   matrix.setTextColor(Wheel(w));
  //   matrix.print(str[w]);
  // }
  // matrix.println();
  // matrix.setTextColor(matrix.Color333(7,7,7));
  // matrix.println("");

  // print each letter with a rainbow color
  
  // whew!
}




void loop() {
  int tuple[2];
  char rc;
  boolean recvInProgress = false;
  // matrix.drawPixel(0, num_people, matrix.Color333(0, 0, 7));

  while (!Serial.available()) {
     // If not available, a red dot
    matrix.drawPixel(12, 12, matrix.Color333(7, 0, 0));

   }
  matrix.drawPixel(16, 16, matrix.Color333(0, 0, 0));

  // int ndx = 0;
  // while (Serial.available() > 0) {
  //   rc = Serial.read();
  //   matrix.drawPixel(10,5, matrix.Color333(7, 7, 7));
  //   if (recvInProgress == true) {
  //       if (rc != endMarker) {
  //         matrix.drawPixel(ndx, 10, matrix.Color333(0, 0, 7));
  //         //  matrix.drawPixel(5,10, matrix.Color333(0, 0, 7));
  //           delay(400);
  //           integer[ndx] = rc;
  //           ndx += 1;
  //         matrix.drawPixel(ndx-1, 10, matrix.Color333(0, 0, 0));
  //           if (ndx >= 4) {
  //               ndx = 4 - 1;
  //           }
  //       }
  //       else {
  //           matrix.drawPixel(ndx, 10, matrix.Color333(0, 0, 7));
  //           integer[ndx] = '\0'; // terminate the string
  //           pixels[pixel_index] = atoi(integer);
  //           pixel_index += 1;
  //           recvInProgress = false;
  //           matrix.drawPixel(ndx, 10, matrix.Color333(0, 0, 0));
  //           ndx = 0;
            
  //           delay(400);
  //       }
  //   } else if (rc == startMarker) {
  //           recvInProgress = true;
  //           matrix.drawPixel(5,10, matrix.Color333(0, 0, 7));
  //           delay(400);
  //       }
  // }
  // String python_output = Serial.readStringUntil('\n');
  // pixels[0] = python_output.substring(0,2).toInt();
  // for (int i = 1; i < 30; i++){
  //   pixels[i] = python_output.substring(2*i, 2*i + 2).toInt();
  // }
  // // sscanf(python_output.c_str(), "%s,%s,%s,%s,%s,%s", &pixels[0], &pixels[1], &pixels[2], &pixels[3], &pixels[4], &pixels[5]);
  // matrix.drawPixel(pixels[0], 1, matrix.Color333(0, 7, 0));
  //  matrix.drawPixel(pixels[1], 2, matrix.Color333(0, 7, 0));
  //   matrix.drawPixel(pixels[2], 3, matrix.Color333(0, 7, 0));
  //    matrix.drawPixel(pixels[3], 4, matrix.Color333(0, 7, 0));
  //     matrix.drawPixel(pixels[4], 5, matrix.Color333(0, 7, 0));
  // matrix.drawPixel(pixels[5], 6, matrix.Color333(0, 7, 0));

  
  // int a, b, c, d;
  // sscanf(Serial.readString().c_str(), "%2d,%2d,%2d,%2d", &a, &b, &c, &d);
  //   matrix.drawPixel(a, b, matrix.Color333(0, 7, 0));
  // matrix.drawPixel(c, d, matrix.Color333(0, 7, 0));
  // sscanf(Serial.readString().c_str(), "%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d,%2d", \ 
  //   &pixels[0], &pixels[1], &pixels[2], &pixels[3], &pixels[4], &pixels[5], &pixels[6], &pixels[7], &pixels[8], &pixels[9], \
  //   &pixels[10], &pixels[11], &pixels[12], &pixels[13], &pixels[14], &pixels[15], &pixels[16], &pixels[17], &pixels[18], &pixels[19], \
  //   &pixels[20], &pixels[21], &pixels[22], &pixels[23], &pixels[24], &pixels[25], &pixels[26], &pixels[27], &pixels[28], &pixels[29]);

  delay(100);

  

  // BELOW IS WHAT WE ACTUALLY USE

  String python_output = Serial.readString();
  if (python_output == "new") {
    
    matrix.drawPixel(6, 6, matrix.Color333(0, 7, 0));
    for (int i=0; i<num_people; i++) {
      matrix.drawPixel(pixels[2*i], pixels[2*i+1], matrix.Color333(0, 0, 0));
      delay(100);
    }
    
    matrix.drawPixel(0, num_people, matrix.Color333(0, 0, 0));
    
    num_people = 0;
    
  } else if (python_output.substring(0, 5) == "truck") {
    if (python_output.substring(5, 6) == "1"){
      truck_color_1 = python_output.substring(6, python_output.length());
    } else if (python_output.substring(5, 6) == "2"){
      truck_color_2 = python_output.substring(6, python_output.length());
    } else if (python_output.substring(5, 6) == "3"){
      truck_color_3 = python_output.substring(6, python_output.length());
    } 
    

  } else {
    sscanf(python_output.c_str(), "%2d,%2d", &tuple[0], &tuple[1]);

    pixels[num_people * 2] = tuple[0];  
    pixels[num_people * 2+1] = tuple[1];
    num_people += 1;
    
    // matrix.drawPixel(0, num_people, matrix.Color333(0, 0, 0));
    // If available, a green dot
    matrix.drawPixel(12, 12, matrix.Color333(0, 7, 0));
    // delay(10000);

    // for (int i=0; i<num_people; i++){
    //   PeopleBitMap[pixels[2*i]*64 + pixels[2*i+1]] = 0xFFFF;
    // }
    for (int i=0; i<num_people; i++) {
      matrix.drawPixel(pixels[2*i], pixels[2*i+1], matrix.Color333(0, 7, 0));
      delay(100);
    }

  }

  
}


// Input a value 0 to 24 to get a color value.
// The colours are a transition r - g - b - back to r.
uint16_t Wheel(byte WheelPos) {
  if(WheelPos < 8) {
   return matrix.Color333(7 - WheelPos, WheelPos, 0);
  } else if(WheelPos < 16) {
   WheelPos -= 8;
   return matrix.Color333(0, 7-WheelPos, WheelPos);
  } else {
   WheelPos -= 16;
   return matrix.Color333(WheelPos, 0, 7 - WheelPos);
  }
}
