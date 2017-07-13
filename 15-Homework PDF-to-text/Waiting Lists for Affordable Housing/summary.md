# Waiting Lists for Affordable Housing

The Somerville Housing Waiting lists omitting personal identifying information. [MuckRock page](https://www.muckrock.com/foi/somerville-8/waiting-lists-for-affordable-housing-in-somerville-ma-740/)

## Process

1. I Converted the PDF into images with ImageMagick because it is image-based and does not have any embedded text.

```sh
$ convert -units PixelsPerInch -density 300 9-05-12_mr740_RES.pdf[2-10] -threshold 70% convert_output/waiting_list.png
```

2. Then I used [Soma's Kull tool](https://jsoma.github.io/kull/#/) to select the values and [Soma's tesseract-uzn](https://github.com/jsoma/tesseract-uzn) to extract them without using a uzn file for each image. I created one uzn file per choosen column.

```sh
$ for i in convert_output/*.png ; do ./tesseract-uzn date_waiting_list.uzn $i > $i-date.txt;  done;

$ for i in convert_output/*.png ; do ./tesseract-uzn age_waiting_list.uzn $i > $i-age.txt;  done;

$ for i in convert_output/*.png ; do ./tesseract-uzn members_waiting_list.uzn $i > $i-members.txt;  done;

$ for i in convert_output/*.png ; do ./tesseract-uzn disabled_waiting_list.uzn $i > $i-disabled.txt;  done;
```

I tried to add a threshold, increase the DPI, change the orientation of the page, but was unable to get a good result.

3. I used paste to concatenate the four TXT files into a TSV file. 

```sh
$ for i in tesseract_output/*-date.txt cat $i file2.txt > fileresults.txt

$ cat file1.txt file2.txt > fileresults.txt

$ paste file1.txt file2.txt > fileresults.txt
```

## A few questions

We could get the average age and number of people in families that are on the waiting list or look for increases of the demands during certain periods of the year.