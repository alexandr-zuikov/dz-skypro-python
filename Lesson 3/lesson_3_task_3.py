from address import Address
from mailing import Mailing

to_address = Address ("193230","Санкт-Петербург","Улица Крыленко", "1", "176")
from_address = Address ("141402","Химки","Улица Гоголя", "6", "126")
mail = Mailing(to_address, from_address, str(123456789), int(150))

print("Отправление", mail.track, "из", 
      mail.from_address.index,",",
      mail.from_address.city,",",
      mail.from_address.street,",",
      mail.from_address.building,"-", 
      mail.from_address.apartament,"в", 
      mail.to_address.index,",", 
      mail.to_address.city,",",
      mail.to_address.street,",",
      mail.to_address.building,"-",
      mail.to_address.apartament, ".",
      "Стоимость", mail.cost, "рублей.")