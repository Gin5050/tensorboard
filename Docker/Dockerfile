FROM nvcr.io/nvidia/pytorch:19.08-py3
RUN apt-get clean && apt-get update

RUN pip install pillow scikit-image tensorboard tensorboardx matplotlib tensorflow future torch torchvision --ignore-installed
RUN pip install wrapt==1.10.0 --ignore-installed

WORKDIR /workspace/work

CMD /bin/bash