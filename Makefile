.PHONY: build_files clean_files

build_files:
	python3.8 setup_cython.py build_ext --inplace
# python3.8 setup_cython.py build_ext -j 4 --inplace
# -j sets the number of threads to use while multiprocessing (default: 4)

run_main:
	python3.8 -W ignore Main_Script.py

install_dependencies:
	pip3.8 install numpy matplotlib scipy imutils opencv-python cython

clean_files:
	-rm -r build/
	-rm *.so