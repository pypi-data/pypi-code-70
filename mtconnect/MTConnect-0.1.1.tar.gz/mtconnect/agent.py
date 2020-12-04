#general imports
import os
import uuid  
from xml.etree import ElementTree
from datetime import datetime

#mtconnect imports
from .storage import MTBuffer, MTDataEntity
from .xmlhelper import read_devices

class MTConnect():
    # ! Use: Handle MTConnect agent
    # ? Data:
    #instanceID 
    instanceId = None
    hostname = None

    #item buffer
    buffer = None
    asset_buffer = None

    #dictionary of devices
    device_dict = None

    def __init__(self,loc='./device.xml',hostname='http://0.0.0.0:80'):
        #set variables
        self.hostname = hostname

        #initalize buffer
        self.buffer = MTBuffer()

        #read device information
        file_location = os.getenv('MTCDeviceFile',loc)
        self.device_dict = read_devices(file_location)

        #generate instanceId -64bit int uuid4 is 128 so shift it
        self.instanceId = uuid.uuid4().int & (1<<64)-1

    #validate data
    def validate_dataId(self,dataId):
        for device in self.device_dict:
            if(dataId in device.get_sub_item()):
                return True
        return False

    def validate_dataValue(self, dataId, value):
        pass

    #push data from machines
    def push_data(self, dataId, value, type=None, sub_type=None):
        
        new_data = MTDataEntity(dataId, value,type,sub_type)
    
    #run MTConnect probe command
    def probe(self):
        root_container = ElementTree.Element('MTConnectDevices')
        header_element = ElementTree.SubElement(root_container, 'Header')
        header_element.set('version','1.6.0.0')
        header_element.set('instanceId',str(self.instanceId))
        header_element.set('creationTime',datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))
        header_element.set('bufferSize',str(self.buffer.buffer_size))
        header_element.set('assetBufferSize','0')
        header_element.set('assetCount','0')

        device_container = ElementTree.SubElement(root_container, 'Devices')
        for device in self.device_dict:
            device_container.append(self.device_dict[device].xml_data)
        
        return ElementTree.tostring(root_container).decode()

    #run MTConnect sample command
    def sample(self, path, start, count, interval):
        pass

    #run MTConnnect current command
    def current(self, at, path):
        pass