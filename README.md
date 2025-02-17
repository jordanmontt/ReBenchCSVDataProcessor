# ReBenchCSVDataProcessor

`ReBenchCSVDataProcessor` is a Python class for processing benchmarking data from CSV files. It cleans, aggregates, and exports [ReBench](https://github.com/smarr/ReBench) CSV results in LaTeX, Markdown, or HTML formats.

## TLDR

Adjust the CSV file path and export format in `playground.py` to use `ReBenchCSVDataProcessor` for your benchmarking data and then run `python3 playground.py` in the terminal.

## Usage

In `playground.py`, modify the following:

```python
rebench_csv_path = '~/Documents/ReBenchFiles/reBenchResult.csv'  # <-----  Update this path to your csv rebench file
output = rebench_processor.to_latex()  # <------ Change to to_markdown() or to_html() as needed
```

Then, execute the following command in the terminal:

```bash
python3 playground.py
``` 

## Requirements

- Python 3.x
- pandas library

Install pandas with:

```bash
pip install pandas
```
