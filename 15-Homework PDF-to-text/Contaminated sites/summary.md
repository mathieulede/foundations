# Contaminated sites in the Upper Peninsula

A complete list of contaminated sites in the Upper Peninsula. [MuckRock page](https://www.muckrock.com/foi/michigan-117/contaminated-sites-in-the-upper-peninsula-24638/)

## Process

1. I used Tabula to extract the PDF into a CSV file.

2. The CSV is clean but I had to replace all the carriage returns \r by an espace in jupyter

```python
df.replace(to_replace='\r', value=' ', regex=True, inplace=True)
```

## A few questions

We could get the most poluted place in the Upper Peninsula, The cities near these places.