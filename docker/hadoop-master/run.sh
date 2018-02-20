#!/bin/bash

namedir=/hadoop/dfs/name
if [ ! -d $namedir ]; then
  echo "Namenode name directory not found: $namedir"
  exit 2
fi

if [ -z "$CLUSTER_NAME" ]; then
  echo "Cluster name not specified"
  exit 2
fi

[ "$(ls -A $namedir)" ] && echo "Not Empty" || echo 'Y' | $HADOOP_PREFIX/bin/hdfs --config $HADOOP_CONF_DIR namenode -format $CLUSTER_NAME 

#service sshd start
$HADOOP_PREFIX/bin/hdfs --config $HADOOP_CONF_DIR namenode &
$HADOOP_PREFIX/bin/yarn --config $HADOOP_CONF_DIR resourcemanager &
$HADOOP_PREFIX/bin/yarn --config $HADOOP_CONF_DIR historyserver



