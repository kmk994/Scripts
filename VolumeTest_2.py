
import arcpy
import csv
arcpy.CheckOutExtension("3D")
arcpy.env.workspace = r"C:\Pliki\Local Coalhouse Point\Storage_calculations_v2"

inSurface1 = r"C:\Pliki\Local Coalhouse Point\Storage_calculations_v2\tin\Existing_Channel_post"


result = arcpy.SurfaceVolume_3d(inSurface1, "Post_41.csv", "BELOW", "3.7", "1", "0")
result1 = arcpy.SurfaceVolume_3d(inSurface1, "Post_40.csv", "BELOW", "3.6", "1", "0")
result2 = arcpy.SurfaceVolume_3d(inSurface1, "Post_39.csv", "BELOW", "3.5", "1", "0")
result3 = arcpy.SurfaceVolume_3d(inSurface1, "Post_38.csv", "BELOW", "3.4", "1", "0")
result4 = arcpy.SurfaceVolume_3d(inSurface1, "Post_37.csv", "BELOW", "3.3", "1", "0")
result5 = arcpy.SurfaceVolume_3d(inSurface1, "Post_36.csv", "BELOW", "3.2", "1", "0")
result6 = arcpy.SurfaceVolume_3d(inSurface1, "Post_35.csv", "BELOW", "3.1", "1", "0")
result7 = arcpy.SurfaceVolume_3d(inSurface1, "Post_34.csv", "BELOW", "3", "1", "0")
result8 = arcpy.SurfaceVolume_3d(inSurface1, "Post_33.csv", "BELOW", "2.9", "1", "0")
result9 = arcpy.SurfaceVolume_3d(inSurface1, "Post_32.csv", "BELOW", "2.8", "1", "0")
result10 = arcpy.SurfaceVolume_3d(inSurface1, "Post_31.csv", "BELOW", "2.7", "1", "0")
result11 = arcpy.SurfaceVolume_3d(inSurface1, "Post_30.csv", "BELOW", "2.6", "1", "0")
result12 = arcpy.SurfaceVolume_3d(inSurface1, "Post_29.csv", "BELOW", "2.5", "1", "0")
result13 = arcpy.SurfaceVolume_3d(inSurface1, "Post_28.csv", "BELOW", "2.4", "1", "0")
result14 = arcpy.SurfaceVolume_3d(inSurface1, "Post_27.csv", "BELOW", "2.3", "1", "0")
result15 = arcpy.SurfaceVolume_3d(inSurface1, "Post_26.csv", "BELOW", "2.2", "1", "0")
result16 = arcpy.SurfaceVolume_3d(inSurface1, "Post_25.csv", "BELOW", "2.1", "1", "0")
result17 = arcpy.SurfaceVolume_3d(inSurface1, "Post_24.csv", "BELOW", "2", "1", "0")
result18 = arcpy.SurfaceVolume_3d(inSurface1, "Post_23.csv", "BELOW", "1.9", "1", "0")
result19 = arcpy.SurfaceVolume_3d(inSurface1, "Post_22.csv", "BELOW", "1.89", "1", "0")
result20 = arcpy.SurfaceVolume_3d(inSurface1, "Post_21.csv", "BELOW", "1.84", "1", "0")
result21 = arcpy.SurfaceVolume_3d(inSurface1, "Post_20.csv", "BELOW", "1.8", "1", "0")
result22 = arcpy.SurfaceVolume_3d(inSurface1, "Post_19.csv", "BELOW", "1.79", "1", "0")
result23 = arcpy.SurfaceVolume_3d(inSurface1, "Post_18.csv", "BELOW", "1.74", "1", "0")
result24 = arcpy.SurfaceVolume_3d(inSurface1, "Post_17.csv", "BELOW", "1.7", "1", "0")
result25 = arcpy.SurfaceVolume_3d(inSurface1, "Post_16.csv", "BELOW", "1.64", "1", "0")
result26 = arcpy.SurfaceVolume_3d(inSurface1, "Post_15.csv", "BELOW", "1.6", "1", "0")
result27 = arcpy.SurfaceVolume_3d(inSurface1, "Post_14.csv", "BELOW", "1.5", "1", "0")
result28 = arcpy.SurfaceVolume_3d(inSurface1, "Post_13.csv", "BELOW", "1.4", "1", "0")
result29 = arcpy.SurfaceVolume_3d(inSurface1, "Post_12.csv", "BELOW", "1.3", "1", "0")
result30 = arcpy.SurfaceVolume_3d(inSurface1, "Post_11.csv", "BELOW", "1.2", "1", "0")
# List of CSV files to merge
csv_files = ["Post_41.csv", "Post_40.csv", "Post_39.csv", "Post_38.csv", "Post_37.csv", "Post_36.csv", "Post_35.csv", "Post_34.csv", "Post_33.csv", "Post_32.csv", "Post_31.csv", "Post_30.csv", "Post_29.csv", "Post_28.csv", "Post_27.csv", "Post_26.csv", "Post_25.csv", "Post_24.csv", "Post_23.csv", "Post_22.csv", "Post_21.csv", "Post_20.csv", "Post_19.csv", "Post_18.csv", "Post_17.csv", "Post_16.csv", "Post_15.csv", "Post_14.csv", "Post_13.csv", "Post_12.csv","Post_11.csv"]

# Output file name for merged CSV
merged_file = "Existing_channel_post.csv"

# Open output CSV file in write mode
with open(merged_file, 'wb') as output:
    csv_writer = csv.writer(output)

    # Loop through each CSV file and append its contents to the merged CSV
    for csv_file in csv_files:
        with open(csv_file, 'rb') as file:
            csv_reader = csv.reader(file)
            # Skip the header row in all but the first CSV file
            if csv_file != csv_files[0]:
                next(csv_reader)
            for row in csv_reader:
                csv_writer.writerow(row)

print("CSV files merged successfully into '{}'.".format(merged_file))