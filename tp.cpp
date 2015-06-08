#include <iostream>
#include "serial.h"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <math.h>
#include <unistd.h>
using namespace cv;
using namespace std;

float dist(Point center1, Point center2){
	float dist;
	dist= sqrt((center1.x-center2.x)*(center1.x-center2.x)+(center1.y-center2.y)*(center1.y-center2.y));
	return dist;
	}

 int main( int argc, char** argv )
 {
	char c;
	serial_device arduino; 
	arduino.initialize("/dev/ttyUSB0");
    VideoCapture cap(0); //capture the video from webcam

    if ( !cap.isOpened() )  // if not success, exit program
    {
         cout << "Cannot open the web cam" << endl;
         return -1;
    }
	
    namedWindow("Control", CV_WINDOW_AUTOSIZE); //create a window called "Control"

int iLowH = 86;
int iHighH = 104;

int iLowS = 0; 
int iHighS = 255;

int iLowV = 0;
int iHighV = 255;

//Create trackbars in "Control" window
createTrackbar("LowH", "Control", &iLowH, 179); //Hue (0 - 179)
createTrackbar("HighH", "Control", &iHighH, 179);

createTrackbar("LowS", "Control", &iLowS, 255); //Saturation (0 - 255)
createTrackbar("HighS", "Control", &iHighS, 255);

createTrackbar("LowV", "Control", &iLowV, 255);//Value (0 - 255)
createTrackbar("HighV", "Control", &iHighV, 255);

int iLastX = -1; 
int iLastY = -1;

int width= cap.get(CV_CAP_PROP_FRAME_WIDTH);
int height=cap.get(CV_CAP_PROP_FRAME_HEIGHT);
cout<<width<<endl;
cout<<height<<endl;

float c1x=width/2, c1y=0;
float c2x=0, c2y=height/2;
float c3x=width/2, c3y=height;
float c4x=width, c4y=height/2;


//Capture a temporary image from the camera
Mat imgTmp;
cap.read(imgTmp); 

//Create a black image with the size as the camera output
Mat imgLines = Mat::zeros( imgTmp.size(), CV_8UC3 );;


    while (true)
    {
        Mat imgOriginal;

        bool bSuccess = cap.read(imgOriginal); // read a new frame from video



         if (!bSuccess) //if not success, break loop
        {
             cout << "Cannot read a frame from video stream" << endl;
             break;
        }

Mat imgHSV;

cvtColor(imgOriginal, imgHSV, COLOR_BGR2HSV); //Convert the captured frame from BGR to HSV

Mat imgThresholded;

inRange(imgHSV, Scalar(iLowH, iLowS, iLowV), Scalar(iHighH, iHighS, iHighV), imgThresholded); //Threshold the image
      
//morphological opening (removes small objects from the foreground)
erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(10, 10)) );
dilate( imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(10, 10)) ); 

//morphological closing (removes small holes from the foreground)
dilate( imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(10, 10)) ); 
erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(10, 10)) );

//Calculate the moments of the thresholded image
Moments oMoments = moments(imgThresholded);

double dM01 = oMoments.m01;
double dM10 = oMoments.m10;
double dArea = oMoments.m00;

// if the area <= 10000, I consider that the there are no object in the image and it's because of the noise, the area is not zero 
if (dArea > 10000)
{
//calculate the position of the ball
int posX = dM10 / dArea;
int posY = dM01 / dArea;        
        
if (iLastX >= 0 && iLastY >= 0 && posX >= 0 && posY >= 0)
{
//Draw a red line from the previous point to the current point

circle(imgOriginal,Point(iLastX, iLastY),10	, Scalar(0,0,255),-1);
}

iLastX = posX;
iLastY = posY;
}
else{
	iLastX = -1; 
    iLastY = -1;
}

imshow("Thresholded Image", imgThresholded); //show the thresholded image

imgOriginal = imgOriginal + imgLines;
imshow("Original", imgOriginal); //show the original image
if(dist(Point(iLastX, iLastY),Point(c1x,c1y))<=160)
{
	cout<<"Region 1"<<endl;
	c='a';
	arduino.write_byte(c);
	
}
else if(dist(Point(iLastX, iLastY),Point(c2x,c2y))<=160)
{
	cout<<"Region 2"<<endl;
	c='b';
	arduino.write_byte(c);
}
 else if(dist(Point(iLastX, iLastY),Point(c3x,c3y))<=160)
{
	cout<<"Region 3"<<endl;
	c='c';
	arduino.write_byte(c);
}
 else if(dist(Point(iLastX, iLastY),Point(c4x,c4y))<=160)
{
	cout<<"Region 4"<<endl;
	c='d';
	arduino.write_byte(c);
}
else
{
	cout<<"Do nothing"<<endl;
	c='o';
	arduino.write_byte(c);
}
   
    
        if (waitKey(30) == 27) //wait for 'esc' key press for 30ms. If 'esc' key is pressed, break loop
       {
            cout << "esc key is pressed by user" << endl;
            break; 
       }
    }
   
   return 0;
   
}
