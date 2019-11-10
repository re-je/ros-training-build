# ROS-I Training Build

Build tools for the [re.je](https://re.je) ROS-I training.

> **NOTE:** This repo is a WIP

## Usage - Bare Metal

Install `ansible` and `git`

    sudo apt update
    sudo apt install -y ansible git

Clone this repo:

    git clone https://github.com/re-je/ros-training-build.git
    cd ros-training-build

Run the bare metal playbooks.

    sudo ansible-playbook -i localhost bootstrap-ubuntu.yml
    sudo ansible-playbook -i localhost playbook.yml --skip-tags=chroot

Remove any networks used during install:

    nmcli --fields UUID con show | tail -n+2 | while read line; do nmcli con delete uuid  $line; done

## Usage - Container

These commands use the
[ansible-bender](https://github.com/ansible-community/ansible-bender) project
and need the
[requirements](https://github.com/ansible-community/ansible-bender#requirements-host)
of that project.

    pip3 install --user ansible ansible-bender
    ansible-bender build container.yml

### Run one-off

The container will be removed when closed.

    podman run --rm \
        --interactive --tty \
        --security-opt label=disable \
        --network host \
        -v /etc/localtime:/etc/localtime:ro \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        --hostname re-je-tmp --add-host re-je-tmp:127.0.0.1 \
        --env DISPLAY=$DISPLAY \
        --volume /dev/dri:/dev/dri \
        localhost/ros:melodic-training-bionic

### Persistent

Create a persistent container

    podman create \
        --interactive --tty \
        --security-opt label=disable \
        --name reje-ros \
        --network host \
        -v /etc/localtime:/etc/localtime:ro \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        --hostname re-je --add-host re-je:127.0.0.1 \
        --env DISPLAY=$DISPLAY \
        --volume /dev/dri:/dev/dri \
        localhost/ros:melodic-training-bionic

Start the persistent container

    podman start reje-ros

## Usage - Chroot Minimal base image

Set up mirrors:

```
cat <<EOF > /etc/apt/sources.list
deb http://gb.archive.ubuntu.com/ubuntu/ bionic main restricted universe multiverse 
deb-src http://gb.archive.ubuntu.com/ubuntu/ bionic main restricted universe multiverse 

deb http://gb.archive.ubuntu.com/ubuntu/ bionic-security main restricted universe multiverse 
deb-src http://gb.archive.ubuntu.com/ubuntu/ bionic-security main restricted universe multiverse 

deb http://gb.archive.ubuntu.com/ubuntu/ bionic-updates main restricted universe multiverse 
deb-src http://gb.archive.ubuntu.com/ubuntu/ bionic-updates main restricted universe multiverse    
EOF
```

Run the setup ansible and run chroot role:

    apt update
    apt install -y ansible git
    git clone https://github.com/re-je/ros-training-build.git
    cd ros-training-build/
    ansible-playbook -i localhost bootstrap-ubuntu.yml
    ansible-playbook -i localhost chroot.yml
    cd ..
    rm -rf ros-training-build/

## Attribution

This EP has received funding from the European Union’s Horizon 2020 research and
innovation programme under the project [ROSIN](http://rosin-project.eu/) with
the grant agreement No 732287.
