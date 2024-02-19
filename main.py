from FileOperations import FileOperation

class PurchaseCostCalc:
    def __init__(self):
        self.file_op = FileOperation()
        self.OpenXlsxFile()

    def OpenXlsxFile(self):
        file_name = "./Sample_BOM_lists/Sample_BOM_list_1.xlsx" # You have to let the user choose
        self.file_op.OpenXlsxFile(file_name)

if __name__ == "__main__":
    PurchaseCostCalc()