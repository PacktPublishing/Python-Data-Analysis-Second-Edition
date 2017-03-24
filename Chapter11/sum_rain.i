%module sum_rain

%{
  #define SWIG_FILE_WITH_INIT
  #include "sum_rain.h"
%}

%include "/tmp/numpy.i"

%init %{
  import_array();
%}

%apply (int* IN_ARRAY1, int DIM1) {(int* rain, int len)};

%include "sum_rain.h"
