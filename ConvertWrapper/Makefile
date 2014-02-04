PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /opt/local/Library/Frameworks/Python.framework/Versions/2.7/include/python$(PYTHON_VERSION)
PYTHON_LIB = /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python$(PYTHON_VERSION)/config/
 
# location of the Boost Python include files and library
 
BOOST_INC = /opt/local/include/boost/python
BOOST_LIB = /opt/local/lib

# Boost Python library keyword (for Macports Boost installation use -lboost_python-mt)
BOOST_PYTHON_LIB = -lboost_python-mt


# compile mesh classes

.PHONY: all
all: Convert_ext.so

Convert_ext.so: Convert_ext.o
	g++ -shared Convert_ext.o -L$(BOOST_LIB) $(BOOST_PYTHON_LIB) -L$(PYTHON_LIB) -lpython$(PYTHON_VERSION) -o Convert_ext.so
 
Convert_ext.o:Convert_ext.cpp
	g++ -I$(PYTHON_INCLUDE) -I$(BOOST_INC) -fPIC -c Convert_ext.cpp

clean:

	@- $(RM) Convert_ext.o Convert_ext.so
	
distclean: clean
