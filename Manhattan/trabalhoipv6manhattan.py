# -*-  Mode: Python; -*-
# /*
#  * This program is free software; you can redistribute it and/or modify
#  * it under the terms of the GNU General Public License version 2 as
#  * published by the Free Software Foundation;
#  *
#  * This program is distributed in the hope that it will be useful,
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  * GNU General Public License for more details.
#  *
#  * You should have received a copy of the GNU General Public License
#  * along with this program; if not, write to the Free Software
#  * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#  *
#  * Ported to Python by Mohit P. Tahiliani
#  */

import ns.core
import ns.network
import ns.csma
import ns.internet
import ns.point_to_point
import ns.applications
import sys
from random import uniform

# // Default Network Topology
# //
# //       	   
# // n1---r1--r2--r3--r4--r5---s1
# //    	point-to-point  
# // 
# //

cmd = ns.core.CommandLine()
cmd.verbose = "True"
cmd.AddValue("numroteadores", "Numero de Roteadores")
cmd.AddValue("tamanhodepacotes", "Tamanho dos pacotes")
cmd.AddValue("numeroclientes", "Numero de Clientes")
cmd.AddValue("intervalodepacotes", "Valor do intervalo de pacotes")
cmd.Parse(sys.argv)

clienteslist = []
routeadoreslist = []

for i in range(int(cmd.numeroclientes)):
	clienteslist.append(ns.network.Node())

for i in range(int(cmd.numroteadores)):
	routeadoreslist.append(ns.network.Node())	


verbose = cmd.verbose

ns.core.LogComponentEnable("UdpEchoClientApplication", ns.core.LOG_LEVEL_INFO)
ns.core.LogComponentEnable("UdpEchoServerApplication", ns.core.LOG_LEVEL_INFO)

'''
n1 = ns.network.Node()

r1 = ns.network.Node()
r2 = ns.network.Node()
r3 = ns.network.Node()
r4 = ns.network.Node()
r5 = ns.network.Node()
'''
s1 = ns.network.Node()

containerlist = []

clientes = ns.network.NodeContainer()
for i in clienteslist:
	clientes.Add(i)
clientes.Add(routeadoreslist[0])

containerlist.append(ns.network.NodeContainer())
containerlist[0].Add(routeadoreslist[0])
containerlist[0].Add(routeadoreslist[12])

containerlist.append(ns.network.NodeContainer())
containerlist[1].Add(routeadoreslist[0])
containerlist[1].Add(routeadoreslist[1])

containerlist.append(ns.network.NodeContainer())
containerlist[2].Add(routeadoreslist[0])
containerlist[2].Add(routeadoreslist[4])

containerlist.append(ns.network.NodeContainer())
containerlist[3].Add(routeadoreslist[0])
containerlist[3].Add(routeadoreslist[3])

containerlist.append(ns.network.NodeContainer())
containerlist[4].Add(routeadoreslist[1])
containerlist[4].Add(routeadoreslist[13])

containerlist.append(ns.network.NodeContainer())
containerlist[5].Add(routeadoreslist[1])
containerlist[5].Add(routeadoreslist[2])

containerlist.append(ns.network.NodeContainer())
containerlist[6].Add(routeadoreslist[1])
containerlist[6].Add(routeadoreslist[5])

containerlist.append(ns.network.NodeContainer())
containerlist[7].Add(routeadoreslist[2])
containerlist[7].Add(routeadoreslist[14])

containerlist.append(ns.network.NodeContainer())
containerlist[8].Add(routeadoreslist[2])
containerlist[8].Add(routeadoreslist[3])

containerlist.append(ns.network.NodeContainer())
containerlist[9].Add(routeadoreslist[2])
containerlist[9].Add(routeadoreslist[6])

containerlist.append(ns.network.NodeContainer())
containerlist[10].Add(routeadoreslist[3])
containerlist[10].Add(routeadoreslist[15])

containerlist.append(ns.network.NodeContainer())
containerlist[11].Add(routeadoreslist[3])
containerlist[11].Add(routeadoreslist[7])

# linha de cima

containerlist.append(ns.network.NodeContainer())
containerlist[12].Add(routeadoreslist[4])
containerlist[12].Add(routeadoreslist[5])

containerlist.append(ns.network.NodeContainer())
containerlist[13].Add(routeadoreslist[4])
containerlist[13].Add(routeadoreslist[8])

containerlist.append(ns.network.NodeContainer())
containerlist[14].Add(routeadoreslist[4])
containerlist[14].Add(routeadoreslist[7])


containerlist.append(ns.network.NodeContainer())
containerlist[15].Add(routeadoreslist[5])
containerlist[15].Add(routeadoreslist[6])

containerlist.append(ns.network.NodeContainer())
containerlist[16].Add(routeadoreslist[5])
containerlist[16].Add(routeadoreslist[9])

containerlist.append(ns.network.NodeContainer())
containerlist[17].Add(routeadoreslist[6])
containerlist[17].Add(routeadoreslist[7])

containerlist.append(ns.network.NodeContainer())
containerlist[18].Add(routeadoreslist[6])
containerlist[18].Add(routeadoreslist[10])

containerlist.append(ns.network.NodeContainer())
containerlist[19].Add(routeadoreslist[7])
containerlist[19].Add(routeadoreslist[11])

## linha 2

containerlist.append(ns.network.NodeContainer())
containerlist[20].Add(routeadoreslist[8])
containerlist[20].Add(routeadoreslist[9])

containerlist.append(ns.network.NodeContainer())
containerlist[21].Add(routeadoreslist[8])
containerlist[21].Add(routeadoreslist[12])

