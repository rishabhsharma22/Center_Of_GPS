This package is used to find a center point of a all the GPS latitude and longitude that are gathered.

Center_Of_GPS.py file has a method called center which takes a single argument that is the location of the file that has latitude and longitude of which the center has to be computed.

To integrate the file in any python program use the command.

Python Code: 'import Center_Of_GPS'

Please keep the file in the folder of site packages of your python location or in the same folder where you are trying to call this file.

Once the file is imported the center method can be called using the below command

Python Code: Center_Of_GPS.center("File_Location")


The function center() return a tuple with the center of all the gps location in the following form.

output: ("center_of_latitude","center_of_longitude")

