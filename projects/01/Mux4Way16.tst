
load Mux4Way16.hdl,
output-file Mux4Way16.out,
compare-to Mux4Way16.cmp,
output-list a%B3.16.3 b%B3.16.3  c%B3.16.3 d%B3.16.3 sel%B3.2.3 out%B3.16.3;

// Used these four test cases because it there were over 256 possiblities


set a %B0000000000000000,
set b %B1111111111111111,
set c %B1010101010101010,
set d %B0101010101010101,
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
    