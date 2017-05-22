import vehiculos_clases as vc

my_vehicleAAF_FighterAT = vc.Vehiculo("A-143 'Buzzard'", "AAF", "Ataque")
my_vehicleAAF_Fighter = vc.Vehiculo("A-149 'Gryphon'", "AAF", "Polivalente")
my_vehicleAAF_CarMR = vc.Vehiculo("Strider", "AAF", "MRAP")
my_vehicleAAF_HeloT = vc.Vehiculo("CH-49 'Mohawk'", "AAF", "Helicóptero")
my_vehicleAAF_Helo = vc.Vehiculo("WY-55 'Hellcat", "AAF", "Helicóptero")
my_vehicleAAF_MBT = vc.Vehiculo("MBT-52 'Kuma", "AAF", "Carro de Combate Principal")
my_vehicleAAF_APC = vc.Vehiculo("AFV-4 'Gorgon'", "AAF", "Vehículo de Transporte de Personal")
my_vehicleAAF_IFV = vc.Vehiculo("FV-720 'Mora'", "AAF", "Vehiculo de Combate de Infatería")

aaf_vehicles = [my_vehicleAAF_FighterAT, my_vehicleAAF_Fighter, my_vehicleAAF_CarMR, my_vehicleAAF_HeloT, my_vehicleAAF_Helo, my_vehicleAAF_MBT, my_vehicleAAF_APC, my_vehicleAAF_IFV]

vehiculo = aaf_vehicles[2]
print(vehiculo)
"""
print(my_vehicleAAF_FighterAT)
print(my_vehicleAAF_Fighter)
print(my_vehicleAAF_CarMR)
print(my_vehicleAAF_HeloT)
print(my_vehicleAAF_Helo)
print(my_vehicleAAF_MBT)
print(my_vehicleAAF_APC)
print(my_vehicleAAF_IFV)
"""