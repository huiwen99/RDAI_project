export HOSTSRC=/home/khuiwen/Documents/GitLab/RDAI_project
export WORKSPACE=$HOME/Workspace 

docker run --gpus all --rm -it -w $WORKSPACE -v $HOSTSRC:$WORKSPACE --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 -p 5002:5002 \
    rdai_project:v1.0