double sum_rain(int* rain, int len) {

  double sum = 0.;

  for (int i = 0; i < len; i++){
    if(rain[i] == -1) {
       sum += 0.025;
    } else {
      sum += 0.1 * rain[i];
    }
  }

  return sum;
}
