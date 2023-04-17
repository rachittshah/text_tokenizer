clean:
	rm -rf ./build ./dist ./*.egg-info **/*.whl ./html

build: clean install
	python3 setup.py sdist bdist_wheel --dist-dir ./token_count


package: build
	mv ./src/*.whl ./

install:
	pip3 install -r ./requirements.txt


