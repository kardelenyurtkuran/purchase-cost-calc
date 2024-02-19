import pandas as pd

class FileOperation:
    def OpenXlsxFile(self, file_name):
        df = pd.read_excel(file_name, engine='openpyxl')
        print(df)