// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

  // Initialize R2=0
  @2
  M=0
  // Initialize a=0
  @a
  M=0

(LOOP)
  @a
  D=M
  @0
  D=D-M
  @HALT
  D;JGE // Check if a-r0 < 0

  @1
  D=M
  @2
  M=D+M
  @a
  M=M+1
  @LOOP
  0;JMP

(HALT)
  @HALT
  0;JMP