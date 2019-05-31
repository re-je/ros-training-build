# ROS-I Training Build

Build tools for the [re.je](https://re.je) ROS-I training.

> **NOTE:** This repo is a WIP

## Usage - General

Clone this repo:

    git clone https://github.com/re-je/ros-training-build.git

## Usage - Bare Metal

Install `ansible` and `git`

    sudo apt update
    sudo apt install -y ansible git

Run the bare metal playbooks.

    sudo ansible-playbook -i localhost bootstrap-ubuntu.yml
    sudo ansible-playbook -i localhost playbook.yml

## Usage - Container

These commands use the
[ansible-bender](https://github.com/ansible-community/ansible-bender) project
and need the
[requirements](https://github.com/ansible-community/ansible-bender#requirements-host)
of that project.

    pip3 install --user ansible ansible-bender
    ansible-bender build container.yml

### Enable connections to xorg

> **NOTE:** Adjusting the permissions to the X server host is not the safest and
> will be replaced in this documentation shortly

    xhost +local:root

After the container has been closed run.

    xhost -local:root

### Run one-off

The container will be removed when closed.

    podman run --rm \
        --interactive --tty \
        --privileged \
        --network host \
        --hostname re-je-tmp --add-host re-je-tmp:127.0.0.1 \
        --env DISPLAY=$DISPLAY \
        --volume /dev/dri:/dev/dri \
        localhost/ros:melodic-training-bionic

### Persistent

Create a persistent container

    podman create \
        --interactive --tty \
        --privileged \
        --name reje-ros \
        --network host \
        --hostname re-je --add-host re-je:127.0.0.1 \
        --env DISPLAY=$DISPLAY \
        --volume /dev/dri:/dev/dri \
        localhost/ros:melodic-training-bionic

Start the persistent container

    podman start reje-ros

## Attribution

This EP has received funding from the European Union’s Horizon 2020 research and
innovation programme under the project [ROSIN](http://rosin-project.eu/) with
the grant agreement No 732287.
