# Vanity license plates

A list of all personalized license plate number applications that were rejected for the year 2013 in New Hampshire. [MuckRock page](https://www.muckrock.com/foi/new-hampshire-81/rejected-personalized-aka-vanity-license-plates-in-2013-department-of-motor-vehicles-11650/)

## Process

1. I Converted the PDF into images with ImageMagick because it is image-based and does not have any embedded text.

```sh
$ convert -units PixelsPerInch -density 150 2013_rejected_vanity_plate_applications_Redacted.pdf vanity_plate.png
```

2. Then I used Tesseract to get a text output. I didn't use UZN because the scans where not well positionned from one page to another.

```sh
$ for i in *.png ; do tesseract $i $i;  done;
```

3. In python, I used glob to concatenate all the files and, as there is no tables or fixed format, regex to extract the number, date and reasons for rejection.
[The notebook with a graph](https://github.com/mathieulede/foundations/blob/master/15-Homework%20PDF-to-text/Vanity%20license%20plates/Vanity%20license%20plates.ipynb)

[The cleaned data](https://github.com/mathieulede/foundations/blob/master/15-Homework%20PDF-to-text/Vanity%20license%20plates/vanity_license_plates.csv)

## A few questions

We could get the most wanted vanity plate number. Show the time of the year when the demand is the highest. Group the type of vanity plates with regex to find the sexual oriented ones, violent ones, etc. `(F.*K.*)` `(P.*SY)` `(K.*L.*)` `(M[OU]M)`