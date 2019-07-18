TODO: Reflect on what you learned this week and what is still unclear.

This week task seemed daunting at first, integrating just 5 weeks of coding experience with "neural networks" to use a webcam to read a body. 
I jumped straight to believing the task involved seeing if a y-coordinate for the arms could be compared the the coordinate for neck or nose. My partner chose a slightly different route relating to creating a triangle with the shoulder, elbow and wrist. 

The intial stage of codng involved exploring the existing line to create:

print(POSE_COCO_BODY_PARTS[4][0]) 
    What I wanted was to see if I could obtain the value of the body part number 4, similar to the dictionary reading exercise from prior weeks. However this just prints the letter of index [0] within element [4], as I should have expected rip. 
    
BUT this did help in seeing that I could target specific body parts! B U T I found it odd that the body part assigned to [4] kept changing. What this made my partner and I think was we would need to go in and read the dataset and use a search method to find the relevant body part. This is where PANDAS came in, as a way to more clearly read the dataset as a dataframe through which we could read.

Using pandas we were able to effectively isolate the y-coordinates for different body parts and then compare them. 

After being able to stablise the dataframe I was able to explore how the x and y values for each body part changed as I moved. Prior to this, as i mentioned earlier, the body part associated to an index --> POSE_COCO_BODY_PARTS[X] kept changing so I couldn't really udnerstand what the values were until this point.

In terms of the y-axis, 0 meant the top of the screeen and the bottom would be 1. Similarly, the left was 0 while right was 1.

At this stage the code worked but only if the relevant body parts (neck and wrists) were in frame as the program loaded, if not the program would crash. This led to use incorporating a try except clause and FINALLY THE PROGRAM IS DONE.

The final change in this assignment was that I adjusted the font and size of "TAXI" for the lols. 


A snippet of an older iteration of the code:

WITH THE CODE BELOW, it works however only if nose and the two wrists are intiially in frame, it doesnt matter if they are in frame afterwards but initally if they arent there it crashes. 
output = pd.DataFrame([(POSE_COCO_BODY_PARTS[k], v.y) for k,v in human.body_parts.items()])
            output.columns = ["Body Part", "y-coord"]
            
            try:
                Nosedf = output[output['Body Part'] == 'Nose']
                noseheight = float(Nosedf.iloc[:,1])
                print(noseheight)
            except:
                pass
            try:
                RWristdf = output[output['Body Part'] == 'RWrist']
                RWristHeight = float(RWristdf.iloc[:,1])
                print(RWristHeight)
            except:
                pass

            try:
                LWristdf = output[output['Body Part'] == 'LWrist']
                LWristHeight = float(LWristdf.iloc[:,1])
                print(RWristHeight)
            except:
                pass

            if RWristHeight < noseheight or LWristHeight < noseheight:
                     hail_taxi(image)


This happens because you cant float a none type

Elijah - defined a function where it selects a row, and if its not empty it returns a flat