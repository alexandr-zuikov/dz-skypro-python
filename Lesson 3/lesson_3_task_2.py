from smartphone import Smartphone

catalog = [Smartphone("Nokia","6260","+79168466176"),
           Smartphone("HTC","Titan 2","+79168466176"),
           Smartphone("Nokia","Lumia 1520","+79168466176"),
           Smartphone("Meizu","MX4 Pro","+79118491230"),
           Smartphone("Apple","iPhone XS Max","+79118491230")]

for phone in catalog:
    phone.print_catalog()