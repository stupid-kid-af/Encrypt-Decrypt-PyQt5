FROM python:3.8
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /usr/src/app

RUN adduser --quiet --disabled-password qtuser && usermod -a -G audio qtuser
ENV LIBGL_ALWAYS_INDIRECT=1
ENV T_X11_NO_MITSHM=1
VOLUME  /tmp/.X11-unix:/tmp/.X11-unix:rw
ENV DISPLAY=$DISPLAY
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 python3-pyqt5 -y
RUN apt install libgl1-mesa-glx
RUN  rm -rf /var/lib/apt/lists/*
ENV QT_DEBUG_PLUGINS=1
RUN pip install pycryptodome cipher pyqt5
RUN mkdir ui
COPY application.py .
COPY cipher.py .
COPY /images/ .
COPY /ui/ ui

CMD ["python3", "./application.py"]
