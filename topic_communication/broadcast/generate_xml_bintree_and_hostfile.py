#!/usr/bin/env python2.7
import sys
import os
import math

# Link parameters
link_latency = "10us"
link_bandwidth = 10
link_bandwidth_unit = "Gbps"


# Convenient math wrappers
def floor(x):
	return int(math.floor(x))
def ceil(x):
	return int(math.ceil(x))
def pow2(x):
	return int(math.pow(2,x))

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
                       "<prop id=\"smpi/host-speed\" value=\"1\"></prop>\n"
                       "</config>\n\n")

        AS_head = "<zone id=\"AS0\" routing=\"Floyd\">\n"

        return head + config_clause + AS_head


def issueTail():
	return "</zone>\n</platform>\n"

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
	print >> sys.stderr, "Usage:a"+sys.argv[0]+" <num hosts>\n"
        print >> sys.stderr, "  Will generate a bintree_<num hosts>.xml and hostfile_<num hosts>.txt file\n"
	exit(1)

num_hosts = int(sys.argv[1])


###############################################################
# Generate Binary Tree XML file

filename = "./bintree_"+str(num_hosts)+".xml"
fh = open(filename, 'w')
fh.write(issueHead())

# Create all hosts and links
for i in range(0,num_hosts):
	fh.write(issueHost(i))
	if (i*2+1 < num_hosts):
  		fh.write(issueLink2(i,i*2+1))
	if (i*2+2 < num_hosts):
  		fh.write(issueLink2(i,i*2+2))

# Create all routes
for i in range(0,num_hosts):
	level_i = floor(math.log(1+i,2))
	left_child = 2*i+1
	right_child = 2*i+2
	if (left_child < num_hosts):
		fh.write(issueRouteHead(i, left_child))
		fh.write(issueRouteLink2(i,left_child))
		fh.write(issueRouteTail())
	if (right_child < num_hosts):
		fh.write(issueRouteHead(i, right_child))
		fh.write(issueRouteLink2(i,right_child))
		fh.write(issueRouteTail())

fh.write(issueTail())
fh.close()
print >> sys.stderr, "BinTree XML platform description file created: "+filename

###############################################################
## Generate host file
filename = "./hostfile_"+str(num_hosts)+".txt"
fh = open(filename, 'w')

for i in range(0,num_hosts):
	fh.write("host-"+str(i)+".hawaii.edu\n")

fh.close()
print >> sys.stderr, "Hostfile created: "+filename

