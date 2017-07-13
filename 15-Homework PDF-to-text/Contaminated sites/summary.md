# Contaminated sites in the Upper Peninsula

A complete list of contaminated sites in the Upper Peninsula pulled together by the Office of Waste Management and Radiological Protection Division. [MuckRock page](https://www.muckrock.com/foi/michigan-117/contaminated-sites-in-the-upper-peninsula-24638/)

## Process

1. I used Tabula to extract the PDF into a CSV file.

2. The CSV is clean but I had to replace all the carriage returns `\r` by an espace in jupyter. [The notebook, with a map](https://github.com/mathieulede/foundations/blob/master/15-Homework%20PDF-to-text/Contaminated%20sites/Contamined%20sites.ipynb)

```python
df.replace(to_replace='\r', value=' ', regex=True, inplace=True)
```

[The cleaned data](https://github.com/mathieulede/foundations/blob/master/15-Homework%20PDF-to-text/Contaminated%20sites/contamined_sites.csv)

## A few questions

We could get the most poluted places in the Upper Peninsula, look for clusters, find the companies that pollute the most, the cities near poluted places, the lakes or rivers near these places and the cities downstream.