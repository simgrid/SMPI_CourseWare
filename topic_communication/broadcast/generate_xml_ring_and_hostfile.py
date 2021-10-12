#!/usr/bin/env python3
import sys
import os
import math

# Link parameters
link_latency = "10us"
link_bandwidth = 10
link_bandwidth_unit = "Gbps"

# XML generation functions
def issueHead():
        head = ("<?xml version='1.0'?>\n"
                "<!DOCTYPE platform SYSTEM \"http://simgrid.gforge.inria.fr/simgrid/simgrid.dtd\">\n"
                "<platform version=\"4.1\">\n\n")

        config_clause = ("<!--  WARNING:  This <config></config> clause below\n"
                       "makes it so that NO COMPUTATION TIME is simulated. This is because\n"
                       "in this module, for pedagogic purposes, we don't want to muddy the\n"
                       "(simulation) waters with computational times. As a results, this\n"
                       "XML platform file may not be suitable for running other\n"
                       "simulations, unless you remove the <config></config> clause.\n"
                       "-->\n"
                       "<config>\n"
                       "<prop id=\"smpi/simulate-computation\" value=\"0\"></prop>\n"
                       "<prop id=\"smpi/host-speed\" value=\"1f\"></prop>\n"
                       "</config>\n\n")

        AS_head = "<AS id=\"AS0\" routing=\"Floyd\">\n"

        return head + config_clause + AS_head


def issueTail():
	return "</AS>\n</platform>\n"

def issueLink1(x):
	return "  <link id=\"link-"+str(x)+"\" latency=\""+str(link_latency)+"\" bandwidth=\""+str(link_bandwidth)+link_bandwidth_unit+"\"/>\n"

def issueLink2(x,y):
	return "  <link id=\"link-"+str(x)+"-"+str(y)+"\" latency=\""+str(link_latency)+"\" bandwidth=\""+str(link_bandwidth)+link_bandwidth_unit+"\"/>\n"

def issueLink3(x,y,bw):
	return "  <link id=\"link-"+str(x)+"-"+str(y)+"\" latency=\""+str(link_latency)+"\" bandwidth=\""+str(bw)+link_bandwidth_unit+"\"/>\n"

def issueHost(index):
	return "  <host id=\"host-"+str(index)+".hawaii.edu\" speed=\"10Gf\"/>\n"

def issueRouteHead(index1, index2):
	return "  <route src=\"host-"+str(index1)+".hawaii.edu\" dst=\"host-"+str(index2)+".hawaii.edu\">\n"
def issueRouteTail():
	return "  </route>\n"

def issueRouteLink1(x):
	return "\t<link_ctn id=\"link-"+str(x)+"\"/>\n"

def issueRouteLink2(x,y):
	return "\t<link_ctn id=\"link-"+str(x)+"-"+str(y)+"\"/>\n"

######################################################################
# Parse command-line arguments
if (len(sys.argv) != 2):
	sys.stderr.write("Usage: "+sys.argv[0]+" <num hosts>\n")
	sys.stderr.write("  Will generate a ring_<num hosts>.xml and hostfile_<num hosts>.txt file\n")
	exit(1)

num_hosts = int(sys.argv[1])

###############################################################
# Generate RING XML file
filename = "./ring_"+str(num_hosts)+".xml"
fh = open(filename, 'w')
fh.write(issueHead())

# Create hosts
for i in range(0,num_hosts):
	fh.write(issueHost(i))

# Create links
for i in range(0,num_hosts):
	fh.write(issueLink1(i))

## Create one-hop routes
for i in range (0,num_hosts):
	src = i
	dst = i+1
	if (dst == num_hosts):
		dst = 0;
	fh.write(issueRouteHead(src,dst))
	fh.write(issueRouteLink1(src))
	fh.write(issueRouteTail())

fh.write(issueTail())
fh.close()
sys.stderr.write("Ring XML platform file created: "+filename+"\n")

###############################################################
## Generate host file
filename = "./hostfile_"+str(num_hosts)+".txt"
fh = open(filename, 'w')

for i in range(0,num_hosts):
	fh.write("host-"+str(i)+".hawaii.edu\n")

fh.close()
sys.stderr.write("Hostfile created: "+filename+"\n")

