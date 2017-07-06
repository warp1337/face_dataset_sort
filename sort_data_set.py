import cv2
import sys
import glob

# cascade File
c_path = sys.argv[1]
# folder to be globbed
data_dir = sys.argv[2]
# positive examples
pos_dir = sys.argv[3]
# negative examples
neg_dir = sys.argv[4]
# obviously the cascade file
faceCascade = cv2.CascadeClassifier(c_path)

# counter
c_pos = 0
c_neg = 0
c_all = 0
for im in glob.glob(data_dir + '/*.jpg'):
    c_all += 1
    # print("Found: %s" % im)
    image = cv2.imread(im)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    if len(faces) > 0:
        print("Found {0} faces!".format(len(faces)))
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Faces found", gray)
        cv2.waitKey(0)
        cv2.imwrite(pos_dir + "/" + im, gray)
        c_pos += 1
    else:
        print("Writing negative example %s" % im)
        cv2.imwrite(neg_dir + "/" + im, gray)
        c_neg += 1

print("Processed %d images | positive %d | negative %d" % (c_all, c_pos, c_neg))
