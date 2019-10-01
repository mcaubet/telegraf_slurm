#!/usr/bin/env python

import pyslurm
import sys
import subprocess
import socket

from time import gmtime, strftime, sleep

if __name__ == "__main__":

    try:
        a = pyslurm.job()
        jobs = a.get()

        RUNNING_CPUS = 0
        PENDING_CPUS = 0
        BOOT_FAIL_CPUS = 0
        CANCELLED_CPUS = 0
        COMPLETED_CPUS = 0
        CONFIGURING_CPUS = 0
        COMPLETING_CPUS = 0
        DEADLINE_CPUS = 0
        FAILED_CPUS = 0
        NODE_FAIL_CPUS = 0
        OUT_OF_MEMORY_CPUS = 0
        PREEMPTED_CPUS = 0
        RESV_DEL_HOLD_CPUS = 0
        REQUEUE_FED_CPUS = 0
        REQUEUE_HOLD_CPUS = 0
        REQUEUED_CPUS = 0
        RESIZING_CPUS = 0
        REVOKED_CPUS = 0
        SIGNALING_CPUS = 0
        SPECIAL_EXIT_CPUS = 0
        STAGE_OUT_CPUS = 0
        STOPPED_CPUS = 0
        SUSPENDED_CPUS = 0
        TIMEOUT_CPUS = 0
        # Node States
        RUNNING_NODES = 0
        PENDING_NODES = 0
        BOOT_FAIL_NODES = 0
        CANCELLED_NODES = 0
        COMPLETED_NODES = 0
        CONFIGURING_NODES = 0
        COMPLETING_NODES = 0
        DEADLINE_NODES = 0
        FAILED_NODES = 0
        NODE_FAIL_NODES = 0
        OUT_OF_MEMORY_NODES = 0
        PREEMPTED_NODES = 0
        RESV_DEL_HOLD_NODES = 0
        REQUEUE_FED_NODES = 0
        REQUEUE_HOLD_NODES = 0
        REQUEUED_NODES = 0
        RESIZING_NODES = 0
        REVOKED_NODES = 0
        SIGNALING_NODES = 0
        SPECIAL_EXIT_NODES = 0
        STAGE_OUT_NODES = 0
        STOPPED_NODES = 0
        SUSPENDED_NODES = 0
        TIMEOUT_NODES = 0
        # Job states
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

        if len(jobs) > 0:
            for jobid in jobs:
                if jobs[jobid]["job_state"] == "PENDING":
                    PENDING = PENDING + 1
                    PENDING_CPUS = PENDING_CPUS + jobs[jobid]["num_cpus"]
                    PENDING_NODES = PENDING_NODES + jobs[jobid]["num_nodes"]
    
                if jobs[jobid]["job_state"] == "RUNNING":
                    RUNNING = RUNNING + 1
                    RUNNING_CPUS = RUNNING_CPUS + jobs[jobid]["num_cpus"]
                    RUNNING_NODES = RUNNING_NODES + jobs[jobid]["num_nodes"]

                if jobs[jobid]["job_state"] == "BOOT_FAIL":
                    BOOT_FAIL = BOOT_FAIL + 1
                    BOOT_FAIL_CPUS = BOOT_FAIL_CPUS + jobs[jobid]["num_cpus"]
                    BOOT_FAIL_NODES = BOOT_FAIL_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "CANCELLED":
                    CANCELLED = CANCELLED + 1
                    CANCELLED_CPUS = CANCELLED_CPUS + jobs[jobid]["num_cpus"]
                    CANCELLED_NODES = CANCELLED_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "COMPLETED":
                    COMPLETED = COMPLETED + 1
                    COMPLETED_CPUS = COMPLETED_CPUS + jobs[jobid]["num_cpus"]
                    COMPLETED_NODES = COMPLETED_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "CONFIGURING":
                    CONFIGURING = CONFIGURING + 1
                    CONFIGURING_CPUS = CONFIGURING_CPUS + jobs[jobid]["num_cpus"]
                    CONFIGURING_NODES = CONFIGURING_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "COMPLETING":
                    COMPLETING = COMPLETING + 1
                    COMPLETING_CPUS = COMPLETING_CPUS + jobs[jobid]["num_cpus"]
                    COMPLETING_NODES = COMPLETING_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "DEADLINE":
                    DEADLINE = DEADLINE + 1
                    DEADLINE_CPUS = DEADLINE_CPUS + jobs[jobid]["num_cpus"]
                    DEADLINE_NODES = DEADLINE_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "FAILED":
                    FAILED = FAILED + 1
                    FAILED_CPUS = FAILED_CPUS + jobs[jobid]["num_cpus"]
                    FAILED_NODES = FAILED_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "NODE_FAIL":
                    NODE_FAIL = NODE_FAIL + 1
                    NODE_FAIL_CPUS = NODE_FAIL_CPUS + jobs[jobid]["num_cpus"]
                    NODE_FAIL_NODES = NODE_FAIL_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "OUT_OF_MEMORY":
                    OUT_OF_MEMORY = OUT_OF_MEMORY + 1
                    OUT_OF_MEMORY_CPUS = OUT_OF_MEMORY_CPUS + jobs[jobid]["num_cpus"]
                    OUT_OF_MEMORY_NODES = OUT_OF_MEMORY_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "PREEMPTED":
                    PREEMPTED = PREEMPTED + 1
                    PREEMPTED_CPUS = PREEMPTED_CPUS + jobs[jobid]["num_cpus"]
                    PREEMPTED_NODES = PREEMPTED_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "RESV_DEL_HOLD":
                    RESV_DEL_HOLD = RESV_DEL_HOLD + 1
                    RESV_DEL_HOLD_CPUS = RESV_DEL_HOLD_CPUS + jobs[jobid]["num_cpus"]
                    RESV_DEL_HOLD_NODES = RESV_DEL_HOLD_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "REQUEUE_FED":
                    REQUEUE_FED = REQUEUE_FED + 1
                    REQUEUE_FED_CPUS = REQUEUE_FED_CPUS + jobs[jobid]["num_cpus"]
                    REQUEUE_FED_NODES = REQUEUE_FED_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "REQUEUE_HOLD":
                    REQUEUE_HOLD = REQUEUE_HOLD + 1
                    REQUEUE_HOLD_CPUS = REQUEUE_HOLD_CPUS + jobs[jobid]["num_cpus"]
                    REQUEUE_HOLD_NODES = REQUEUE_HOLD_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "REQUEUED":
                    REQUEUED = REQUEUED + 1
                    REQUEUED_CPUS = REQUEUED_CPUS + jobs[jobid]["num_cpus"]
                    REQUEUED_NODES = REQUEUED_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "RESIZING":
                    RESIZING = RESIZING + 1
                    RESIZING_CPUS = RESIZING_CPUS + jobs[jobid]["num_cpus"]
                    RESIZING_NODES = RESIZING_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "REVOKED":
                    REVOKED = REVOKED + 1
                    REVOKED_CPUS = REVOKED_CPUS + jobs[jobid]["num_cpus"]
                    REVOKED_NODES = REVOKED_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "SIGNALING":
                    SIGNALING = SIGNALING + 1
                    SIGNALING_CPUS = SIGNALING_CPUS + jobs[jobid]["num_cpus"]
                    SIGNALING_NODES = SIGNALING_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "SPECIAL_EXIT":
                    SPECIAL_EXIT = SPECIAL_EXIT + 1
                    SPECIAL_EXIT_CPUS = SPECIAL_EXIT_CPUS + jobs[jobid]["num_cpus"]
                    SPECIAL_EXIT_NODES = SPECIAL_EXIT_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "STAGE_OUT":
                    STAGE_OUT = STAGE_OUT + 1
                    STAGE_OUT_CPUS = STAGE_OUT_CPUS + jobs[jobid]["num_cpus"]
                    STAGE_OUT_NODES = STAGE_OUT_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "STOPPED":
                    STOPPED = STOPPED + 1
                    STOPPED_CPUS = STOPPED_CPUS + jobs[jobid]["num_cpus"]
                    STOPPED_NODES = STOPPED_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "SUSPENDED":
                    SUSPENDED = SUSPENDED + 1
                    SUSPENDED_CPUS = SUSPENDED_CPUS + jobs[jobid]["num_cpus"]
                    SUSPENDED_NODES = SUSPENDED_NODES + jobs[jobid]["num_nodes"]
                
                if jobs[jobid]["job_state"] == "TIMEOUT":
                    TIMEOUT = TIMEOUT + 1
                    TIMEOUT_CPUS = TIMEOUT_CPUS + jobs[jobid]["num_cpus"]
                    TIMEOUT_NODES = TIMEOUT_NODES + jobs[jobid]["num_nodes"]

            num_jobs = "boot_fail_jobs={0},cancelled_jobs={1},completed_jobs={2},configuring_jobs={3},completing_jobs={4},deadline_jobs={5},failed_jobs={6},node_fail_jobs={7},oom_jobs={8},pending_jobs={9},preempted_jobs={10},running_jobs={11},resv_del_hold_jobs={12},requeue_fed_jobs={13},requeue_hold_jobs={14},requeued_jobs={15},resizing_jobs={16},revoked_jobs={17},signaling_jobs={18},special_exit_jobs={19},stage_out_jobs={20},stopped_jobs={21},suspended_jobs={22},timeout_jobs={23}".format(BOOT_FAIL,CANCELLED,COMPLETED,CONFIGURING,COMPLETING,DEADLINE,FAILED,NODE_FAIL,OUT_OF_MEMORY,PENDING,PREEMPTED,RUNNING,RESV_DEL_HOLD,REQUEUE_FED,REQUEUE_HOLD,REQUEUED,RESIZING,REVOKED,SIGNALING,SPECIAL_EXIT,STAGE_OUT,STOPPED,SUSPENDED,TIMEOUT)

            num_cpus = "boot_fail_cpus={0},cancelled_cpus={1},completed_cpus={2},configuring_cpus={3},completing_cpus={4},deadline_cpus={5},failed_cpus={6},node_fail_cpus={7},oom_cpus={8},pending_cpus={9},preempted_cpus={10},running_cpus={11},resv_del_hold_cpus={12},requeue_fed_cpus={13},requeue_hold_cpus={14},requeued_cpus={15},resizing_cpus={16},revoked_cpus={17},signaling_cpus={18},special_exit_cpus={19},stage_out_cpus={20},stopped_cpus={21},suspended_cpus={22},timeout_cpus={23}".format(BOOT_FAIL_CPUS,CANCELLED_CPUS,COMPLETED_CPUS,CONFIGURING_CPUS,COMPLETING_CPUS,DEADLINE_CPUS,FAILED_CPUS,NODE_FAIL_CPUS,OUT_OF_MEMORY_CPUS,PENDING_CPUS,PREEMPTED_CPUS,RUNNING_CPUS,RESV_DEL_HOLD_CPUS,REQUEUE_FED_CPUS,REQUEUE_HOLD_CPUS,REQUEUED_CPUS,RESIZING_CPUS,REVOKED_CPUS,SIGNALING_CPUS,SPECIAL_EXIT_CPUS,STAGE_OUT_CPUS,STOPPED_CPUS,SUSPENDED_CPUS,TIMEOUT_CPUS)

            num_nodes = "boot_fail_nodes={0},cancelled_nodes={1},completed_nodes={2},configuring_nodes={3},completing_nodes={4},deadline_nodes={5},failed_nodes={6},node_fail_nodes={7},oom_nodes={8},pending_nodes={9},preempted_nodes={10},running_nodes={11},resv_del_hold_nodes={12},requeue_fed_nodes={13},requeue_hold_nodes={14},requeued_nodes={15},resizing_nodes={16},revoked_nodes={17},signaling_nodes={18},special_exit_nodes={19},stage_out_nodes={20},stopped_nodes={21},suspended_nodes={22},timeout_nodes={23}".format(BOOT_FAIL_NODES,CANCELLED_NODES,COMPLETED_NODES,CONFIGURING_NODES,COMPLETING_NODES,DEADLINE_NODES,FAILED_NODES,NODE_FAIL_NODES,OUT_OF_MEMORY_NODES,PENDING_NODES,PREEMPTED_NODES,RUNNING_NODES,RESV_DEL_HOLD_NODES,REQUEUE_FED_NODES,REQUEUE_HOLD_NODES,REQUEUED_NODES,RESIZING_NODES,REVOKED_NODES,SIGNALING_NODES,SPECIAL_EXIT_NODES,STAGE_OUT_NODES,STOPPED_NODES,SUSPENDED_NODES,TIMEOUT_NODES)

            print("SQueue,hostname={0} {1},{2},{3}".format(socket.gethostname(),num_jobs,num_cpus,num_nodes))

        else:
            print("No jobs found !")
    except ValueError as e:
        print("Job query failed - {0}".format(e.args[0]))
