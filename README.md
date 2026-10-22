# Zillow Web Miner

Python scripts that collect for-sale home listings from Zillow across New York City's five boroughs and turn them into one clean CSV for analysis.

## How it works

1. **`scrapZillow.py`** sends the same search requests Zillow's website makes, one borough at a time (Manhattan, Brooklyn, Queens, Staten Island and the Bronx), and follows pagination until no pages are left. Each page of results is saved as a JSON file such as `mtnZillowSearch1.json`. It waits one second between requests.
2. **`JSONtoCSV.py`** reads every `.json` file in the current folder, pulls out each listing's details, keeps only listings with complete data, and writes them to `new_york_properties.csv`.

## Output columns

| Column | Example |
| --- | --- |
| Property Price | 850000 |
| Street Address | 123 Main St APT 4B |
| City / State / Zipcode | Brooklyn, NY, 11201 |
| Bedrooms / Bathrooms | 2 / 1 |
| Home Type | CONDO |
| Home Status | FOR_SALE |
| Living Area | 950 (sq ft) |

## Run it

```bash
pip install requests pandas
cd web-miner
python scrapZillow.py     # downloads the search pages as JSON
python JSONtoCSV.py       # combines them into new_york_properties.csv
```

The request headers in `scrapZillow.py` were copied from a browser session. Zillow's bot protection rejects stale headers, so if requests start failing (status 403), copy fresh request headers from your browser's developer tools (Network tab, the `async-create-search-page-state` request) into `rawHeader`.

## Notes

- Zillow's internal search API is undocumented and can change at any time.
- Check Zillow's terms of use before scraping, keep request rates low, and use the data for personal or academic analysis only.
