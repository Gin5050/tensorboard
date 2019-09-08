FROM nvcr.io/nvidia/pytorch:19.08-py3

# 各環境変数を設定
ENV USER tester
ENV HOME /home/${USER}
ENV SHELL /bin/bash

# 一般ユーザーアカウントを追加
RUN useradd -m ${USER}
# 一般ユーザーにsudo権限を付与
RUN gpasswd -a ${USER} sudo
# 一般ユーザーのパスワード設定
RUN echo "${USER}:test_pass" | chpasswd
# ログインシェルを指定
#sed -i.bak -e "s/${HOME}:/${HOME}:${SHELL}" /etc/passwd

RUN apt-get clean && apt-get update

RUN pip install pillow scikit-image tensorboard tensorboardx matplotlib tensorflow future torch torchvision --ignore-installed
RUN pip install wrapt==1.10.0 --ignore-installed

WORKDIR /workspace/work

CMD /bin/bash