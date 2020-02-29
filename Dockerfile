FROM 119.3.170.97:5000/ubuntu
MAINTAINER lsp 1593073434@qq.com

ADD . /usr/src/
VOLUME /usr/src
WORKDIR /usr/src
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
CMD ./run.sh