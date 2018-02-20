FROM dockerized/base

RUN mkdir -p /hadoop/dfs/data
VOLUME /hadoop/dfs/data

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 50075
EXPOSE 50010
EXPOSE 8042

CMD ["/run.sh"]
