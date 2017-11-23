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


s1 = ns.network.Node()

containerlist = []

clientes = ns.network.NodeContainer()
for i in clienteslist:
	clientes.Add(i)
clientes.Add(routeadoreslist[0])

# MX - GT
containerlist.append(ns.network.NodeContainer())
containerlist[0].Add(routeadoreslist[0])
containerlist[0].Add(routeadoreslist[1])

# MX - US
containerlist.append(ns.network.NodeContainer())
containerlist[1].Add(routeadoreslist[0])
containerlist[1].Add(routeadoreslist[18])

# GT - SV
containerlist.append(ns.network.NodeContainer())
containerlist[2].Add(routeadoreslist[1])
containerlist[2].Add(routeadoreslist[2])

# SV - NI
containerlist.append(ns.network.NodeContainer())
containerlist[3].Add(routeadoreslist[2])
containerlist[3].Add(routeadoreslist[3])

# SV - CR
containerlist.append(ns.network.NodeContainer())
containerlist[4].Add(routeadoreslist[2])
containerlist[4].Add(routeadoreslist[4])

# NI - CR
containerlist.append(ns.network.NodeContainer())
containerlist[5].Add(routeadoreslist[3])
containerlist[5].Add(routeadoreslist[4])

# CR - HN
containerlist.append(ns.network.NodeContainer())
containerlist[6].Add(routeadoreslist[4])
containerlist[6].Add(routeadoreslist[5])

# HN - PA
containerlist.append(ns.network.NodeContainer())
containerlist[7].Add(routeadoreslist[5])
containerlist[7].Add(routeadoreslist[6])

# PA - VE
containerlist.append(ns.network.NodeContainer())
containerlist[8].Add(routeadoreslist[6])
containerlist[8].Add(routeadoreslist[7])

# PA - BR
containerlist.append(ns.network.NodeContainer())
containerlist[9].Add(routeadoreslist[6])
containerlist[9].Add(routeadoreslist[14])

# PA - CU
containerlist.append(ns.network.NodeContainer())
containerlist[10].Add(routeadoreslist[6])
containerlist[10].Add(routeadoreslist[17])

# PA - CO
containerlist.append(ns.network.NodeContainer())
containerlist[11].Add(routeadoreslist[6])
containerlist[11].Add(routeadoreslist[8])

# CO - CL
containerlist.append(ns.network.NodeContainer())
containerlist[12].Add(routeadoreslist[8])
containerlist[12].Add(routeadoreslist[11])

# EC - PE
containerlist.append(ns.network.NodeContainer())
containerlist[13].Add(routeadoreslist[9])
containerlist[13].Add(routeadoreslist[10])

# PE - CL
containerlist.append(ns.network.NodeContainer())
containerlist[14].Add(routeadoreslist[10])
containerlist[14].Add(routeadoreslist[11])

# CL - BO
containerlist.append(ns.network.NodeContainer())
containerlist[15].Add(routeadoreslist[11])
containerlist[15].Add(routeadoreslist[16])

# CL - PY
containerlist.append(ns.network.NodeContainer())
containerlist[16].Add(routeadoreslist[11])
containerlist[16].Add(routeadoreslist[15])

# CL - AR
containerlist.append(ns.network.NodeContainer())
containerlist[17].Add(routeadoreslist[11])
containerlist[17].Add(routeadoreslist[12])

# AR - UY
containerlist.append(ns.network.NodeContainer())
containerlist[18].Add(routeadoreslist[12])
containerlist[18].Add(routeadoreslist[14])

# AR - UY
containerlist.append(ns.network.NodeContainer())
containerlist[19].Add(routeadoreslist[12])
containerlist[19].Add(routeadoreslist[13])

# BR - US
containerlist.append(ns.network.NodeContainer())
containerlist[20].Add(routeadoreslist[14])
containerlist[20].Add(routeadoreslist[18])

# BR - UK
containerlist.append(ns.network.NodeContainer())
containerlist[21].Add(routeadoreslist[14])
containerlist[21].Add(routeadoreslist[19])

# PY - BR
containerlist.append(ns.network.NodeContainer())
containerlist[22].Add(routeadoreslist[15])
containerlist[22].Add(routeadoreslist[14])

# BO - CU
containerlist.append(ns.network.NodeContainer())
containerlist[23].Add(routeadoreslist[16])
containerlist[23].Add(routeadoreslist[17])

