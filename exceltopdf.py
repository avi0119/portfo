from spire.xls import *
from spire.xls.common import *

def ExcelToPdf(filename,targetpdf):
	# Create a Workbook object
	workbook = Workbook()

	# Load an Excel document
	workbook.LoadFromFile(filename)

	# Iterate through the worksheets in the workbook
	for sheet in workbook.Worksheets: 

	    # Get the PageSetup object
	    pageSetup = sheet.PageSetup

	    # Set page margins
	    pageSetup.TopMargin = 0.3
	    pageSetup.BottomMargin = 0.3
	    pageSetup.LeftMargin = 0.3
	    pageSetup.RightMargin = 0.3

	# Set worksheet to fit to page when converting
	workbook.ConverterSetting.SheetFitToPage = True

	# Convert to PDF file
	workbook.SaveToFile(targetpdf, FileFormat.PDF)
	workbook.Dispose()