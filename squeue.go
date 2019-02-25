/*  
    squeue.go is a Slurm plugin for Telegraf. This is fully inspired by the 
    Prometheus Slurm Plugin developed by Victor Penso and Matteo Dessalvi:
      https://github.com/vpenso/prometheus-slurm-exporter
    
    Copyright (C) 2019 Marc Caubet Serrabou, Victor Penso, Matteo Dessalvi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/
package main

import (
  "fmt"
  /*  "github.com/influxdata/telegraf"
      "github.com/influxdata/telegraf/plugins/inputs"*/
  "io/ioutil"
  "log"
  "os"
  "os/exec"
  "strings"
)

type SQueueMetrics struct {
  boot_fail     uint32
  cancelled     uint32
  completed     uint32
  configuring   uint32
  completing    uint32
  deadline      uint32
  failed        uint32
  node_fail     uint32
  oom           uint32
  pending       uint32
  preempted     uint32
  running       uint32
  resv_del_hold uint32
  requeue_fed   uint32
  requeue_hold  uint32
  requeued      uint32
  resizing      uint32
  revoked       uint32
  signaling     uint32
  special_exit  uint32
  stage_out     uint32
  stopped       uint32
  suspended     uint32
  timeout       uint32
}

func SQueueGetMetrics() *SQueueMetrics {
  return ParseSQueueMetrics(SQueueData())
}

func ParseSQueueMetrics(squeue []byte) *SQueueMetrics {
  var sq SQueueMetrics
  lines := strings.Split(string(squeue), "\n")
  for _, line := range lines {
    if strings.Contains(line, ",") {
      splitted := strings.Split(line, ",")
      state := splitted[1]
      switch state {
        case "BOOT_FAIL":
          sq.boot_fail++
        case "CANCELLED":
          sq.cancelled++
        case "COMPLETED":
          sq.completed++
        case "CONFIGURING":
          sq.configuring++
        case "COMPLETING":
          sq.completing++
        case "DEADLINE":
          sq.deadline++
        case "FAILED":
          sq.failed++
        case "NODE_FAIL":
          sq.node_fail++
        case "OUT_OF_MEMORY":
          sq.oom++
        case "PENDING":
          sq.pending++
        case "PREEMPTED":
          sq.preempted++
        case "RUNNING":
          sq.running++
        case "RESV_DEL_HOLD":
          sq.resv_del_hold++
        case "REQUEUE_FED":
          sq.requeue_fed++
        case "REQUEUE_HOLD":
          sq.requeue_hold++
        case "REQUEUED":
          sq.requeued++
        case "RESIZING":
          sq.resizing++
        case "REVOKED":
          sq.revoked++
        case "SIGNALING":
          sq.signaling++
        case "SPECIAL_EXIT":
          sq.special_exit++
        case "STAGE_OUT":
          sq.stage_out++
        case "STOPPED":
          sq.stopped++
        case "SUSPENDED":
          sq.suspended++
        case "TIMEOUT":
          sq.timeout++
      }
    }
  }
  return &sq
}

// Execute the squeue command and return its output
func SQueueData() []byte {
  cmd := exec.Command("/usr/bin/squeue", "-h", "-o %A,%T,%a,%u,%g,%c", "--states=all")
  stdout, err := cmd.StdoutPipe()
  if err != nil {
    log.Fatal(err)
  }
  if err := cmd.Start(); err != nil {
    log.Fatalf("cmd.Start() failed with %s\n", err)
  }
  out, _ := ioutil.ReadAll(stdout)
  if err := cmd.Wait(); err != nil {
    log.Fatalf("cmd.Wait() failed with %s\n", err)
  }
  return out
}

func Hostname() string {
  hostname, error := os.Hostname()
  if error != nil {
    panic(error)
  }
  return hostname
}

func main() {
  sq := SQueueGetMetrics()

  hostname := Hostname()

  fmt.Printf("SQueue,host=%s boot_fail=%d,cancelled=%d,completed=%d,configuring=%d,completing=%d,deadline=%d,failed=%d,node_fail=%d,oom=%d,pending=%d,preempted=%d,running=%d,resv_del_hold=%d,requeue_fed=%d,requeue_hold=%d,requeued=%d,resizing=%d,revoked=%d,signaling=%d,special_exit=%d,stage_out=%d,stopped=%d,suspended=%d,timeout=%d\n", hostname, sq.boot_fail, sq.cancelled, sq.completed, sq.configuring, sq.completing, sq.deadline, sq.failed, sq.node_fail, sq.oom, sq.pending, sq.preempted, sq.running, sq.resv_del_hold, sq.requeue_fed, sq.requeue_hold, sq.requeued, sq.resizing, sq.revoked, sq.signaling, sq.special_exit, sq.stage_out, sq.stopped, sq.suspended, sq.timeout)

}

/*
func (q *SQueueMetrics) Description() string {
  return "Return Slurm SQueue information"
}

func (q *SQueueMetrics) Gather(acc telegraf.Accumulator) error {

  fields := make(map[string]interface{})

  fields["pending"] = q.pending
  fields["running"] = q.running
  fields["suspended"] = q.suspended
  fields["cancelled"] = q.cancelled
  fields["completing"] = q.completing
  fields["completed"] = q.completed
  fields["configuring"] = q.configuring
  fields["failed"] = q.failed
  fields["timeout"] = q.timeout
  fields["preempted"] = q.preempted
  fields["node_fail"] = q.node_fail

  tags := make(map[string]string)

  acc.AddFields("SlurmSQueue", fields, tags)

  return nil
}

func init() {
  sq := SQueueGetMetrics()
  fmt.Printf("1: %v\n", sq)
  inputs.Add("SlurmSqueue", func() telegraf.Input { return q })
}
*/
