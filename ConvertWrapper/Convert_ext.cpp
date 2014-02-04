/***************************************************************************
 Convert_ext.cpp  -  description
 -------------------
 copyright            : (C) 2014 Valentina Fioretti
 email                : fioretti@iasfbo.inaf.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software for non commercial purpose              *
 *   and for public research institutes; you can redistribute it and/or    *
 *   modify it under the terms of the GNU General Public License.          *
 *   For commercial purpose see appropriate license terms                  *
 *                                                                         *
 ***************************************************************************/

#include <boost/python/module.hpp>
#include <boost/python/def.hpp>


namespace { // Avoid cluttering the global namespace.

   // Conversion from int to unsigned short
  unsigned short int convert(int value) { return (unsigned short) value; }
}

namespace python = boost::python;

// Python requires an exported function called init<module-name> in every
// extension module. This is where we build the module contents.
BOOST_PYTHON_MODULE(Convert_ext)
{
   // Add regular functions to the module.
   python::def("convert", convert);
}
