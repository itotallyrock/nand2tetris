// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

  @SCREEN
  D=A
  @SCREEN_END
  M=D

  // Set screen length and screen end
  @8191
  D=A
  @SCREEN_LENGTH
  M=D
  @SCREEN_END
  M=M+D

  // set current position
  @SCREEN
  D=A


(KEYCHECK)
  @KBD
  D=M
  // If key is pressed FILL_B if not FILL_W
  @FILL_B
  D;JGT
  @FILL_W
  0;JMP

(FILL_B)
  @color
  M=-1
  @FILL
  0;JMP

(FILL_W)
  @color
  M=0
  @FILL
  0;JMP

(FILL)
  @SCREEN_LENGTH
  D=M
  @current
  M=D

  (NEXT)
    @current
    D=M
    @position
    M=D
    @SCREEN
    D=A
    @position
    M=M+D

    @color
    D=M
    @position
    A=M
    M=D

    @current
    D=M-1
    M=D

    @NEXT
    D;JGE

  @KEYCHECK
  0;JMP
