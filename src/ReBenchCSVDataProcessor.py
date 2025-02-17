import pandas as pd


class ReBenchCSVDataProcessor:
    def __init__(self):
        self.csv_file = None
        self.df = None
        self.aggregated_df = None

    def set_up_rebench_csv_file(self, file_reference):
        self.csv_file = file_reference
        self.create_data_frame()

    def create_data_frame(self):
        try:
            self.df = pd.read_csv(self.csv_file, sep='\t', on_bad_lines='skip', comment='#')
            self.group_df_by_benchmarks_and_executions()
        except pd.errors.ParserError as e:
            print(f"Error parsing the CSV file: {e}")
            return

        # Remove useless columns
        columns_to_remove = ['inputSize', 'cores', 'machine', 'varValue', 'extraArgs']
        self.df.drop(columns=columns_to_remove, inplace=True)

        # Keep only the total column as it is the one that has the real time to execute value
        self.df = self.df[self.df['criterion'] == 'total']

    def group_df_by_benchmarks_and_executions(self):
        self.aggregated_df = self.df.groupby(['benchmark', 'executor'])['value'].agg(['mean'])
        return self.aggregated_df

    def to_latex(self):
        latex_output = self.aggregated_df.to_latex(
            float_format="%.2f",
            multirow=True,  # Use multirow for hierarchical indexing
            escape=True)  # Set to False if you want to include special characters
        return latex_output

    def to_markdown(self):
         # Export to Markdown
        markdown_table = self.aggregated_df.to_markdown(
            floatfmt=".2f",
            tablefmt="github")
        return markdown_table

    def to_html(self):
        html_table = self.aggregated_df.to_html(
            float_format="%.2f",
            border=0,
            classes='table table-striped',
            index=True)
        return html_table

    @classmethod
    def on_csv_file(cls, file_reference):
        instance = cls()
        instance.set_up_rebench_csv_file(file_reference)
        return instance
