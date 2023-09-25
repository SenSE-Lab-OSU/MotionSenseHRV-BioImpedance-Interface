from data_collection import bluetooth_reciver

'''Setting up a device for data collection is composed of 2 steps:
    1. Create a MSenseCharacteristic object for every characteristic you would like to collect from,
    by inputting a Name, function, and UUID

    2. Create an MSenseDevice object, and add all desired characteristics to it through a list.

A Default Example using the Ohio State SENSE lab devices has been done for you below'''

ppg_sensor = bluetooth_reciver.MSenseCharacteristic("PPG", bluetooth_reciver.ppg_handler,
                                                    "da39c925-1d81-48e2-9c68-d0ae4bbd351f")
magnometer = bluetooth_reciver.MSenseCharacteristic("Magnometer",
                                                    bluetooth_reciver.notification_handler_magnometer,
                                                    "da39c924-1d81-48e2-9c68-d0ae4bbd351f")

accelorometer = bluetooth_reciver.MSenseCharacteristic("Accelorometer",
                                                       bluetooth_reciver.motionsense_handler,
                                                       "da39c921-1d81-48e2-9c68-d0ae4bbd351f")

accelorometer_ENMO = bluetooth_reciver.MSenseCharacteristic("Accelorometer_ENMO",
                                                       bluetooth_reciver.motionsense_ENMO_handler,
                                                       "da39c927-1d81-48e2-9c68-d0ae4bbd351f")

#ommitting magnometer for now 
RightSensor = bluetooth_reciver.MSenseDevice("RightMotionSense2", [ppg_sensor, accelorometer,accelorometer_ENMO])
LeftSensor = bluetooth_reciver.MSenseDevice("LeftMotionSense2", [ppg_sensor, accelorometer,accelorometer_ENMO])
# to replace, comment out the above 2 lines of code and replace it with these:
#  
#RightSensor = bluetooth_reciver.MSenseDevice("RightMotionSense2", [ppg_sensor, magnometer, accelorometer])
#LeftSensor = bluetooth_reciver.MSenseDevice("LeftMotionSense2", [ppg_sensor, magnometer, accelorometer])

# Start BioImpedance Setup

#MagnitudeImpedance = bluetooth_reciver.MSenseCharacteristic("BioImpedance", bluetooth_reciver.BioImpedanceHandle, "DA39C924-1D81-48E2-9C68-D0AE4BBD351F")

#LBioZSensor = bluetooth_reciver.MSenseDevice("LBIOZ", [MagnitudeImpedance])

#RBioZSensor = bluetooth_reciver.MSenseDevice("RBIOZ", [MagnitudeImpedance])



all_sensors = [ RightSensor, LeftSensor ]




