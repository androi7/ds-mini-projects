# Web Scraping of Indeed Jobs
---
In this project the website from *indeed* is scraped to obtain job offers of data-related jobs from larger cities in the USA to predict high and low salaries.

## Motivation
The goal is to apply several classification models on a binary problem and to evaluate them such as to adapt the prediction approach based on the relevance of different outcome requirements like prediction and accuracy.

## Tools
- Programming Language: Python
- Web Scraping: BeautifulSoup

## Footnote
The website *indeed* uses captchas and therefore the web scraping process is divided into several smaller steps to avoid to get blocked. The assossiated function provides a parameter to add a list of proxy ip addresses which can be applied in a rotating cycle. However, the scraped proxy ip addresses in this project come from a free proxy server list which can be detected from the website and thus, do not lead to the desired result.

