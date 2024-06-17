# Data Coding Interview

This repo contains the assets for the Data team's coding interview questions. It is shared with candidates prior to their scheduled interview.

**Candidates**

Please follow the instructions in this document to prepare for your coding interview.

## Setting Up Docker Environment

It is highly advisable that the candidate setup the docker environment prior to their interview. Otherwise, valuable interview time may be wasted on setting up the docker environment.

### Install Docker

You will require a docker system installed on the workstation you will be using for the interview.

If you do not already have docker installed, please see the [docker install documentation](https://docs.docker.com/engine/install/) for your operating system.

### Building Docker Image

Ensure that you have the [make](https://www.gnu.org/software/make/) tools installed on your workstation.

The [Makefile](Makefile) contains targets that can be used to build the image for this [Dockerfile](docker/Dockerfile) by running:

```bash
make docker_image
```

#### Bash

If the docker image has been successfully built, you can now start the docker container and connect to it through a [bash](https://opensource.com/resources/what-bash) terminal with this target:

```bash
make docker_sh
```

## Coding Interview Question

Your coding interview question will be based on one of the subfolders under the [src](src/) directory.

The email you received regarding the technical assessment interview should have included which subfolder you have been assigned to. Go to this subfolder and familiarize yourself with the source code. It is not necessary to review any of the other `src` subfolders.

The detailed coding interview requirements will be provided during your interview.

#### Running Pytest

We use the [tox](https://tox.wiki/en/4.13.0/) automation tool to manage environments for running [Pytest](https://docs.pytest.org/) unit tests.

From the docker bash terminal, change directory to the subfolder under `src` that you have been assigned. For example:

```bash
cd src/stories_metadata
```

Then to run the pytest unit tests contained under this subfolder:

```bash
tox
```

Review the output. The output will indicate if the tests succeeded or not.
