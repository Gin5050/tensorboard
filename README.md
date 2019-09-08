# tensorboard
learning tensorboard

## memo

```
docker run --runtime=nvidia -it -v /home/yuki/work/tensorboard:/workspace/work -p 8888:8888 -p 6006:6006 tensorboardx
```

```
jupyter notebook --port=8080 --ip=0.0.0.0 --no-browser --allow-root
```

```
tensorboard --logdir=./logs
```