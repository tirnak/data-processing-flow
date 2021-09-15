FROM snakemake/snakemake
RUN mkdir /mnt/data
RUN pip3 install xlrd openpyxl scipy
COPY scripts/* /usr/local/bin/
