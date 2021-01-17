HOST=127.0.0.1
PACKAGE:=afitop100
TEST_PATH=./$(PACKAGE)/tests/

.PHONY : clean

.DEFAULT_GOAL = help
help:
	@echo "--------------------HELP-----------------------"
	@echo "To test the project type make test"
	@echo "To clean the build files type make clean-build"
	@echo "-----------------------------------------------"

clean:
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '*.pyo' -exec rm -rf {} +

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

test: clean
	/usr/local/bin/python3 -m unittest discover -v -s $(TEST_PATH) -p 'test_*.py'
