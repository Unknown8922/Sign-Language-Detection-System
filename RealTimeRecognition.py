import cv2
import numpy as np
import tensorflow as tf
import os
import pyttsx3

# Load saved model from PC
model = tf.keras.models.load_model(r'Sign-Language-Recognition-main/new_model_20ep3.h5')
model.summary()

# Define the directory containing your training data
training_data_dir = r'C:\Users\Zoe Mirielle Varma\OneDrive\Desktop\Sign-Language-Recognition\Sign-Language-Recognition-main\datasett\Gesture Image Pre-Processed Data'

# Get the list of labels from the training data directory
training_labels = sorted(os.listdir(training_data_dir))

# Update the labels in your inference code to match the training labels
labels = training_labels

print("Training Labels:", training_labels)
print("Inference Labels:", labels)

# Initiating the video source, 0 for internal camera
cap = cv2.VideoCapture(0)
while(True):
    _, frame = cap.read()
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), 5) 
    roi = frame[100:300, 100:300]
    img = cv2.resize(roi, (50, 50))
    cv2.imshow('roi', roi)

    img = img/255

    # Make prediction about the current frame
    prediction = model.predict(img.reshape(1,50,50,3))
    char_index = np.argmax(prediction)
    
    # Print char_index during runtime
    print("Char Index:", char_index)

    confidence = round(prediction[0, char_index] * 100, 1)

    # Check if char_index is within the range of labels list
    if char_index < len(labels):
        predicted_char = labels[char_index]
    else:
        predicted_char = "Unknown"
    
    # Print the predicted character
    print("Predicted Char:", predicted_char)
    
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(predicted_char) 
    engine.runAndWait()

    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 1
    color = (0, 255, 255)
    thickness = 2

    # Writing the predicted char and its confidence percentage to the frame
    msg = predicted_char + ', Conf: ' + str(confidence) + ' %'
    cv2.putText(frame, msg, (80, 80), font, fontScale, color, thickness)
    
    cv2.imshow('frame', frame)
    
    # Close the camera when press 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