containerlist.append(ns.network.NodeContainer())
containerlist[22].Add(routeadoreslist[8])
containerlist[22].Add(routeadoreslist[11])


containerlist.append(ns.network.NodeContainer())
containerlist[23].Add(routeadoreslist[9])
containerlist[23].Add(routeadoreslist[10])

containerlist.append(ns.network.NodeContainer())
containerlist[24].Add(routeadoreslist[9])
containerlist[24].Add(routeadoreslist[13])

containerlist.append(ns.network.NodeContainer())
containerlist[25].Add(routeadoreslist[10])
containerlist[25].Add(routeadoreslist[11])

containerlist.append(ns.network.NodeContainer())
containerlist[26].Add(routeadoreslist[10])
containerlist[26].Add(routeadoreslist[14])

containerlist.append(ns.network.NodeContainer())
containerlist[27].Add(routeadoreslist[11])
containerlist[27].Add(routeadoreslist[15])

#terceira linha

containerlist.append(ns.network.NodeContainer())
containerlist[28].Add(routeadoreslist[12])
containerlist[28].Add(routeadoreslist[13])

containerlist.append(ns.network.NodeContainer())
containerlist[29].Add(routeadoreslist[12])
containerlist[29].Add(routeadoreslist[15])

containerlist.append(ns.network.NodeContainer())
containerlist[30].Add(routeadoreslist[13])
containerlist[30].Add(routeadoreslist[14])

containerlist.append(ns.network.NodeContainer())
containerlist[31].Add(routeadoreslist[14])
containerlist[31].Add(routeadoreslist[15])

final = ns.network.NodeContainer()
final.Add(routeadoreslist[int(cmd.numroteadores)-1])
final.Add(s1)


nodes = ns.network.NodeContainer();
for i in clienteslist:
	nodes.Add(i)
nodes.Add(s1);

routers = ns.network.NodeContainer();
for i in routeadoreslist:
	routers.Add(i);


csma = ns.csma.CsmaHelper()
csma.SetChannelAttribute("DataRate", ns.core.StringValue("100Mbps"))
csma.SetChannelAttribute("Delay", ns.core.StringValue("2ms"))


clientesDevices = csma.Install(clientes);

deviceslist = []

for i in containerlist:
	deviceslist.append(csma.Install(i));

finalDevices = csma.Install(final);


ripNgRouting = ns.internet.RipNgHelper();
ripNgRouting.ExcludeInterface(routeadoreslist[0],1);
ripNgRouting.ExcludeInterface(routeadoreslist[int(cmd.numroteadores)-1],6);

listRH = ns.internet.Ipv6ListRoutingHelper();
listRH.Add(ripNgRouting,0);

#staticRh = ns.internet.Ipv6StaticRoutingHelper();
#listRH.Add(staticRh, 5);



internetv6 = ns.internet.InternetStackHelper()
internetv6.SetIpv4StackInstall(False);
internetv6.SetRoutingHelper (listRH);
internetv6.Install(routers);

internetv6Nodes = ns.internet.InternetStackHelper()
internetv6Nodes.SetIpv4StackInstall(False);
internetv6Nodes.Install(nodes);

address = ns.internet.Ipv6AddressHelper();
address.SetBase(ns.network.Ipv6Address("2001:1::"), ns.network.Ipv6Prefix(64))
clienteInterfaces = address.Assign(clientesDevices)
clienteInterfaces.SetForwarding(int(cmd.numeroclientes), True)
clienteInterfaces.SetDefaultRouteInAllNodes(int(cmd.numeroclientes))

interfaceslist = []
cont = 2
cont2= 0
for i in deviceslist:
	address.SetBase(ns.network.Ipv6Address("2001:"+str(cont)+"::"), ns.network.Ipv6Prefix(64))
	interfaceslist.append(address.Assign(i))
	interfaceslist[cont2].SetForwarding(0, True)
	interfaceslist[cont2].SetForwarding(1, True)
	cont2+=1
	cont+=1

address.SetBase(ns.network.Ipv6Address("2001:40::"), ns.network.Ipv6Prefix(64))
finalInterfaces = address.Assign(finalDevices)
finalInterfaces.SetForwarding(0, True)
finalInterfaces.SetDefaultRouteInAllNodes(0)



echoServer = ns.applications.UdpEchoServerHelper(9)

serverApps = echoServer.Install(final.Get(1))
serverApps.Start(ns.core.Seconds(0.0))
serverApps.Stop(ns.core.Seconds(930.0))


echoClient = ns.applications.UdpEchoClientHelper(finalInterfaces.GetAddress(1,1), 9)
echoClient.SetAttribute("MaxPackets", ns.core.UintegerValue(500))
echoClient.SetAttribute("Interval", ns.core.TimeValue(ns.core.Seconds (float(cmd.intervalodepacotes))))
echoClient.SetAttribute("PacketSize", ns.core.UintegerValue(int(cmd.tamanhodepacotes)))

tempolist=[]
for i in clienteslist:
	tempolist.append(uniform(0,2))

clientappslist = []
cont = 0
for i in clienteslist:
	clientappslist.append(echoClient.Install(clientes.Get(cont)))
	clientappslist[cont].Start(ns.core.Seconds(150.0+tempolist[cont]))
	clientappslist[cont].Stop(ns.core.Seconds(930.0))
	cont+=1


ns.core.Simulator.Stop(ns.core.Seconds(930.0))
ns.core.Simulator.Run()
ns.core.Simulator.Destroy()

