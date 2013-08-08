SHELL := /bin/bash
PYTHON := python
PIP := pip
PACKAGE_DIR := $(shell python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())";)
LIB_DIR := lib

LIBS += flask
LIBS += werkzeug

deps: deploy_deps dev_deps

deploy_deps:
	$(PIP) install -Ur requirements.txt
	link_libs

link_libs:
	mkdir -p $(LIB_DIR)
	find $(LIB_DIR) -mindepth 1 -delete
	@$(foreach lib,$(LIBS), ln -s -F -h  $(PACKAGE_DIR)/$(lib) $(LIB_DIR)/;)

dev_deps:
	$(PIP) install -Ur requirements_dev.txt

clean:
	find . -name "*.py[co]" -delete

test_unit_py: nosetests

test_integrations_py:
	nosetests --logging-level=ERROR -a slow --with-coverage --cover-package=calc

test: clean test_integrations_py

unit: test_unit_py