# CU - US
containerlist.append(ns.network.NodeContainer())
containerlist[24].Add(routeadoreslist[17])
containerlist[24].Add(routeadoreslist[18])



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




csmaCli = ns.csma.CsmaHelper()
csmaCli.SetChannelAttribute("DataRate", ns.core.StringValue("2Gbps"))
csmaCli.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csma300 = ns.csma.CsmaHelper()
csma300.SetChannelAttribute("DataRate", ns.core.StringValue("300Mbps"))
csma300.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csma400 = ns.csma.CsmaHelper()
csma400.SetChannelAttribute("DataRate", ns.core.StringValue("400Mbps"))
csma400.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csma600 = ns.csma.CsmaHelper()
csma600.SetChannelAttribute("DataRate", ns.core.StringValue("600Mbps"))
csma600.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csma1 = ns.csma.CsmaHelper()
csma1.SetChannelAttribute("DataRate", ns.core.StringValue("1Gbps"))
csma1.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csma2 = ns.csma.CsmaHelper()
csma2.SetChannelAttribute("DataRate", ns.core.StringValue("2Gbps"))
csma2.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csma25 = ns.csma.CsmaHelper()
csma25.SetChannelAttribute("DataRate", ns.core.StringValue("2.5Gbps"))
csma25.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csma5 = ns.csma.CsmaHelper()
csma5.SetChannelAttribute("DataRate", ns.core.StringValue("5Gbps"))
csma5.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csma10 = ns.csma.CsmaHelper()
csma10.SetChannelAttribute("DataRate", ns.core.StringValue("10Gbps"))
csma10.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csma100 = ns.csma.CsmaHelper()
csma100.SetChannelAttribute("DataRate", ns.core.StringValue("100Gbps"))
csma100.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))


clientesDevices = csmaCli.Install(clientes);

deviceslist = []

lista300 = [19]
lista400 = [4,6,7]
lista600 = [13]
lista1 = [1]
lista2 = [8]
lista25 = [0,2,3,5,14]
lista5 = [21]
lista10 = [9,10,11,12,15,16,17,18,22,23,24]
lista100 = [20]
cont = 0
for i in containerlist:
	if cont in lista300:
		deviceslist.append(csma300.Install(i))
	elif cont in lista400:
		deviceslist.append(csma400.Install(i));	
	elif cont in lista600:
		deviceslist.append(csma600.Install(i));
	elif cont in lista1:
		deviceslist.append(csma1.Install(i));
	elif cont in lista2:
		deviceslist.append(csma2.Install(i));
	elif cont in lista25:
		deviceslist.append(csma25.Install(i));
	elif cont in lista5:
		deviceslist.append(csma5.Install(i));
	elif cont in lista10:
		deviceslist.append(csma10.Install(i));
	elif cont in lista100:
		deviceslist.append(csma100.Install(i));			
	cont+=1

finalDevices = csmaCli.Install(final);


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

address.SetBase(ns.network.Ipv4Address("192.168.50.0"), ns.network.Ipv4Mask("255.255.255.0"))
finalInterfaces = address.Assign(finalDevices)

for i in clienteslist:
	static = ns.internet.Ipv4StaticRoutingHelper();
	static = static.GetStaticRouting(i.GetObject(ns.internet.Ipv4.GetTypeId()));
	static.AddHostRouteTo(ns.network.Ipv4Address("192.168.50.2"),ns.network.Ipv4Address("192.168.1."+str(int(cmd.numeroclientes)+1)),1);

static = ns.internet.Ipv4StaticRoutingHelper();
static = static.GetStaticRouting(s1.GetObject(ns.internet.Ipv4.GetTypeId()));
cont=1
for i in clienteslist:
	static.AddHostRouteTo(ns.network.Ipv4Address("192.168.1."+str(cont)),ns.network.Ipv4Address("192.168.50.1"),1);
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
	clientappslist[cont].Start(ns.core.Seconds(150.0+tempolist[cont]))
	clientappslist[cont].Stop(ns.core.Seconds(930.0))
	cont+=1

#csma10.EnablePcapAll("manhattan")


ns.core.Simulator.Stop(ns.core.Seconds(930.0))
ns.core.Simulator.Run()
ns.core.Simulator.Destroy()

