# Excel-binary
This python module is written to read and export xlsb data in python. 
We need to enter the filename to create the instance of the xlsb class, then call the read_xlsb method to read the dataset in a dataset in python. We can also use the export methods to directly convert the xlsb file sheets to csv/xlsx formats.



Formats for the code written 

###############################################################################################
##create instance with the filename 

newfile = xlsb("test.xlsb")

##read dataset to a data frame 

data_frame_xlsb = newfile.read_xlsb(1)

##export xlsb file to csv format

newfile.xlsb_export_csv(1,"test_output.csv")

##export xlsb file to xlsx format (sheet name is optional, by default sheet name is set to Sheet1)

newfile.xlsb_export_xlsx(1,"test_output.xlsx","first_sheet")
 #############################################################################################




