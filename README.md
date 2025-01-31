# Excel-Binary (xlsb Reader & Exporter)
## Overview
Excel-binary is a Python module designed for reading and exporting .xlsb (Excel Binary Format) files. It provides an easy-to-use interface to convert .xlsb files into Pandas DataFrames or export them directly to CSV/XLSX formats.

## Features
✅ Read .xlsb files into Pandas DataFrames
✅ Export .xlsb sheets to CSV or XLSX formats
✅ Customizable sheet selection for export
✅ Simple & efficient API

## Usage
1. Create an instance with the filename
```python
from excel_binary import xlsb  
newfile = xlsb("test.xlsb")
```
2. Read an .xlsb sheet into a Pandas DataFrame
```python
data_frame_xlsb = newfile.read_xlsb(sheet_number=1)
 ```
3. Export an .xlsb sheet to CSV format
```python
newfile.xlsb_export_csv(sheet_number=1, output_filename="test_output.csv")
```  
5. Export an .xlsb sheet to XLSX format
```python
newfile.xlsb_export_xlsx(sheet_number=1, output_filename="test_output.xlsx", sheet_name="first_sheet")  
```
Note: The sheet_name parameter is optional; it defaults to "Sheet1".

Contributing
Contributions are welcome! If you find a bug or want to add enhancements, feel free to:

Fork the repo
Create a pull request
Report issues
License
This project is licensed under MIT License. See LICENSE for details.
