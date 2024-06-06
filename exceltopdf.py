# Import Module 
from win32com import client
import pythoncom 


def ExcelToPdf (filename,target):
	# Open Microsoft Excel 
	pythoncom.CoInitialize()
	excel = client.Dispatch("Excel.Application") 

	# Read Excel File 
	sheets = excel.Workbooks.Open(filename) 
	work_sheets = sheets.Worksheets[0] 
	work_sheets.Columns.AutoFit() 
	# Convert into PDF File 
	work_sheets.ExportAsFixedFormat(0, target) 
	sheets.Close(True)

