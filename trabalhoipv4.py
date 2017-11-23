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

cont = 0
for i in range(0,int(cmd.numroteadores)-1,1):
	containerlist.append(ns.network.NodeContainer())
	containerlist[cont].Add(routeadoreslist[i])
	containerlist[cont].Add(routeadoreslist[i+1])
	cont+=1

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


ripRouting = ns.internet.RipHelper();
ripRouting.ExcludeInterface(routeadoreslist[0],1);
ripRouting.ExcludeInterface(routeadoreslist[int(cmd.numroteadores)-1],2);

listRH = ns.internet.Ipv4ListRoutingHelper();
listRH.Add(ripRouting,0);

#staticRh = ns.internet.Ipv6StaticRoutingHelper();
#listRH.Add(staticRh, 5);



internetv6 = ns.internet.InternetStackHelper()
internetv6.SetIpv6StackInstall(False);
internetv6.SetRoutingHelper (listRH);
internetv6.Install(routers);

internetv6Nodes = ns.internet.InternetStackHelper()
internetv6Nodes.SetIpv6StackInstall(False);
internetv6Nodes.Install(nodes);

address = ns.internet.Ipv4AddressHelper();
address.SetBase(ns.network.Ipv4Address("192.168.1.0"), ns.network.Ipv4Mask("255.255.255.0"))
clientesInterfaces = address.Assign(clientesDevices)

interfaceslist = []

cont = 2
for i in deviceslist:
	address.SetBase(ns.network.Ipv4Address("192.168."+str(cont)+".0"), ns.network.Ipv4Mask("255.255.255.0"))
	interfaceslist.append(address.Assign(i))
	cont+=1

address.SetBase(ns.network.Ipv4Address("192.168.20.0"), ns.network.Ipv4Mask("255.255.255.0"))
finalInterfaces = address.Assign(finalDevices)

for i in clienteslist:
	static = ns.internet.Ipv4StaticRoutingHelper();
	static = static.GetStaticRouting(i.GetObject(ns.internet.Ipv4.GetTypeId()));
	static.AddHostRouteTo(ns.network.Ipv4Address("192.168.20.2"),ns.network.Ipv4Address("192.168.1."+str(int(cmd.numeroclientes)+1)),1);

static = ns.internet.Ipv4StaticRoutingHelper();
static = static.GetStaticRouting(s1.GetObject(ns.internet.Ipv4.GetTypeId()));
cont=1
for i in clienteslist:
	static.AddHostRouteTo(ns.network.Ipv4Address("192.168.1."+str(cont)),ns.network.Ipv4Address("192.168.20.1"),1);
	cont+=1

echoServer = ns.applications.UdpEchoServerHelper(9)

serverApps = echoServer.Install(final.Get(1))
serverApps.Start(ns.core.Seconds(0.0))
serverApps.Stop(ns.core.Seconds(930.0))

echoClient = ns.applications.UdpEchoClientHelper(finalInterfaces.GetAddress(1), 9)
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
	clientappslist[cont].Start(ns.core.Seconds(50.0+tempolist[cont]))
	clientappslist[cont].Stop(ns.core.Seconds(930.0))
	cont+=1



ns.core.Simulator.Stop(ns.core.Seconds(930.0))
ns.core.Simulator.Run()
ns.core.Simulator.Destroy()

