install: #for linux ubuntu
	sudo apt update
	sudo apt install software-properties-common
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt install python3.7
	python3.7 --version
	$(MAKE) run

run:
	python main.py

test:
	python test.py