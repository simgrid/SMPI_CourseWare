#!/usr/bin/env python2.7
import sys
import os
import math

# Link parameters
link_latency = "20us"
link_bandwidth = 10
link_bandwidth_unit = "Gbps"

# XML generation functions
def issueHead():
	return "<?xml version='1.0'?>\n<!DOCTYPE platform SYSTEM \"http://simgrid.gforge.inria.fr/simgrid.dtd\">\n<platform version=\"3\">\n<AS id=\"AS0\" routing=\"Full\">\n"

def issueTail():
	return "</AS>\n</platform>\n"

def issueLink1(x):
	return "  <link id=\"link-"+str(x)+"\" latency=\""+str(link_latency)+"\" bandwidth=\""+str(link_bandwidth)+link_bandwidth_unit+"\"/>\n"

def issueLink2(x,y):
	return "  <link id=\"link-"+str(x)+"-"+str(y)+"\" latency=\""+str(link_latency)+"\" bandwidth=\""+str(link_bandwidth)+link_bandwidth_unit+"\"/>\n"

def issueLink3(x,y,bw):
	return "  <link id=\"link-"+str(x)+"-"+str(y)+"\" latency=\""+str(link_latency)+"\" bandwidth=\""+str(bw)+link_bandwidth_unit+"\"/>\n"

def issueHost(index):
	return "  <host id=\"host-"+str(index)+".hawaii.edu\" power=\"1\"/>\n"

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
	print >> sys.stderr, "  Will generate a ring_<num hosts>.xml and hostfile_<num hosts>.txt file\n"
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

# Create routes
for i in range (0,num_hosts):
	for j in range(i+1,num_hosts):
		fh.write(issueRouteHead(i,j))
		for k in range(i,(j+num_hosts)%num_hosts):
  			fh.write(issueRouteLink1(k))
    		fh.write(issueRouteTail())

fh.write(issueTail())
fh.close()
print >> sys.stderr, "Ring XML platform file created: "+filename

###############################################################
## Generate host file
filename = "./hostfile_"+str(num_hosts)+".txt"
fh = open(filename, 'w')

for i in range(0,num_hosts):
	fh.write("host-"+str(i)+".hawaii.edu\n")

fh.close()
print >> sys.stderr, "Hostfile created: "+filename

