load DMux4Way.hdl,
output-file DMux4Way.out,
compare-to DMux4Way.cmp,
output-list in%B3.1.3 sel%B3.2.3 a%B3.1.3 b%B3.1.3 c%B3.1.3 d%B3.1.3;

set in 0,
set sel %B00,
eval,
output;

set sel %B01,
eval,
output;

set sel %B10,
eval,
output;

set sel %B11,
eval,
output;

set in 1,
set sel %B00,
eval,
output;

set sel %B01,
eval,
output;

set sel %B10,
eval,
output;

set sel %B11,
eval,
output;

