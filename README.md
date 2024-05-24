# *Sign Language Recognition*

## Introduction
Sign language is a vital means of communication for millions of people worldwide who are deaf or hard of hearing. However, communication barriers often arise when sign language users interact with individuals who do not understand sign language. Sign language detection systems aim to address this challenge by leveraging technology to interpret and translate sign language gestures into spoken or written language, thereby facilitating communication between sign language users and non-signers.


## Dataset
The [Sign Language Gesture Images Dataset](https://www.kaggle.com/ahmedkhanak1995/sign-language-gesture-images-dataset) has been used for training our model.For this model , I have deleted from the original dataset, the numbers from 0-9 and deleted letters 'J' and 'Z' as they utilise motion detection which is not implemented in this system.  

## Accuracy
This model that has been trained has had the accuracy of approximately 99.95% and the loss is approximately 0.00208.

## System limitations
1. With any detection system, there is always going to be errors, I cannot guarentee that this system is 100% accuracte. 
2. This system will not be able to detect hand guestures if there is no natural light or good lighting.
3. The timing of the output of the letters may vary from device to device
4. The letters J and Z , were removed as these letters utilise motion detection which is not implemented.

## How to run the files
1. Locate the RealTimeRecognition.py file 
2. Right click the file and locate "Run Code"
3. Press "Run Code"
4. This file will start running on the terminal and will take a few seconds to start after reading the labels.
