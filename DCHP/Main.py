import ipaddress
from DHCP import DHCP

count = 0  # contador para el array creacion de rango de ip's (arrays empiezan por 0)
network = ipaddress.ip_network("192.168.0.0/24")  # ip de red y la mascara

print("Enciendiendo DHCP")  # peticion de datos para DHCP y el numero de PC en la red
print("Que ip debe tener el servidor DHCP? (192.168.0.?)")
x = input()
ipStaticDHCP = ipaddress.ip_address(x)
print("Introduzca la ip que desea que empieze el rango (192.168.0.?)")
c = input()
ipInicioRango = ipaddress.ip_address(c)
print("Que rango de ip's desea? (numero de PC's)")
NumPCRango = int(input())

print("Creando DHCP IP local estatica: " + str(ipInicioRango))  # comprovador de datos introducidos para el DHCP
print("Su IP de inicio del rango és: " + str(ipInicioRango) + " un maximo de " + str(NumPCRango) + " de PC's")

DHCPServer = DHCP(ipStaticDHCP, ipInicioRango, NumPCRango, network)  # envio de datos para la clase DHCP

print(DHCPServer.getipStaticDHCP(), DHCPServer.getipInicioRango(), DHCPServer.NumPCRango, DHCPServer.network)
# comprovador de creacion de objeto de la DHCP ^

ipAInsertar = DHCPServer.getipInicioRango() # switch de variable para añadir al array sin modificar atributo

print("")
print("La lista de ip's es la siguiente: ")
print("")

while count < DHCPServer.getNumPCRango():  # crear lista para ips
    DHCPServer.anadirDisponibles(ipAInsertar)
    ipAInsertar = ipAInsertar + 1
    count = count + 1

print(DHCPServer.getipDisponibles())

print("")
print("Fin lista")
print("")



