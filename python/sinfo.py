#!/usr/bin/env /usr/local/conda/envs/slurm/bin/python

import pyslurm
import socket
import re

def get_sinfo(node_dict):
    for nodeid in node_dict:
        nodename = node_dict[nodeid]["name"]
        state = node_dict[nodeid]["state"]
        alloc_cpus = node_dict[nodeid]["alloc_cpus"]
        alloc_mem = node_dict[nodeid]["alloc_mem"]
        boot_time = node_dict[nodeid]["boot_time"]
        cores = node_dict[nodeid]["cores"]
        cores_per_socket = node_dict[nodeid]["cores_per_socket"]
        cpu_load = node_dict[nodeid]["cpu_load"]
        cpus = node_dict[nodeid]["cpus"]
        err_cpus = node_dict[nodeid]["err_cpus"]
        free_mem = node_dict[nodeid]["free_mem"]
        mem_spec_limit = node_dict[nodeid]["mem_spec_limit"]
        node_hostname = node_dict[nodeid]["node_hostname"]
        partitions = ';'.join(node_dict[nodeid]["partitions"])
        real_memory = node_dict[nodeid]["real_memory"]
        slurmd_start_time = node_dict[nodeid]["slurmd_start_time"]
        sockets = node_dict[nodeid]["sockets"]
        threads = node_dict[nodeid]["threads"]
        tmp_disk = node_dict[nodeid]["tmp_disk"]
        weight = node_dict[nodeid]["weight"]
        print("slurm,metric=nodes,hostname={},nodename={},partitions={} state=\"{}\",alloc_cpus={},alloc_mem={},boot_time={},cores={},cores_per_socket={},cpu_load={},cpus={},err_cpus={},free_mem={},mem_spec_limit={},node_hostname=\"{}\",real_memory={},slurmd_start_time={},sockets={},threads={},tmp_disk={},weight={}".format(socket.gethostname(),nodename,partitions,state,alloc_cpus,alloc_mem,boot_time,cores,cores_per_socket,cpu_load,cpus,err_cpus,free_mem,mem_spec_limit,node_hostname,real_memory,slurmd_start_time,sockets,threads,tmp_disk,weight))

if __name__ == "__main__":

    try:
        rnode = pyslurm.node()
        nodes = rnode.get()
        
        if len(nodes) > 0:
            get_sinfo(nodes)
        else:
            print("No Nodes found !")
    
    except ValueError as enode:
        print("Error - {0}".format(enode.args[0]))
