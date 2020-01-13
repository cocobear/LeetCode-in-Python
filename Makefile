
venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv -p python3 --no-site-packages venv
	venv/bin/pip install -Ur requirements.txt
	touch venv/bin/activate

test: venv
	venv/bin/py.test  solutions

coverage: venv
	venv/bin/py.test --cov-config .coveragerc --verbose --cov-report term --cov-report html --cov=datastruct datastruct
