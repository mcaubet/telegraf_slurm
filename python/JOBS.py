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

        if len(jobs) > 0:

            BOOT_FAIL = a.find('job_state', "BOOT_FAIL")
            CANCELLED = a.find('job_state', "CANCELLED")
            COMPLETED = a.find('job_state', "COMPLETED")
            CONFIGURING = a.find('job_state', "CONFIGURING")
            COMPLETING = a.find('job_state', "COMPLETING")
            DEADLINE = a.find('job_state', "DEADLINE")
            FAILED = a.find('job_state', "FAILED")
            NODE_FAIL = a.find('job_state', "NODE_FAIL")
            OUT_OF_MEMORY = a.find('job_state', "OUT_OF_MEMORY")
            PENDING = a.find('job_state', "PENDING")
            PREEMPTED = a.find('job_state', "PREEMPTED")
            RUNNING = a.find('job_state', "RUNNING")
            RESV_DEL_HOLD = a.find('job_state', "RESV_DEL_HOLD")
            REQUEUE_FED = a.find('job_state', "REQUEUE_FED")
            REQUEUE_HOLD = a.find('job_state', "REQUEUE_HOLD")
            REQUEUED = a.find('job_state', "REQUEUED")
            RESIZING = a.find('job_state', "RESIZING")
            REVOKED = a.find('job_state', "REVOKED")
            SIGNALING = a.find('job_state', "SIGNALING")
            SPECIAL_EXIT = a.find('job_state', "SPECIAL_EXIT")
            STAGE_OUT = a.find('job_state', "STAGE_OUT")
            STOPPED = a.find('job_state', "STOPPED")
            SUSPENDED = a.find('job_state', "SUSPENDED")
            TIMEOUT = a.find('job_state', "TIMEOUT")

            queue_status = "boot_fail={0},cancelled={1},completed={2},configuring={3},completing={4},deadline={5},failed={6},node_fail={7},oom={8},pending={9},preempted={10},running={11},resv_del_hold={12},requeue_fed={13},requeue_hold={14},requeued={15},resizing={16},revoked={17},signaling={18},special_exit={19},stage_out={20},stopped={21},suspended={22},timeout={23}".format(len(BOOT_FAIL),len(CANCELLED),len(COMPLETED),len(CONFIGURING),len(COMPLETING),len(DEADLINE),len(FAILED),len(NODE_FAIL),len(OUT_OF_MEMORY),len(PENDING),len(PREEMPTED),len(RUNNING),len(RESV_DEL_HOLD),len(REQUEUE_FED),len(REQUEUE_HOLD),len(REQUEUED),len(RESIZING),len(REVOKED),len(SIGNALING),len(SPECIAL_EXIT),len(STAGE_OUT),len(STOPPED),len(SUSPENDED),len(TIMEOUT))
            
            print("SQueue,hostname={0} {1}".format(socket.gethostname(),queue_status))

        else:
            print("No jobs found !")
    except ValueError as e:
        print("Job query failed - {0}".format(e.args[0]))
