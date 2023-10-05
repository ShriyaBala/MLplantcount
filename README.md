# Plant-counter-CV
Computer vision for counting plants in an image. This program should be deployed for the mobile application, meaning it will run in the cloud. Users will upload photos through our app, and the application will send them to the cloud for processing. Afterward, the processing will take place in the cloud, and the results will be sent back in the form of a JSON object, presented appropriately to the user. This constitutes the fundamental concept of the application.

## Getting Started

This is the repo to count the number of Plants or Germinations in a given image, by using HSV transformation. and count the number of plants or germinations using the contours count and thresholding concepts


### Packages required

* [Opencv](https://opencv.org/)
* [Numpy](https://numpy.org/)
## usage

```
python Trial1\main6.py
```
## Note:
The input image is stored in the 'Images' folder and the output is stored in the 'hsv_results' folder. The output contains the masked image, the result image and the details of the count in the json format.

## sample input
![](Images\6.jpg)

## sample output

![](hsv_results/6/details.json)
![](hsv_results/6/masked_image.jpg)
![](hsv_results/6/result.jpg)

