# ReBenchCSVDataProcessor

ReBench CSV Data Processor is a Python tool for processing [ReBench](https://github.com/smarr/ReBench) CSV benchmarking data. Export results in LaTeX, HTML, or Markdown.

## Usage

To run the ReBench CSV Data Processor, use the following command in your terminal:

```bash
python3 rebenchProcessor.py <path_to_csv_file> [--format <output_format>]
```

### Parameters

- `<path_to_csv_file>`: The path to the CSV file containing the benchmarking data.
- `--format`, `-f`: (Optional) Specify the output format. Choices include:
  - `latex` or `l`: Export results in LaTeX format (default).
  - `html` or `h`: Export results in HTML format.
  - `markdown` or `m`: Export results in Markdown format.

### Examples

1. To process a CSV file and export the results in LaTeX format (default):
```bash
python3 rebenchProcessor.py ~/Documents/ReBenchFiles/rebench.csv
```

2. To process a CSV file and export the results in HTML format:

```bash
python3 rebenchProcessor.py ~/Documents/ReBenchFiles/rebench.csv --format html
```

3. To process a CSV file and export the results in Markdown format using the shorthand:

```bash
python3 rebenchProcessor.py ~/Documents/ReBenchFiles/rebench.csv -f m
```

## Requirements

- Python 3.x
- pandas library
- numpy library


```bash
# Install pandas
pip install pandas

#Install numpy
pip install numpy
```
