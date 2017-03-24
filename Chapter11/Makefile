CC = g++
PYLIBPATH = $(shell python3-config --exec-prefix)/lib
LIB = -L$(PYLIBPATH) $(shell python3-config --libs) -L/usr/local/Cellar/boost/1.63.0/lib -L/usr/local/Cellar/boost-python/1.63.0/lib -lboost_python3
OPTS = $(shell python3-config --include) -O2 -I/usr/local/Cellar/boost/1.63.0/include

default: librain.so
	@python3 ./rain_demo.py

librain.so: rain.o
	$(CC) $(LIB)  -Wl,-rpath,$(PYLIBPATH) -shared $< -o $@

rain.o: boost_rain.cpp Makefile
	$(CC) $(OPTS) -c $< -o $@

clean:
	rm -rf *.so *.o

.PHONY: default clean
