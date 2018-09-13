
load Add16.hdl,
output-file Add16.out,
compare-to Add16.cmp,
output-list a%B3.16.3 b%B3.16.3 out%B3.16.3;

// Used these 6 cases because there were over 256 possiblities


set a %B0000000000000000,
set b %B0000000000000000,
eval,
output;


set a %B1111111111111111,
set b %B1111111111111111,
eval,
output;


set a %B1111111111111111,
set b %B0000000000000000,
eval,
output;


set a %B1010101010101010,
set b %B0101010101010101,
eval,
output;


set a %B1010101010101010,
set b %B0000000000000000,
eval,
output;


set a %B1010101010101010,
set b %B1111111111111111,
eval,
output;

