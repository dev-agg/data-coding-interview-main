root_abspath := $(realpath -s $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

docker_image:
	docker build -f ${root_abspath}/docker/Dockerfile -t data-coding-env ${root_abspath}/src

docker_sh: docker_image
	docker run -it \
		-v ${root_abspath}:/opt/spark/apps \
		-e PYTHONPATH=/opt/spark/apps/src \
		-w /opt/spark/apps \
		data-coding-env \
		bash

lint: docker_image
	docker run -it \
		-v ${root_abspath}:/opt/spark/apps \
		-e PYTHONPATH=/opt/spark/apps/src \
		-w /opt/spark/apps \
		data-coding-env \
		flake8 && mypy
