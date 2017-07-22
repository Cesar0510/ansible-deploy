#
# Ansible for Django
# Cesar H. <caherdenez@gmai.com>
#

.PHONY: default clean


default:
	@echo $(ENV_NAME)' build script'
	@echo
	@echo 'usage: make <target>'
	@echo

clean:
	@echo 'cleaning up temporary files'
	find . -name '*.pyc' -type f -exec rm {} ';'
	find . -name '__pycache__' -type d -print | xargs rm -rf
