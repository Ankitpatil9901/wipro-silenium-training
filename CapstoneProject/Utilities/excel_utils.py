import openpyxl
import pandas as pd
import os


class ExcelUtils:

    @staticmethod
    def get_excel_path(filename="login_data.xlsx"):
        base_path = os.getcwd()
        return os.path.join(base_path, "test_data", filename)

    @staticmethod
    def read_login_data(path, row=0):

        #Reads login data from Excel file
        try:
            df = pd.read_excel(path, sheet_name="LoginData")
            username = df.loc[row, "username"]
            password = df.loc[row, "password"]
            return username, password

        except Exception as e:
            print(f"Error reading LoginData sheet: {e}")
            raise

    @staticmethod
    def read_shipping_data(path, row=0):
        #Reads shipping data from Excel file
        try:
            df = pd.read_excel(path, sheet_name="ShippingData")

            firstname = df.loc[row, "firstname"]
            lastname = df.loc[row, "lastname"]
            address = df.loc[row, "address"]
            state = df.loc[row, "state"]
            postalcode = str(df.loc[row, "postalcode"])

            return firstname, lastname, address, state, postalcode

        except Exception as e:
            print(f"Error reading ShippingData sheet: {e}")
            raise

    @staticmethod
    def read_product_data(path):
        workbook = openpyxl.load_workbook(path)
        sheet = workbook["SearchProduct"]

        product = sheet.cell(row=2, column=1).value

        return product
'''
    @staticmethod
    def get_row_count(path, sheet_name):
        """
        Returns number of rows in sheet
        """
        try:
            df = pd.read_excel(path, sheet_name=sheet_name)
            return len(df)
        except Exception as e:
            print(f"Error getting row count: {e}")
            raise

'''