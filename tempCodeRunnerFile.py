          x,y,w,h = face

            #Get the face ROI
            offset = 10
            face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
            face_section = cv2.resize(face_section,(100,100))

            #Predicted Label (out)
            out = knn(trainset,face_section.flatten())

            #Display on the screen the name and rectangle around it
            pred_name = names[int(out)]
            cv2.putText(frame,pred_name,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            print(pred_name)