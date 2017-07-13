# Waiting Lists for Affordable Housing

The Somerville Housing Waiting lists omitting personal identifying information. [MuckRock page](https://www.muckrock.com/foi/somerville-8/waiting-lists-for-affordable-housing-in-somerville-ma-740/)

## Process

1. I Converted the PDF into images with ImageMagick because it is image-based and does not have any embedded text.

```sh
$ convert -units PixelsPerInch -density 300 9-05-12_mr740_RES.pdf[2-10] -threshold 70% convert_output/waiting_list.png
```

2. Then I used [Soma's Kull tool](https://jsoma.github.io/kull/#/) to select the values and [Soma's tesseract-uzn](https://github.com/jsoma/tesseract-uzn) to extract them without using a uzn file for each image. I created one uzn file per chosen column.

```sh
$ for i in convert_output/*.png ; do ./tesseract-uzn date_waiting_list.uzn $i > $i-date.txt;  done;
```
```sh
$ for i in convert_output/*.png ; do ./tesseract-uzn age_waiting_list.uzn $i > $i-age.txt;  done;
```
```sh
$ for i in convert_output/*.png ; do ./tesseract-uzn members_waiting_list.uzn $i > $i-members.txt;  done;
```
```sh
$ for i in convert_output/*.png ; do ./tesseract-uzn disabled_waiting_list.uzn $i > $i-disabled.txt;  done;
```

I tried to add a threshold, increase the DPI, change the orientation of the page, but was unable to get a good result.

3. I could have used `cat` to concatenate the TXT files into a new big file and then `paste` to create a TSV file from them but it's safer to go line by line to avoid mismatches. 

```sh
$ for i in tesseract_output/*-date.txt; do cat $i >> fileresults.txt; done;
```
```sh
$ paste file1.txt file2.txt file3.txt file4.txt > result.txt
```

4. I used python and glob to concatenate everything [The notebook with an histogram](https://github.com/mathieulede/foundations/blob/master/15-Homework%20PDF-to-text/Vanity%20license%20plates/Vanity%20license%20plates.ipynb)

[The cleaned data](https://github.com/mathieulede/foundations/blob/master/15-Homework%20PDF-to-text/Waiting%20list%20for%20affordable%20housing/waiting_list.csv)

## A few questions

We could get the average age and number of people in families that are on the waiting list or look for increases of the demands during certain periods of the year.