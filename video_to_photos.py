import cv2
vidcap = cv2.VideoCapture('dataset/29er Sailing medemblik #2.mp4')
success,image = vidcap.read()
# count = 0
# success = True
# print("starting video split")
# while success:
#   print(f"handling image {count}")
#   success,image = vidcap.read()
#   cv2.imwrite("dataset/img_29er Sailing medemblik #2/frame%d.jpg" % count, image)     # save frame as JPEG file
#   if cv2.waitKey(10) == 27:                     # exit if Escape is hit
#       break
#   count += 1


import cv2
vidcap = cv2.VideoCapture('dataset/Laser Dinghy Go Pro Capsize.mp4')
success,image = vidcap.read()
count = 0
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 333))
  cv2.imwrite("dataset/img_laser dinghy go pro capsize/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1