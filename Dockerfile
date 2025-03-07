FROM mlupin/docker-lambda:python3.9-build

LABEL maintainer="mehabawyohanse@gmail.com"

WORKDIR /var/task

# Fancy prompt to remind you are in zappashell
RUN echo 'export PS1="\[\e[36m\]zappashell>\[\e[m\] "' >> /root/.bashrc

# Create and Activate the virtual environment 
RUN echo 'virtualenv -p python3 ./ve >/dev/null' >> /root/.bashrc
RUN echo 'source ./ve/bin/activate >/dev/null' >> /root/.bashrc

# Additional RUN commands here
# RUN yum clean all && \
#    yum -y install <stuff>

CMD ["bash"]