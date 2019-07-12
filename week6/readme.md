TODO: Reflect on what you learned this week and what is still unclear.

attempted print(POSE_COCO_BODY_PARTS[4][0]) however this just prints the letter of index [0] within element [4]

CHANGED THE taxi text width for fun

using pandas
#WITH THE CODE BELOW, it works however only if nose and the two wrists are intiially in frame, it doesnt matter if they are in frame afterwards but initally if they arent there it crashes. 
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

Elijah - defined a function where it selects a row, and if its not empty it returns a fllat