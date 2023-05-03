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
int pixels[64];
int num_people;
int pixel_index;
char truck_color_1;
char truck_color_2;
char truck_color_3;

uint16_t truck_color_1_matrix;
uint16_t truck_color_2_matrix;
uint16_t truck_color_3_matrix;

int x_boundary = 25;
int y1_boundary = 9;
int y2_boundary = 18;

// Define Time Increments
int time_inc = 2;



char startMarker = ';';
char endMarker = ',';

char integer[4];

int numbers[3];
// numbers[0] = "20";
// numbers[1] = "20";
// numbers[2] = "20";

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


  //matrix.drawPixel()

  // White Lines For Background
  matrix.drawLine(0, 12, 30, 32, matrix.Color333(3,3,3));
  matrix.drawLine(0, 17, 13, 32, matrix.Color333(3,3,3));

  // fill circle
  matrix.fillCircle(1, 31, 2, matrix.Color333(2, 7, 2));
  matrix.fillCircle(1, 29, 2, matrix.Color333(0, 7, 0));
  matrix.fillCircle(1, 26, 2, matrix.Color333(1, 7, 1));
  matrix.fillCircle(3, 31, 2, matrix.Color333(0, 7, 0));
  matrix.fillCircle(0, 24, 1, matrix.Color333(4, 7, 4));
  matrix.fillCircle(0, 23, 2, matrix.Color333(0, 7, 0));
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



void update_numbers() {
  for (int i=0; i < num_people; i++){
  
            // Define Boundaries
      
}
}



void loop() {
  int tuple[2];
  char rc;
  boolean recvInProgress = false;
  // matrix.drawPixel(0, num_people, matrix.Color333(0, 0, 7));

  // truck 1
  if (truck_color_1 == 'b') {
    truck_color_1_matrix = matrix.Color333(1,2,7);
  } else if (truck_color_1 == 'y') {
    truck_color_1_matrix = matrix.Color333(7,7,0);
  } else if (truck_color_1 == 'r') {
    truck_color_1_matrix = matrix.Color333(7,0,0);
  } else {
    truck_color_1_matrix = matrix.Color333(3,3,3);    
  }


  matrix.drawLine(26, 16, 44, 19, truck_color_1_matrix);
  matrix.drawLine(26, 24, 44, 26, truck_color_1_matrix);
  matrix.drawLine(26, 16, 26, 24, truck_color_1_matrix);
  matrix.drawLine(44, 19, 44, 26, truck_color_1_matrix);
  
  // truck 2
  if (truck_color_2 == 'b') {
    truck_color_2_matrix = matrix.Color333(1,2,7);
  } else if (truck_color_2 == 'y') {
    truck_color_2_matrix = matrix.Color333(7,7,0);
  } else if (truck_color_2 == 'r') {
    truck_color_2_matrix = matrix.Color333(7,0,0);
  } else {
    truck_color_2_matrix = matrix.Color333(3,3,3);    
  }
  matrix.drawLine(34, 9, 48, 12, truck_color_2_matrix);
  matrix.drawLine(34, 15, 48, 18, truck_color_2_matrix);
  matrix.drawLine(34, 9, 34, 15, truck_color_2_matrix);
  matrix.drawLine(48, 12, 48, 18, truck_color_2_matrix);

// Truck 3
  if (truck_color_3 == 'b') {
    truck_color_3_matrix = matrix.Color333(1,2,7);
  } else if (truck_color_3 == 'y') {
    truck_color_3_matrix = matrix.Color333(7,7,0);
  } else if (truck_color_3 == 'r') {
    truck_color_3_matrix = matrix.Color333(7,0,0);
  } else {
    truck_color_3_matrix = matrix.Color333(3,3,3);    
  }
  matrix.drawLine(39, 3, 49, 6, truck_color_3_matrix);
  matrix.drawLine(39, 7, 49, 10, truck_color_3_matrix);
  matrix.drawLine(39, 7, 39, 3, truck_color_3_matrix);
  matrix.drawLine(49, 6, 49, 10, truck_color_3_matrix);

// White Line Separating Text
  matrix.drawLine(50, 0, 50, 32, matrix.Color333(3,3,3));

  // draw some text!
  // draw some text!
  matrix.setTextSize(1);     // size 1 == 8 pixels high
  matrix.setTextWrap(false); // Don't wrap at end of line - will do ourselves


  matrix.fillRect(52, 0, 15, 32, matrix.Color333(0,0,0));

// Truck 1 Text
  matrix.setCursor(52, 23);    // bottom left
  matrix.setTextColor(truck_color_1_matrix);
  matrix.println(numbers[2]);

// Truck 2 Text
  matrix.setCursor(52, 12);    // center
  matrix.setTextColor(truck_color_2_matrix);
  matrix.println(numbers[1]);
  

  // Truck 3 Text
  matrix.setCursor(52, 1);    // start at top left, with 8 pixel of spacing
  matrix.setTextColor(truck_color_3_matrix);
  matrix.println(numbers[0]);
 

  while (!Serial.available()) {
     // If not available, a red dot
    // matrix.drawPixel(12, 12, matrix.Color333(7, 0, 0));
   }
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

  

  // BELOW IS WHAT WE ACTUALLY USE

  String python_output = Serial.readString();
  if (python_output == "new") {
    // A new frame is being captured, reset pixel and wait time values
    for (int i=0; i<num_people; i++) {
      matrix.drawPixel(pixels[2*i], pixels[2*i+1], matrix.Color333(0, 0, 0));
    }
    numbers[0] = 0;
    numbers[1] = 0;
    numbers[2] = 0;
    // Debugging pixel
    // matrix.drawPixel(0, num_people, matrix.Color333(0, 0, 7));
    
    num_people = 0;
    
  } else if (python_output.c_str()[0] == 't') {
    // Truck colors are communicated here
    // matrix.drawPixel(0,0,matrix.Color333(7,0,0));
    if (python_output.c_str()[1] == '1'){
      // matrix.drawPixel(0,1,matrix.Color333(7,0,0));
      truck_color_1 = python_output.c_str()[2];
    } else if (python_output.c_str()[1] == '2') {
      truck_color_2 = python_output.c_str()[2];
    } else if (python_output.c_str()[1] == '3') {
      truck_color_3 = python_output.c_str()[2];
    } 
    

  } else {
      // Read in the next tuple of a person location
      sscanf(python_output.c_str(), "%2d,%2d", &tuple[0], &tuple[1]);

      pixels[num_people * 2] = tuple[0];  
      pixels[num_people * 2+1] = tuple[1];
  
      
      // Update the waittimes
      if (tuple[0] > x_boundary) {
        if (tuple[1] < y1_boundary ) {
          numbers[0] += time_inc;
        } else if (tuple[1] < y2_boundary ) {
          numbers[1] += time_inc;
        } else if (tuple[1] > y2_boundary){
          numbers[2] += time_inc;
        }
      }

      num_people += 1;
      
      for (int i=0; i<num_people; i++) {
        matrix.drawPixel(pixels[2*i], pixels[2*i+1], matrix.Color333(0, 7, 0));
        delay(20);
      }

  }


  }

  
