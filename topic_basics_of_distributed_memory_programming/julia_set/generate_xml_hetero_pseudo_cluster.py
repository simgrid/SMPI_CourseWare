#!/usr/bin/env python2.7
import sys
import os
import math
import random

# Link parameters
link_latency = "10us"
link_bandwidth = 100
link_bandwidth_unit = "Gbps"

# XML generation functions
def issueHead():
        head = ("<?xml version='1.0'?>\n"
                "<!DOCTYPE platform SYSTEM \"http://simgrid.gforge.inria.fr/simgrid/simgrid.dtd\">\n"
                "<platform version=\"4.1\">\n\n")

        config_clause = (
                       "<config>\n"
                       #"<prop id=\"smpi/simulate-computation\" value=\"0\"></prop>\n"
                       "<prop id=\"smpi/host-speed\" value=\"200Gf\"></prop>\n"
                       "</config>\n\n")

        AS_head = "<AS id=\"AS0\" routing=\"Floyd\">\n"

        return head + config_clause + AS_head


def issueTail():
	return "</AS>\n</platform>\n"

def issueLink():
	return "  <link id=\"link\" latency=\""+str(link_latency)+"\" bandwidth=\""+str(link_bandwidth)+link_bandwidth_unit+"\"/>\n"

def issueHost(index):
    if index == 0:
        speed = 210
    else:
        speed = 199 + random.randint(0,10)/10.0
    return "  <host id=\"host-"+str(index)+".hawaii.edu\" speed=\"" + str(speed) + "Gf\"/>\n"

def issueRouteHead(index1, index2):
	return "  <route src=\"host-"+str(index1)+".hawaii.edu\" dst=\"host-"+str(index2)+".hawaii.edu\">\n"
def issueRouteTail():
	return "  </route>\n"

def issueRouteLink():
	return "\t<link_ctn id=\"link\"/>\n"

######################################################################
# Parse command-line arguments
if (len(sys.argv) != 2):
	print >> sys.stderr, "Usage:a"+sys.argv[0]+" <num hosts>\n"
	print >> sys.stderr, "  Will generate a cluster_<num hosts>.xml and hostfile_<num hosts>.txt file\n"
	exit(1)

num_hosts = int(sys.argv[1])

###############################################################
# Generate XML file
filename = "./cluster_"+str(num_hosts)+".xml"
fh = open(filename, 'w')
fh.write(issueHead())

# Create hosts
for i in range(0,num_hosts):
	fh.write(issueHost(i))

# Create link
fh.write(issueLink())

## Create all one-hop routes
for src in range (0,num_hosts):
    for dst in range (src+1,num_hosts):
	    fh.write(issueRouteHead(src,dst))
	    fh.write(issueRouteLink())
	    fh.write(issueRouteTail())

fh.write(issueTail())
fh.close()
print >> sys.stderr, "Cluster XML platform file created: "+filename

###############################################################
## Generate host file
filename = "./hostfile_"+str(num_hosts)+".txt"
fh = open(filename, 'w')

for i in range(0,num_hosts):
	fh.write("host-"+str(i)+".hawaii.edu\n")

fh.close()
print >> sys.stderr, "Hostfile created: "+filename

