import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType, PdfSaveOptions

workbook = Workbook("timeentrydownload.xlsx")
saveOptions = PdfSaveOptions()
saveOptions.setOnePagePerSheet(True)
workbook.save("example.pdf", saveOptions)

jpype.shutdownJVM()