;
; File generated by cc65 v 2.19 - Git 4b9bf9bb9
;
	.fopt		compiler,"cc65 v 2.19 - Git 4b9bf9bb9"
	.setcpu		"65C02"
	.smart		on
	.autoimport	on
	.case		on
	.debuginfo	off
	.importzp	sp, sreg, regsave, regbank
	.importzp	tmp1, tmp2, tmp3, tmp4, ptr1, ptr2, ptr3, ptr4
	.macpack	longbranch
	.forceimport	__STARTUP__
	.import		_puts
	.export		_write
	.export		_main

.segment	"RODATA"

S0002:
	.byte	$48,$65,$6C,$6C,$6F,$20,$77,$6F,$72,$6C,$64,$0A,$00
S0001	:=	S0002+0

; ---------------------------------------------------------------
; int __near__ write (int fildes, const unsigned char *buf, unsigned int count)
; ---------------------------------------------------------------

.segment	"CODE"

.proc	_write: near

.segment	"CODE"

	jsr     pushax
	ldx     #$FF
	stz     M0001
	stx     M0001+1
	bra     L0004
L0005:	lda     M0001+1
	sta     ptr1+1
	lda     M0001
	sta     ptr1
	lda     (ptr1)
	bne     L0005
	lda     M0001
	ldx     M0001+1
	ina
	bne     L0008
	inx
L0008:	sta     ptr1
	stx     ptr1+1
	lda     #$00
	sta     (ptr1)
	lda     M0001
	ldx     M0001+1
	jsr     incax4
	sta     sreg
	stx     sreg+1
	ldy     #$03
	jsr     ldaxysp
	sta     ptr1
	stx     ptr1+1
	lda     (ptr1)
	sta     (sreg)
	ldy     #$02
	ldx     #$00
	lda     #$01
	jsr     addeqysp
	lda     M0001+1
	sta     ptr1+1
	lda     M0001
	sta     ptr1
	lda     #$02
	sta     (ptr1)
L0004:	ldy     #$01
	lda     (sp),y
	ora     (sp)
	php
	ldx     #$00
	tya
	jsr     subeq0sp
	plp
	bne     L0005
	ldx     #$00
	txa
	jmp     incsp6

.segment	"BSS"

M0001:
	.res	2,$00

.endproc

; ---------------------------------------------------------------
; int __near__ main (void)
; ---------------------------------------------------------------

.segment	"CODE"

.proc	_main: near

.segment	"CODE"

	lda     #<(S0001)
	ldx     #>(S0001)
	jsr     _puts
	lda     #<(S0002)
	ldx     #>(S0002)
	jsr     _puts
	ldx     #$00
	txa
	rts

.endproc
