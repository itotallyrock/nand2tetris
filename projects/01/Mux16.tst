
load Mux16.hdl,
output-file Mux16.out,
compare-to Mux16.cmp,
output-list a%B3.16.3 b%B3.16.3  sel%B3.1.3 out%B3.16.3;

// Used these six test cases because it there were over 256 possibilities


set a %B0000000000000000,
set b %B0000000000000000,
set sel 0,
eval,
output;

    
set a %B0000000000000000,
set b %B0000000000000000,
set sel 1,
eval,
output;

    
set a %B1111111111111111,
set b %B1111111111111111,
set sel 0,
eval,
output;

    
set a %B1111111111111111,
set b %B1111111111111111,
set sel 1,
eval,
output;

    
set a %B1111111111111111,
set b %B0000000000000000,
set sel 0,
eval,
output;

    
set a %B1111111111111111,
set b %B0000000000000000,
set sel 1,
eval,
output;

    
set a %B1010101010101010,
set b %B0101010101010101,
set sel 0,
eval,
output;

    
set a %B1010101010101010,
set b %B0101010101010101,
set sel 1,
eval,
output;

    
set a %B1010101010101010,
set b %B0000000000000000,
set sel 0,
eval,
output;

    
set a %B1010101010101010,
set b %B0000000000000000,
set sel 1,
eval,
output;

    
set a %B1010101010101010,
set b %B1111111111111111,
set sel 0,
eval,
output;

    
set a %B1010101010101010,
set b %B1111111111111111,
set sel 1,
eval,
output;

    