import cv2 
from merge_bbox import merge_close_bounding_box

# Test Co-ordinates
coords = [
          [36, 92, 60, 24], [109, 92, 20, 24], [141, 98, 15, 18], 
          [169, 92, 32, 24], [212, 92, 28, 24], [296, 92, 68, 30], 
          [374, 93, 53, 23], [437, 93, 26, 23], [474, 93, 52, 23]
          ]

image_name  = 'test/sample.png'
img = cv2.imread(image_name)
d_rects = []    
for coord in coords:
    each_rect = [None, None, None, None]
    (x, y, w, h) = coord[0], coord[1], coord[2], coord[3]
    each_rect[0], each_rect[1], each_rect[2], each_rect[3] = x, y, w, h
    d_rects.append(each_rect)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

saved_image_path_before_merge = image_name.split(".")[0] + str("_before_merge") + ".png"
cv2.imwrite(saved_image_path_before_merge, img)

merged_bbox = merge_close_bounding_box(bbox_list= coords, image= image_name, merge_threshold= 15)

img = cv2.imread(image_name)
for i in range(len(merged_bbox)):
    (x, y, w, h) = merged_bbox[i][0], merged_bbox[i][1], merged_bbox[i][2], merged_bbox[i][3]
    cv2.rectangle(img, (x, y), (x +w, y +h), (0, 255, 0), 2)

saved_image_path_after_merge = image_name.split(".")[0] + str("_after_merge") + ".png"
cv2.imwrite(saved_image_path_after_merge, img)

