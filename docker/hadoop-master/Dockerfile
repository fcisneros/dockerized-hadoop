FROM dockerized/base

RUN mkdir -p /hadoop/dfs/name
VOLUME /hadoop/dfs/name

RUN mkdir -p /hadoop/yarn/timeline
VOLUME /hadoop/yarn/timeline

ADD run.sh /run.sh
RUN chmod a+x /run.sh

# namenode
EXPOSE 50070
# resourcemanager
EXPOSE 8088
# historyserver
EXPOSE 8188

CMD ["/run.sh"]