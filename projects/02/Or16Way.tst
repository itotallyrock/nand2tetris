
load Or16Way.hdl,
output-file Or16Way.out,
compare-to Or16Way.cmp,
output-list in%B3.16.3 out%B3.1.3;

// Used these 4 cases because there were over 256 possibilities


set in %B0000000000000000,
eval,
output;


set in %B1111111111111111,
eval,
output;


set in %B1010101010101010,
eval,
output;


set in %B0101010101010101,
eval,
output;

