all: check package clear

check: linting static-analysis security-analysis

linting:
	# stage: analysis
	pylint blueprint

static-analysis:
	# stage: analysis
	bandit -r blueprint

security-analysis:
	# stage: analysis
	safety check --full-report

requirements:
	# for container env.
	pipenv lock -r > requirements.txt

package:
	python setup.py sdist bdist_wheel
	ls dist

clear:
	rm -rf dist build CDKBlueprint.egg-info
