
load ALU.hdl,
output-file ALU.out,
compare-to ALU.cmp,
output-list x%B3.16.3 y%B3.16.3 zx%B3.1.3 nx%B3.1.3 zy%B3.1.3 ny%B3.1.3 f%B3.1.3 no%B3.1.3 out%B3.16.3 zr%B3.1.3 ng%B3.1.3;

// Used these 6 cases because there were over 256 possibilities


set x %B0000000000000000,
set y %B0000000000000000,
set zx 0,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zx 1,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;


set x %B1111111111111111,
set y %B1111111111111111,
set zx 0,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zx 1,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;


set x %B1111111111111111,
set y %B0000000000000000,
set zx 0,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zx 1,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;


set x %B1010101010101010,
set y %B0101010101010101,
set zx 0,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zx 1,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;


set x %B1010101010101010,
set y %B0000000000000000,
set zx 0,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zx 1,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;


set x %B1010101010101010,
set y %B1111111111111111,
set zx 0,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zx 1,
set nx 0,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set nx 1,
set zy 0,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set zy 1,
set ny 0,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;

set ny 1,
set f 0,
set no 0,
eval,
output;

set no 1,
eval,
output;

set f 1,
set no 0,
eval,
output;

set no 1,
eval,
output;
