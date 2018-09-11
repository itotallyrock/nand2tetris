
load Mux8Way16.hdl,
output-file Mux8Way16.out,
compare-to Mux8Way16.cmp,
output-list a%B3.16.3 b%B3.16.3  c%B3.16.3 d%B3.16.3 e%B3.16.3 f%B3.16.3 g%B3.16.3 h%B3.16.3 sel%B3.3.3 out%B3.16.3;

// Used these eight test cases because it there were over 256 possiblities


set a %B0000000000000000,
set b %B1111111111111111,
set c %B1010101010101010,
set d %B0101010101010101,
set e %B1001001001001001,
set f %B0010010010010010,
set g %B0000000011111111,
set h %B1111111100000000,
set sel %B000,
eval,
output;
    
set sel %B001,
eval,
output;
    
set sel %B010,
eval,
output;
    
set sel %B011,
eval,
output;
    
set sel %B100,
eval,
output;
    
set sel %B101,
eval,
output;
    
set sel %B110,
eval,
output;
    
set sel %B111,
eval,
output;
    