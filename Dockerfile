# Adapted from: http://lefakkomies.github.io/pynomo-doc/installation/installation.html#python-3-docker-installation

FROM python:3.7-slim-buster

RUN apt-get update             \
 && apt-get install -y         \
    python3                    \
    python3-pip                \
    texlive-latex-base         \
    texlive-fonts-recommended

RUN DEBIAN_FRONTEND=noninteractive pip3 install pyx pynomo numpy scipy six

WORKDIR /nomo
CMD ["bash"]

# to build this, run:
#
#   $ docker build -t pynomo .
#
# to use it, run (on linux):
#
#   $ docker run --rm -v "$PWD":/nomo pynomo python3 frodo-meds.py
#
# that should create frodo-meds.pdf in the current directory
