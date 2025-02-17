import os
from ReBenchCSVDataProcessor import ReBenchCSVDataProcessor


"""Change this with the path of yout csv file"""
rebench_csv_path = '~/Documents/ReBenchFiles/reBenchResult.csv'


csv_file_path = os.path.expanduser(rebench_csv_path)
rebench_processor = ReBenchCSVDataProcessor.on_csv_file(csv_file_path)


""" Export the output. Change it if you want to export it to something else that is not LaTex """
output = rebench_processor.to_latex()
# output = rebench_processor.to_markdown()
# output = rebench_processor.to_html()


print(output)
