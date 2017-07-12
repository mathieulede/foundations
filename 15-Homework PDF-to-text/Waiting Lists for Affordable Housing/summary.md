# Waiting Lists for Affordable Housing

The Somerville Housing Waiting lists omitting personal identifying information. [MuckRock page](https://www.muckrock.com/foi/somerville-8/waiting-lists-for-affordable-housing-in-somerville-ma-740/)

## Process

1. I Converted the PDF into images with ImageMagick because it is image-based and does not have any embedded text.

```sh
$ convert -units PixelsPerInch -density 150 2013_rejected_vanity_plate_applications_Redacted.pdf vanity_plate.png
```

2. Then I used [Soma's Kull tool](https://jsoma.github.io/kull/#/) to select the values and [Soma's tesseract-uzn](https://github.com/jsoma/tesseract-uzn) to extract them without using a uzn file for each image.

```sh
$ for i in *.png ; do tesseract $i $i;  done;
```

I tried to add a threshold, increase the DPI, change the orientation of the page, but was unable to get a good result. 

## A few questions

We could get the average age and number of people in families that are on the waiting list, look for increase of the demands during certain periods of the year