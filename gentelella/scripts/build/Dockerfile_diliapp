FROM ubuntu:latest
MAINTAINER tommy "dalianlxw@163.com"

#ENV diliedu_dir  /var/www/diliapp/
#ENV temp_dir /var/www/diliapp/gentelella/

RUN sed -i -e 's/archive.ubuntu.com/mirrors.aliyun.com/g'  /etc/apt/sources.list

RUN apt-get update \
    && apt-get  install -y  python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3  python \
    && pip3  install --upgrade pip 

RUN apt-get install  python3-mysqldb

#RUN cd ${diliedu_dir} \
#    pip3 install -r requirements.txt 

#RUN cd ${temp_dir} \
#    python ./manage.py  runserver &


ENTRYPOINT ["python3"]

