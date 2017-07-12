# Terrorism prosecutions

A list of terrorism prosecutions since January 1st, 2012 which includes the defendant's name, district, charging date, charges brought, classification category, conviction date, and charges of conviction. [MuckRock page](https://www.muckrock.com/foi/united-states-of-america-10/terrorism-prosecutions-since-january-1st-2012-16873/)

 I wanted to use grep but there are sometimes several lines to extract.

grep '\d, \d\d\d\d' tesseract_output/*.txt > dates.txt
grep 'vanity plate' tesseract_output/*.txt > plates.txt
grep -A1 'reasons:' tesseract_output/*.txt > reasons.txt