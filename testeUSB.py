import usb.core
import usb.util

ID_VENDOR = 0x18d1
ID_PRODUCT = 0x4ee2

# find our device
dev = usb.core.find(idVendor=ID_VENDOR, idProduct=ID_PRODUCT)

if dev is None:
    raise ValueError('Device not found')

 # set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

print cfg

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('test')