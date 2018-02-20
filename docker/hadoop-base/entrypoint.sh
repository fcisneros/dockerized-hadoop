#!/bin/bash

function addProperty() {
  local path=$1
  local name=$2
  local value=$3

  local entry="<property><name>${name}</name><value>${value}</value></property>"
  local escapedEntry="$(echo $entry | sed 's/\//\\\//g')"
  sed -i "/<\/configuration>/ s/.*/${escapedEntry}\n&/" $path
}

# fs.defaultFS
export FS_DEFAULTFS=${FS_DEFAULTFS:-master}

# yarn.timeline-service.hostname
export HISTORYSERVER_HOSTNAME="${HISTORYSERVER_HOSTNAME:-master}"

# yarn.resourcemanager.hostname
export RESOURCEMANAGER_HOSTNAME="${RESOURCEMANAGER_HOSTNAME:-master}"


# CORE
addProperty /etc/hadoop/core-site.xml fs.defaultFS hdfs://${FS_DEFAULTFS}:8020
addProperty /etc/hadoop/core-site.xml hadoop.http.staticuser.user root

# HDFS
addProperty /etc/hadoop/hdfs-site.xml dfs.namenode.rpc-bind-host 0.0.0.0
addProperty /etc/hadoop/hdfs-site.xml dfs.namenode.servicerpc-bind-host 0.0.0.0
addProperty /etc/hadoop/hdfs-site.xml dfs.namenode.http-bind-host 0.0.0.0
addProperty /etc/hadoop/hdfs-site.xml dfs.namenode.https-bind-host 0.0.0.0
addProperty /etc/hadoop/hdfs-site.xml dfs.client.use.datanode.hostname true
addProperty /etc/hadoop/hdfs-site.xml dfs.datanode.use.datanode.hostname true
addProperty /etc/hadoop/hdfs-site.xml dfs.namenode.name.dir file:///hadoop/dfs/name
addProperty /etc/hadoop/hdfs-site.xml dfs.webhdfs.enabled true
addProperty /etc/hadoop/hdfs-site.xml dfs.permissions.enabled false
addProperty /etc/hadoop/hdfs-site.xml dfs.datanode.data.dir file:///hadoop/dfs/data

# YARN
addProperty /etc/hadoop/yarn-site.xml yarn.resourcemanager.bind-host 0.0.0.0
addProperty /etc/hadoop/yarn-site.xml yarn.nodemanager.bind-host 0.0.0.0
addProperty /etc/hadoop/yarn-site.xml yarn.nodemanager.bind-host 0.0.0.0
addProperty /etc/hadoop/yarn-site.xml yarn.timeline-service.bind-host 0.0.0.0
addProperty /etc/hadoop/yarn-site.xml yarn.timeline-service.leveldb-timeline-store.path /hadoop/yarn/timeline
addProperty /etc/hadoop/yarn-site.xml yarn.timeline-service.hostname ${HISTORYSERVER_HOSTNAME}
addProperty /etc/hadoop/yarn-site.xml yarn.timeline-service.enabled true
addProperty /etc/hadoop/yarn-site.xml yarn.timeline-service.generic-application-history.enabled true
addProperty /etc/hadoop/yarn-site.xml yarn.log.server.url http://${HISTORYSERVER_HOSTNAME}:8188/applicationhistory/logs/
addProperty /etc/hadoop/yarn-site.xml yarn.resourcemanager.recovery.enabled true
addProperty /etc/hadoop/yarn-site.xml yarn.resourcemanager.store.class org.apache.hadoop.yarn.server.resourcemanager.recovery.FileSystemRMStateStore
addProperty /etc/hadoop/yarn-site.xml yarn.resourcemanager.fs.state-store.uri /rmstate
addProperty /etc/hadoop/yarn-site.xml yarn.resourcemanager.system-metrics-publisher.enabled true
addProperty /etc/hadoop/yarn-site.xml yarn.resourcemanager.hostname ${RESOURCEMANAGER_HOSTNAME}
addProperty /etc/hadoop/yarn-site.xml yarn.resourcemanager.address ${RESOURCEMANAGER_HOSTNAME}:8032
addProperty /etc/hadoop/yarn-site.xml yarn.resourcemanager.scheduler.address ${RESOURCEMANAGER_HOSTNAME}:8030
addProperty /etc/hadoop/yarn-site.xml yarn.resourcemanager.resource-tracker.address ${RESOURCEMANAGER_HOSTNAME}:8031
addProperty /etc/hadoop/yarn-site.xml yarn.nodemanager.remote-app-log-dir /app-logs
addProperty /etc/hadoop/yarn-site.xml yarn.nodemanager.aux-services mapreduce_shuffle


# MAPRED
addProperty /etc/hadoop/mapred-site.xml yarn.nodemanager.bind-host 0.0.0.0
addProperty /etc/hadoop/mapred-site.xml mapreduce.framework.name yarn
addProperty /etc/hadoop/mapred-site.xml mapreduce.jobhistory.address ${HISTORYSERVER_HOSTNAME}:10020


exec $@
