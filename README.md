# Project-RASC
 Raf's Artificial Swing Coach. Using pose detection and computer vision, finding the optimal way to adjust golf swings using historical data of professionals.

## Synopsis
 Golf has been picking up in popularity again in North America, and I've enjoyed playing the game in the past year.
 Learning from friends, YouTube videos, and social media has been insightful, but I found it very hard to track whether "I am shaping the shot" the correct way. Currently not invested enough to hire a coach, and looking to play more leisurely.

 Hence I've decided to use my expertise in Machine Learning and data collection to create Project RASC (Raf's Artificial Swing Coach).

 Although the main focus of the application is for golf, the fundamentals can be applied to various other activities.

## Steps:
 As of the first commit (Jul 11, 2024), Project RASC has only gone throught the first of many steps. Here is a quick rundown of the next few steps:

 1. Research
    This part of the process focuses on the main machine learning model aspect of the project.
    As of the first commit, pose_detect.py highlights the achievements made to reasonably trust the mediapipe model to highlight landmarks and features of the human body throughout a swing.
 2. Refine structure of application
    Next is create a data pipeline where videos can be fed through the application, and output to a table or library of landmarks with each video. This will later be used to train a seperate model on how a player may improve their swing.
    In addition, a simple graphical and interactive UI will be put in place for deeper analysis.
 3. Dedicated .py app and resources
    As of the first commit, the application lives under Jupyer Notebooks. The plan forward is to output into a proper Python structure for reusability and use of public use.
 4. Collect videos and feed data table
    Cycling back to research, but in a different way. Hand picked videos of players and their iconic swings will be tun through the program and outputed on a table. Example: Tiger Woods clips so that the application can show how your shot is different from Tiger Woods.
 5. UI
    Finally create a UI for public use. How this would be done is currently undefined. It may be thrown into GO with it's own .exe, or on the web for ease of use with proper network hosting.
 6. Clean up and push