FROM snakemake/snakemake
RUN mkdir /mnt/data
RUN pip3 install xlrd openpyxl scipy
RUN apt-get update
RUN apt-get -y install -qq cron

COPY scripts/* /usr/local/bin/
COPY start-snake-cron /etc/cron.d/start-snake-cron

RUN chmod 0644 /etc/cron.d/start-snake-cron
RUN crontab /etc/cron.d/start-snake-cron
RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
