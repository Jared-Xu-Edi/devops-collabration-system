FROM python:3.7-stretch

ENV AZURE_CLI_VERSION 2.19.1-1~stretch

ENV ANSIBLE_PYTHON_INTERPRETER /usr/local/bin/python

ENV BUILD_PACKAGES \
    bash \
    nano \
    curl \
    tar \
    openssh-client \
    sshpass \
    git \
    python3-dateutil \
    python3-httplib2 \
    python3-jinja2 \
    python3-paramiko \
    python3-pip \
    python3-yaml \
    ca-certificates \
    python3-dev \
    libpq-dev \
    musl-dev \
    gcc \
    build-essential \
    make \
    musl-dev \
    libffi-dev \
    libssl-dev \
    apt-transport-https \
    lsb-release \
    vim \
    gnupg

RUN set -x && \
    echo "==> Upgrading system..."  && \
    apt-get update && apt-get upgrade -y && \
    echo "==> Adding system packages..."  && \
    apt-get install -y ${BUILD_PACKAGES} && \
    echo "==> Adding azure-cli repository..." && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" > /etc/apt/sources.list.d/azure-cli.list && \
    apt-get update && \
    echo "==> Adding system packages..."  && \
    cat packages.txt | xargs apt-get install -y && \
    echo "==> Cleaning up..."  && \
    apt-get clean && apt-get autoclean && rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/* && \
    rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin

RUN curl -sL https://packages.microsoft.com/keys/microsoft.asc | \
    gpg --dearmor | \
    tee /etc/apt/trusted.gpg.d/microsoft.asc.gpg > /dev/null

RUN set -x && \
    echo "==> Adding Some Required libraries"  && \
    pip install cryptography>=2.3 openshift jq --trusted-host pypi.org --trusted-host files.pythonhosted.org --default-timeout=200

ADD requirements.txt ./

RUN set -x && \
    echo "==> Adding python libs"  && \
    pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org && \
    pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org --default-timeout=200