#!/usr/bin/env python

import pyslurm
import socket

# import sys
# from time import gmtime, strftime, sleep

def get_squeue(job_dict,partition,key=None):
    
    RUNNING = 0
    PENDING = 0
    BOOT_FAIL = 0
    CANCELLED = 0
    COMPLETED = 0
    CONFIGURING = 0
    COMPLETING = 0
    DEADLINE = 0
    FAILED = 0
    NODE_FAIL = 0
    OUT_OF_MEMORY = 0
    PREEMPTED = 0
    RESV_DEL_HOLD = 0
    REQUEUE_FED = 0
    REQUEUE_HOLD = 0
    REQUEUED = 0
    RESIZING = 0
    REVOKED = 0
    SIGNALING = 0
    SPECIAL_EXIT = 0
    STAGE_OUT = 0
    STOPPED = 0
    SUSPENDED = 0
    TIMEOUT = 0

    for jobid in job_dict:
        if partition in job_dict[jobid]["partition"]:
            if job_dict[jobid]["job_state"] == "PENDING":
                PENDING = PENDING + (1 if key == None else job_dict[jobid][key])
    
            if job_dict[jobid]["job_state"] == "RUNNING":
                RUNNING = RUNNING + (1 if key == None else job_dict[jobid][key])
    
            if job_dict[jobid]["job_state"] == "BOOT_FAIL":
                BOOT_FAIL = BOOT_FAIL + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "CANCELLED":
                CANCELLED = CANCELLED + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "COMPLETED":
                COMPLETED = COMPLETED + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "CONFIGURING":
                CONFIGURING = CONFIGURING + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "COMPLETING":
                COMPLETING = COMPLETING + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "DEADLINE":
                DEADLINE = DEADLINE + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "FAILED":
                FAILED = FAILED + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "NODE_FAIL":
                NODE_FAIL = NODE_FAIL + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "OUT_OF_MEMORY":
                OUT_OF_MEMORY = OUT_OF_MEMORY + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "PREEMPTED":
                PREEMPTED = PREEMPTED + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "RESV_DEL_HOLD":
                RESV_DEL_HOLD = RESV_DEL_HOLD + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "REQUEUE_FED":
                REQUEUE_FED = REQUEUE_FED + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "REQUEUE_HOLD":
                REQUEUE_HOLD = REQUEUE_HOLD + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "REQUEUED":
                REQUEUED = REQUEUED + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "RESIZING":
                RESIZING = RESIZING + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "REVOKED":
                REVOKED = REVOKED + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "SIGNALING":
                SIGNALING = SIGNALING + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "SPECIAL_EXIT":
                SPECIAL_EXIT = SPECIAL_EXIT + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "STAGE_OUT":
                STAGE_OUT = STAGE_OUT + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "STOPPED":
                STOPPED = STOPPED + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "SUSPENDED":
                SUSPENDED = SUSPENDED + (1 if key == None else job_dict[jobid][key])
            
            if job_dict[jobid]["job_state"] == "TIMEOUT":
                TIMEOUT = TIMEOUT + (1 if key == None else job_dict[jobid][key])

    return "boot_fail={0},cancelled={1},completed={2},configuring={3},completing={4},deadline={5},failed={6},node_fail={7},oom={8},pending={9},preempted={10},running={11},resv_del_hold={12},requeue_fed={13},requeue_hold={14},requeued={15},resizing={16},revoked={17},signaling={18},special_exit={19},stage_out={20},stopped={21},suspended={22},timeout={23}".format(BOOT_FAIL,CANCELLED,COMPLETED,CONFIGURING,COMPLETING,DEADLINE,FAILED,NODE_FAIL,OUT_OF_MEMORY,PENDING,PREEMPTED,RUNNING,RESV_DEL_HOLD,REQUEUE_FED,REQUEUE_HOLD,REQUEUED,RESIZING,REVOKED,SIGNALING,SPECIAL_EXIT,STAGE_OUT,STOPPED,SUSPENDED,TIMEOUT)

if __name__ == "__main__":

    try:
        rpartition = pyslurm.partition()
        partitions = rpartition.get()

        if len(partitions) > 0:

            try:
                for partition in partitions:
                    rjob = pyslurm.job()
                    jobs = rjob.get()
                    if len(jobs) > 0:
                        num_jobs = get_squeue(jobs,partition)
                        num_cpus = get_squeue(jobs,partition,'num_cpus')
                        print("SQueue,metric=num_jobs,hostname={0},partition={1} {2}".format(socket.gethostname(),partition,num_jobs))
                        print("SQueue,metric=num_cpus,hostname={0},partition={1} {2}".format(socket.gethostname(),partition,num_cpus))
                    else:
                        print("No jobs found !")
        
            except ValueError as ejob:
                print("Job query failed - {0}".format(ejob.args[0]))
        else:
            print("No Partitions found !")
    except ValueError as epart:
        print("Partition query failed - {0}".format(epart.args[0]))

