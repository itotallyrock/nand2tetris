
load Or8Way.hdl,
output-file Or8Way.out,
compare-to Or8Way.cmp,
output-list in%B3.8.3 out%B3.1.3;

// Used these four test cases because it there were 256 possibilities


set in %B00000000,
eval,
output;


set in %B11111111,
eval,
output;


set in %B10101010,
eval,
output;


set in %B01010101,
eval,
output;

