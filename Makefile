install:
	pip install --upgrade pip
	pip install -r requirements.txt

hello: chapter1/hello.py
	python3 chapter1/hello.py

test: chapter1/test_hello.py
	pytest chapter1/test_hello.py