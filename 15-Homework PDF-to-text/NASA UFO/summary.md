# NASA UFO, Alien FOIA Requests

## Summary

The text of all Freedom of Information Act Requests received by the National Aeronautics and Space Administration (NASA) during the year 2014 requesting for information or documents about, concerning, or mentioning, "unidentified flying objects," "U.F.O.s," "Extraterrestrial life forms," "Aliens," "Alien Abductions," or "Crop circles." [MuckRock page](https://www.muckrock.com/foi/united-states-of-america-10/nasa-ufo-alien-foia-requests-19668/)

## Process

1. I Converted the PDF into images with ImageMagick because it is image-based and does not have any embedded text.

```sh
$ convert -density 300 Jones_Graffiti.pdf graffiti.png
```

2. Then I used Tesseract to get a text output

```sh
$ convert -density 300 Jones_Graffiti.pdf graffiti.png
```