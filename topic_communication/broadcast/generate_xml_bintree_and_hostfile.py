#!/usr/bin/env python2.7
import sys
import os
import math

# Link parameters
link_latency = "20us"
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
	for j in range(i+1,num_hosts):
		fh.write(issueRouteHead(j,i))
		# Host j is at the same of lower level than host i
		level_j = floor(math.log(1+j,2))
		current_host_path_j = j
		# Go up to the same level of that of host i
		for l in range(level_j,level_i,-1):
			parent_host = floor(float(current_host_path_j-1)/2)
			fh.write(issueRouteLink2(min(current_host_path_j,parent_host),max(current_host_path_j,parent_host)))
			current_host_path_j = parent_host
		# Find the common ancestor
		current_host_path_i = i
		while (current_host_path_j != current_host_path_i):
			fh.write(issueRouteLink2(min(current_host_path_j,floor(float(current_host_path_j-1)/2)), max(current_host_path_j,floor(float(current_host_path_j-1)/2))))
			current_host_path_i = floor(float(current_host_path_i-1)/2)
			current_host_path_j = floor(float(current_host_path_j-1)/2)
		common_ancestor = current_host_path_j
		# Go back from i to the common ancestor
		current_host_path_i = i
		sequence = []
		sequence.append(current_host_path_i)
		while (current_host_path_i != common_ancestor):
			parent_host = floor(float(current_host_path_i-1)/2)
			sequence.append(parent_host)
			current_host_path_i = parent_host
		# Issue links in the common ancestor -> i order
		sequence = sequence[::-1]
		for k in range(0,len(sequence)-1):
			fh.write(issueRouteLink2(min(sequence[k],sequence[k+1]),max(sequence[k],sequence[k+1])))
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

