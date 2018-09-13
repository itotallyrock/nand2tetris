
load Inc16.hdl,
output-file Inc16.out,
compare-to Inc16.cmp,
output-list in%B3.16.3 out%B3.16.3;

// Used these 4 test cases because there were over 256 possibilities


set in %B0000000000000000,
eval,
output;


set in %B1111111111111111,
eval,
output;


set in %B1100110100111101,
eval,
output;


set in %B0101010101010101,
eval,
output;

