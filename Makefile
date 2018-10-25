.PHONY: test
test: codegen
	cd ./src && export PYTHONPATH=`pwd` && python -m unittest -b -v
	cd ./src && export PYTHONPATH=`pwd` && flake8 swagger_codegen --max-line-length=100

.PHONY: codegen
codegen: run
	./tools/generate_models.sh

.PHONY: run
run: stop
	docker-compose up -d --remove-orphans

.PHONY: stop
stop:
	docker-compose stop
	docker-compose rm -f
