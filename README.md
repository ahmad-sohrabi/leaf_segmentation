# A Simple Leaf Segmentation
In This Project, We Are going to implement a very simple image processing based leaf segmentation.
<br />

## Algorithm Procedure
1- First of all, to simplify the input image and to have a cleaner image, a simple background removal algorithm based on HSV color
space is implemented.
<br />
2- Then OTSU thresholding algorithm is implemented to have binary image and segmenting detected parts into white and black
<br />
3- As in the last step, the generated mask is not clean enough, an Opening morphological
operation is implemented to keep only leaves.
<br />
4- At last with a bitwise AND operation is implemented to show the segmented leaves result.
The library which is used for the mentioned algorithm is Python OpenCV.
## Result

![Leaf One](https://github.com/ahmad-sohrabi/leaf_segmentation/blob/main/result/Leaf%20Process%201.png?raw=true)
<br />
![Leaf Two](https://github.com/ahmad-sohrabi/leaf_segmentation/blob/main/result/Leaf%20Process%202.png?raw=true)
<br />
![Leaf Three](https://github.com/ahmad-sohrabi/leaf_segmentation/blob/main/result/Leaf%20Process%203.png?raw=true)
<br />
![Leaf Four](https://github.com/ahmad-sohrabi/leaf_segmentation/blob/main/result/Leaf%20Process%204.png?raw=true)
<br />
![Leaf Five](https://github.com/ahmad-sohrabi/leaf_segmentation/blob/main/result/Leaf%20Process%205.png?raw=true)
<br />
![Leaf Six](https://github.com/ahmad-sohrabi/leaf_segmentation/blob/main/result/Leaf%20Process%206.png?raw=true)
<br />
![Leaf Seven](https://github.com/ahmad-sohrabi/leaf_segmentation/blob/main/result/Leaf%20Process%207.png?raw=true)
<br />



