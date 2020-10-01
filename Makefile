VERSION=$(shell python3 -c "from configparser import ConfigParser; p = ConfigParser(); p.read('setup.cfg'); print(p['metadata']['version'])")

default:
	@echo "\"make publish\"?"

tag:
	# Make sure we're on the main branch
	@if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "main" ]; then exit 1; fi
	curl -H "Authorization: token `cat $(HOME)/.github-access-token`" -d '{"tag_name": "v$(VERSION)"}' https://api.github.com/repos/nschloe/stacktags/releases

upload: clean
	@if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "main" ]; then exit 1; fi
	# https://stackoverflow.com/a/58756491/353337
	python3 -m pep517.build --source --binary .
	twine upload dist/*

publish: upload tag

clean:
	@find . | grep -E "(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf
	@rm -rf *.egg-info/ build/ dist/ MANIFEST .pytest_cache/

format:
	isort .
	black .

lint:
	black --check .
	flake8 .

DATE = $(shell date +%Y-%m-%d)
update:
	@if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "main" ]; then exit 1; fi
	git checkout -b data-update-$(DATE)
	python3 data/update.py
	git commit -a -m "data update $(DATE)"
	git push --set-upstream origin data-update-$(DATE)
	python3 data/plot.py
	svgo *.svg
	rm -rf tmp/
	mkdir tmp/
	mv *.svg tmp/
	git checkout gh-pages
	mv tmp/* .
	git commit -a -m "plots update"
	git push
	git checkout data-update-$(DATE)
