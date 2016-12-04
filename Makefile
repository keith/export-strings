.PHONY: test

clean:
	find . -name "*.pyc" -exec rm "{}" \;
	rm -rf tmp

test: clean
	python -m unittest discover -s test
