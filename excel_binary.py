# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:04:34 2019
This code is written to read and export excel binary files using python.

@author: Subhagato Adak (Code help from stackoverflow)
"""
import pandas as pd
from pyxlsb import open_workbook as open_xlsb 

class xlsb :
    def __init__(self,inputfilename):
        self.inputfilename = inputfilename
   
    def read_xlsb(self,sheet_number):
         """
		Enter the sheet number that you need to read and create a data frame, you 
		can use itertions to upload multiple sheets.
	 """
	 df =[]
         with open_xlsb(self.inputfilename) as wb:
             with wb.get_sheet(sheet_number) as sheet:
                 for row in sheet.rows():
                     df.append([item.v for item in row])
                 df = pd.DataFrame(df[1:], columns=df[0])
                 return df
        
    def xlsb_export_csv(self,sheet_number,outputname):
          """
		Enter the sheet number, and ouput file name in the format of .csv that you need to 
		read and create a data frame, you can use itertions to upload multiple sheets.
	  """
	  df =[]
          with open_xlsb(self.inputfilename) as wb:
              with wb.get_sheet(sheet_number) as sheet:
                  for row in sheet.rows():
                      df.append([item.v for item in row])
                  df = pd.DataFrame(df[1:], columns=df[0])
                  df.to_csv(outputname)
                  
    def xlsb_export_xlsx(self,sheet_number,outputname,sheet_name="Sheet1"):
	 """
		Enter the sheet number,output file name and sheet name that you need to read and
		create a data frame, you can use itertions to export multiple sheets.
	 """        
	df =[]
        with open_xlsb(self.inputfilename) as wb:
              with wb.get_sheet(sheet_number) as sheet:
                  for row in sheet.rows():
                      df.append([item.v for item in row])
                  df = pd.DataFrame(df[1:], columns=df[0])
                  df.to_excel(outputname,  sheet_name=sheet_name)
