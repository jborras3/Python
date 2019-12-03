import ipaddress
from DHCP import DHCP
from PC import PC
from switch import switch
from router import router

count = 0  # contador para el array creacion de rango de ip's (arrays empiezan por 0)
network = ipaddress.ip_network("192.168.0.0/24")  # ip de red y la mascara
gateway = "/24"
numTotalPC = 0
switch = switch("", "", network, "")


print("Enciendiendo switch")
print("Enciendiendo router")
print("Enciendiendo DHCP")  # peticion de datos para DHCP y el numero de PC en la red
print("2%")
print("15%")
print("37%")
print("52%")
print("69%")
print("84%")
print("100%")
print("Entrando en configuración del DHCP")
print("")
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
DHCPServer = DHCP(ipStaticDHCP, ipInicioRango, NumPCRango, network, gateway)  # envio de datos para la clase DHCP
print(DHCPServer.getipStaticDHCP(), DHCPServer.getipInicioRango(), DHCPServer.getNumPCRango(), DHCPServer.getnetwork(), DHCPServer.getGateway())
# comprobador de creacion de objeto de la DHCP ^
ipAInsertar = DHCPServer.getipInicioRango() # switch de variable para añadir al array sin modificar atributo
print("")
print("La lista de ip's es la siguiente: ")
print("")
while count < DHCPServer.getNumPCRango():  # crear lista para ips
    DHCPServer.anadirDisponibles(ipAInsertar)  # añade al DHCP
    switch.anadirDisponibles(ipAInsertar)  # añade al switch
    ipAInsertar += 1
    count += 1

print(DHCPServer.getipDisponibles())
print("")
print("Fin lista")
print("")

while numTotalPC > NumPCRango or numTotalPC == 0:
    print("Cuantos pc's quieres?")
    numTotalPC = int(input())

print("")
print("Creando PC's")
print("")
count = 0
while count < numTotalPC:
    ip = DHCPServer.getipDisponibles()[0]
    pc = PC("pc" + str(count), ip, network, gateway)
    switch.anadirPCs(pc)
    DHCPServer.getipDisponibles().pop(0)
    switch.getipDisponibles().pop(0)
    count += 1

print("Lista de ordenadores:")
switch.getInfoPcs()
print("")
print("IP libres restantes:")
print("")
print(switch.getipDisponibles())
print("")
print("Info router")
router = router()
switch.setDHCP(DHCPServer)
router.AddSwitch(switch)
for switchs in router.getSwitches():
    switch.getInfoPcs()