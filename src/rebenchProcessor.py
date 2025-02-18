import os
import argparse
from ReBenchCSVDataProcessor import ReBenchCSVDataProcessor

# Set up argument parsing
parser = argparse.ArgumentParser(description='Process a ReBench CSV file.')
parser.add_argument('csv_file_path', type=str, help='Path to the ReBench CSV file')
parser.add_argument('--format', '-f', type=str, choices=['latex', 'html', 'markdown', 'l', 'h', 'm'], default='latex',
                    help='Output format (default: latex). Use "l" or "latex", "h" or "html", "m" or "markdown".')

# Parse the arguments
args = parser.parse_args()

# Expand user directory if necessary
csv_file_path = os.path.expanduser(args.csv_file_path)

# Process the CSV file
rebench_processor = ReBenchCSVDataProcessor.on_csv_file(csv_file_path)

# Export the output based on the specified format
if args.format == 'latex' or args.format == 'l':
    output = rebench_processor.to_latex()
elif args.format == 'markdown' or args.format == 'm':
    output = rebench_processor.to_markdown()
elif args.format == 'html' or args.format == 'h':
    output = rebench_processor.to_html()

# Print the output
print(output)