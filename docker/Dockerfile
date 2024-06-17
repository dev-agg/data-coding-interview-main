FROM amazoncorretto:8 as builder

RUN yum -y update
RUN yum -y groupinstall development
RUN yum -y install openssl openssl-devel
RUN yum -y install python3-devel

FROM builder as apache-spark

# Install Python dependencies
RUN pip3 install tox flake8 mypy

ENV PATH="${PATH}:/opt/spark/apps/scripts"

CMD ["bash"]
