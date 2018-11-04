SERVICE=sandbox

.PHONY: run
run: stop
	docker-compose up --build -d --remove-orphans

.PHONY: stop
stop:
	docker-compose stop
	docker-compose rm -f

.PHONY: test
test: codegen
	docker-compose run --rm ${SERVICE} \
		nosetests -v --nologcapture /usr/src/app/tests
	docker-compose run --rm ${SERVICE} \
		flake8 /usr/src/appswagger_codegen --max-line-length=100

.PHONY: codegen
codegen: run
	./tools/generate_models.sh

clean:
	docker-compose config --services | xargs docker rm -f
