#!/usr/bin/env python

import pyslurm
import socket

def get_sinfo(node_dict,partition):

    IDLE = 0
    ALLOCATED = 0
    MIXED = 0
    DRAINED = 0
    DRAINING = 0
    DOWN = 0
    FAIL = 0
    UNKNOWN = 0
    COMPLETING = 0
    MAINT = 0
    RESERVED = 0
    POWER_DOWN = 0
    POWER_UP = 0
    FUTURE = 0
    NO_RESPOND = 0
    NPC = 0
    PERFCTRS = 0
    
    for nodeid in node_dict:
        if partition in node_dict[nodeid]["partitions"]:
            if node_dict[nodeid]["state"] == "IDLE":
                IDLE = IDLE + 1
            if node_dict[nodeid]["state"] == "ALLOCATED":
                ALLOCATED = ALLOCATED + 1
            if node_dict[nodeid]["state"] == "MIXED":
                MIXED = MIXED + 1
            if node_dict[nodeid]["state"] == "DRAINED":
                DRAINED = DRAINED + 1
            if node_dict[nodeid]["state"] == "IDLE+DRAIN":
                DRAINED = DRAINED + 1
            if node_dict[nodeid]["state"] == "DRAINING":
                DRAINING = DRAINING + 1
            if node_dict[nodeid]["state"] == "MIXED+DRAIN":
                DRAINING = DRAINING + 1
            if node_dict[nodeid]["state"] == "ALLOCATED+DRAIN":
                DRAINING = DRAINING + 1
            if node_dict[nodeid]["state"] == "DOWN":
                DOWN = DOWN + 1
            if node_dict[nodeid]["state"] == "FAIL":
                FAIL = FAIL + 1
            if node_dict[nodeid]["state"] == "UNKNOWN":
                UNKNOWN = UNKNOWN + 1
            if node_dict[nodeid]["state"] == "COMPLETING":
                COMPLETING = COMPLETING + 1
            if node_dict[nodeid]["state"] == "MAINT":
                MAINT = MAINT + 1
            if node_dict[nodeid]["state"] == "RESERVED":
                RESERVED = RESERVED + 1
            if node_dict[nodeid]["state"] == "POWER_DOWN":
                POWER_DOWN = POWER_DOWN + 1
            if node_dict[nodeid]["state"] == "POWER_UP":
                POWER_UP = POWER_UP + 1
            if node_dict[nodeid]["state"] == "NO_RESPOND":
                NO_RESPOND = NO_RESPOND + 1
            if node_dict[nodeid]["state"] == "FUTURE":
                FUTURE = FUTURE + 1
            if node_dict[nodeid]["state"] == "NPC":
                NPC = NPC + 1
            if node_dict[nodeid]["state"] == "PERFCTRS":
                PERFCTRS = PERFCTRS + 1

    return "idle={0},allocated={1},mixed={2},drained={3},draining={4},down={5},fail={6},unknown={7},completing={8},maintenance={9},reserved={10},power_down={11},power_up={12},no_respond={13},future={14},npc={15},perfctrs={16}".format(IDLE,ALLOCATED,MIXED,DRAINED,DRAINING,DOWN,FAIL,UNKNOWN,COMPLETING,MAINT,RESERVED,POWER_DOWN,POWER_UP,NO_RESPOND,FUTURE,NPC,PERFCTRS)

if __name__ == "__main__":

    try: 
        rpartition = pyslurm.partition()
        partitions = rpartition.get()
        
        if len(partitions) > 0:

            try:
                for partition in partitions:
                    rnode = pyslurm.node()
                    nodes = rnode.get()
    
                    if len(nodes) > 0:
                        nodes = get_sinfo(nodes,partition)
                        print("SQueue,metric=nodes,hostname={0},partition={1} {2}".format(socket.gethostname(),partition,nodes))
                    else:
                        print("No Nodes found !")
    
            except ValueError as enode:
                print("Error - {0}".format(enode.args[0]))
        else:
            print("No Partitions found !")
    except ValueError as epart:
        print("Error - {0}".format(epart.args[0]))
