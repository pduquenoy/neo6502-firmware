; ************************************************************************************************
; ************************************************************************************************
;
;		Name:		errorhandler.asm
;		Purpose:	Handle Errors
;		Created:	11th December 2023
;		Reviewed:   No
;		Author:		Paul Robson (paul@robsons.org.uk)
;
; ************************************************************************************************
; ************************************************************************************************

; ************************************************************************************************
;
;											Handle Errors
;
; ************************************************************************************************

		.section code	

Unimplemented:
		.error_unimp

ErrorHandler:		
		tax 								; error number in X
		lda 	#ErrorMessageText & $FF
		sta 	zTemp0
		lda 	#ErrorMessageText >> 8
		sta 	zTemp0+1
_EHFindMessage: 							; find the message
		dex
		beq 	_EHFoundMessage		
_EHSkip:
		lda 	(zTemp0)
		inc 	zTemp0
		bne 	_EHNoCarry
		inc 	zTemp0+1
_EHNoCarry:		
		cmp 	#0
		bne 	_EHSkip
		bra 	_EHFindMessage
_EHFoundMessage: 							; print the message
		ldy 	#0
_EHMPrint:		
		lda 	(zTemp0),y
		jsr 	CPPrintA
		iny
		lda 	(zTemp0),y
		bne 	_EHMPrint
		;
		lda 	ERRLine 					; check for line #
		ora 	ERRLine+1		
		beq 	_EHWarmStart
		ldy 	#_EHAtMsg >> 8
		lda 	#_EHAtMsg & $FF
		jsr 	CPPrintYA 

		ldx 	#0 							; print line number.
		lda 	ERRLine
		sta 	XSNumber0,x
		lda 	ERRLine+1
		sta 	XSNumber1,x
		stz 	XSNumber2,x
		stz 	XSNumber3,x
		stz 	XSControl,x
		jsr 	CPNumberToString		
		jsr 	CPPrintYA 

_EHWarmStart:
		lda 	#13 						; CR
		jsr 	WriteCharacter
		jmp 	WarmStart

_EHAtMsg:
		.text 	9," at line "

		.send code
		
; ************************************************************************************************
;
;									Changes and Updates
;
; ************************************************************************************************
;
;		Date			Notes
;		==== 			=====
;
; ************************************************************************************************

