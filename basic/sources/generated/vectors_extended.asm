;
;	This file is automatically generated.
;
	.section code
ExtendedVectorTable:
	.word	Command_CLEAR            ; $180 clear
	.word	Command_NEW              ; $181 new
	.word	Command_RUN              ; $182 run
	.word	Command_STOP             ; $183 stop
	.word	Command_END              ; $184 end
	.word	Command_ASSERT           ; $185 assert
	.word	Command_LIST             ; $186 list
	.word	Command_Save             ; $187 save
	.word	Command_Load             ; $188 load
	.word	Command_CAT              ; $189 cat
	.word	Command_GOSUB            ; $18a gosub
	.word	Command_GOTO             ; $18b goto
	.word	Command_RETURN           ; $18c return
	.word	Command_RESTORE          ; $18d restore
	.word	DimCommand               ; $18e dim
	.word	Command_FKEY             ; $18f fkey
	.word	Command_CLS              ; $190 cls
	.word	Command_INK              ; $191 ink
	.word	Unimplemented            ; $192 frame
	.word	Unimplemented            ; $193 solid
	.word	Unimplemented            ; $194 by
	.word	Command_WHO              ; $195 who
	.word	Command_Palette          ; $196 palette
	.word	Unimplemented            ; $197 draw
	.word	Unimplemented            ; $198 hide
	.word	Unimplemented            ; $199 flip
	.word	Command_SOUND            ; $19a sound
	.word	Unimplemented            ; $19b sfx
	.word	Unimplemented            ; $19c slide
	.send code
