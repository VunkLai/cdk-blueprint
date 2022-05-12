all: check package clear

linting:
	# stage: analysis
	pylint blueprint

static-analysis:
	# stage: analysis
	bandit -r blueprint

security-analysis:
	# stage: analysis
	safety check --full-report
	# for container env.
	pipenv lock -r > requirements.txt

check: linting static-analysis security-analysis
	# stage: linting static-analysis security-analysis

package:
	python setup.py sdist bdist_wheel
	ls dist

clear:
	rm -rf dist build CDKBlueprint.egg-info
