import cv2
from typing import List

def merge_close_bounding_box(bbox_list: List, image: str, merge_threshold: int = 15):
    """
    Merge Close Bounding box on X-coordinate. 

    Parameters:
        bbox_list : [
                        [left, top, width, height],
                        [left, top, width, height],
                        [left, top, width, height]
                    ]
        image: image_path


    Return:
        merged_bbox_list = [
                                [left, top, width, height],
                                [left, top, width, height],
                            ]

    """
    image = cv2.imread(image)
    rects = []
    rectsUsed = []
    for cnt in bbox_list:
        rects.append(cnt)
        rectsUsed.append(False)


    # Sort bounding rects by x coordinate
    def getXFromRect(item):
        return item[0]

    rects.sort(key = getXFromRect)

    # Array of accepted: rects
    acceptedRects = []

    # Merge threshold for x coordinate distance
    xThr = merge_threshold

    # Iterate all initial bounding rects
    for supIdx, supVal in enumerate(rects):
        if (rectsUsed[supIdx] == False):

            # Initialize current rect
            currxMin = supVal[0]
            currxMax = supVal[0] + supVal[2]
            curryMin = supVal[1]
            curryMax = supVal[1] + supVal[3]

            # This bounding rect is used
            rectsUsed[supIdx] = True

            # Iterate all initial bounding rects
            # starting from the next
            for subIdx, subVal in enumerate(rects[(supIdx+1):], start = (supIdx+1)):
                # Initialize merge candidate
                candxMin = subVal[0]
                candxMax = subVal[0] + subVal[2]
                candyMin = subVal[1]
                candyMax = subVal[1] + subVal[3]

                # Check if x distance between current rect
                # and merge candidate is small enough
                if (candxMin <= currxMax + xThr):
                    # Reset coordinates of current rect
                    currxMax = candxMax
                    curryMin = min(curryMin, candyMin)
                    curryMax = max(curryMax, candyMax)

                    # Merge candidate (bounding rect) is used
                    rectsUsed[subIdx] = True
                else:
                    break
            # No more merge candidates possible, accept current rect
            acceptedRects.append([currxMin, curryMin, currxMax - currxMin, curryMax - curryMin])

    return acceptedRects

















