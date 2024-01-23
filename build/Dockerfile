FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu20.04

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1


ENV TZ=Asia/Singapore
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ARG DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata python3-tk

RUN apt-get -y update
RUN apt -y update

RUN apt-get install -y \
    software-properties-common \
    build-essential \
    checkinstall \
    cmake \
    pkg-config \
    yasm \
    git \
    vim \
    curl \
    wget \
    gfortran \
    libjpeg8-dev \
    libpng-dev \
    libtiff5-dev \
    libtiff-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libdc1394-22-dev \
    libxine2-dev \
    sudo \
    apt-transport-https \
    libcanberra-gtk-module \
    libcanberra-gtk3-module \
    dbus-x11 \
    vlc \
    iputils-ping \
    python3-dev \
    python3-pip

RUN apt-get clean && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && apt-get -y autoremove

RUN rm -rf /var/cache/apt/archives/

RUN python3 -m pip install --no-cache-dir --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN pip3 install "uvicorn[standard]"

ARG UID
ARG GID
RUN addgroup --gid $GID user
RUN adduser --disabled-password --gecos '' --uid $UID --gid $GID user
USER user

WORKDIR /workspace