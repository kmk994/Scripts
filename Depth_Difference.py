#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      FL060882
#
# Created:     12/06/2019
# Copyright:   (c) FL060882 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import pandas as pd
import arcpy.mapping
from PyPDF2 import PdfFileMerger, PdfFileReader


# Set input csv file
InputCSV = 'Depth_Difference.csv'

# Set relative path
fileDir = os.path.dirname(os.path.realpath('__file__'))
InputFile = os.path.join(fileDir, InputCSV)

# Extract data from input file
data = pd.read_csv(InputFile,sep=",")

MXD_Template = map(lambda x: os.path.join(fileDir, x), data['MXD_Template'].tolist())
Path_Layer = data['Path_Layer'].tolist()
Name_Layer1 = data['Name_Layer1'].tolist()
Name_Simulation = data['Name_Simulation'].tolist()
Return_Period = data['Return_Period'].tolist()
Type_Simulation = data['Type_Simulation'].tolist()
Fut_Epoch = data['Fut_Epoch'].tolist()
Storm_Duration = data['Storm_Duration'].tolist()
Drawing_number = data['Drawing_number'].tolist()
Sheet = data['Sheet'].tolist()
CC = data['CC'].tolist()

# Itarate input files and create maps
merger = PdfFileMerger()

for i in range(len(MXD_Template)):
    print(i)
    mxd = arcpy.mapping.MapDocument(MXD_Template[i])
    df = arcpy.mapping.ListDataFrames(mxd)[0]

    lyr = arcpy.mapping.ListLayers(mxd, "Results", df)[0]  # Wczesniej bylo "" i [25]
    lyr.replaceDataSource(Path_Layer[i], "RASTER_WORKSPACE", Name_Layer1[i])

    title_fig = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[13]
    title_fig.text = "FRA - Coalhouse Point Modelling Results" + "\r\n" + "Difference in maximum flood depth" + "\r\n" + \
                 Name_Simulation[i] + "\r\n" + Sheet[i]

    title_fig = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[12]
    title_fig.text = Drawing_number[i]

    title_fig = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[7]
    title_fig.text = Storm_Duration[i]

    title_fig = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[6]
    title_fig.text = str(Return_Period[i])

    title_fig = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[5]
    title_fig.text = str(CC[i])

    title_fig = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[4]
    title_fig.text = str(Fut_Epoch[i])

    arcpy.RefreshTOC()
    arcpy.RefreshActiveView()

    tmpPdf = os.path.join(fileDir, Drawing_number[i] + ".pdf")
    arcpy.mapping.ExportToPDF(mxd, tmpPdf)
    fd = file(tmpPdf, 'rb')
    merger.append(PdfFileReader(fd))
    fd.close()

merger.write(os.path.join(fileDir, "Maps\Depth_Difference.pdf"))
