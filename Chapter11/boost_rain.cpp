#include <boost/python.hpp>

double sum_rain(boost::python::list rain, int len) {

  double sum = 0.;

  for (int i = 0; i < len; i++){
    int val = boost::python::extract<int>(rain[i]);
    if(val == -1) {
       sum += 0.025;
    } else {
      sum += 0.1 * val;
    }
  }

  return sum;
}

BOOST_PYTHON_MODULE(librain) {
    using namespace boost::python;

    def("sum_rain", sum_rain);
}

