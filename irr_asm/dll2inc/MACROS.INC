;##########################################################################
; macros
;##########################################################################
macro m2m dest,src {
	push	src
	pop	dest
}
;##########################################################################
macro showint caption,value {
	local .over,.str
	jmp	.over
	.str	db caption," = %i",0
.over:	pushad
	mov	ebx,value
	stdcall [GlobalAlloc],GMEM_MOVEABLE+GMEM_ZEROINIT,1000h
	push	eax
	push	eax
	stdcall [GlobalLock],eax
	push	eax
	ccall	[wsprintf],eax,OFFSET .str,ebx
	pop	eax
	stdcall [MessageBox],0,eax,0,MB_OK+MB_ICONASTERISK+MB_APPLMODAL
	call	[GlobalUnlock]
	call	[GlobalFree]
	popad
}
;##########################################################################
macro showuint caption,value {
	local .over,.str
	jmp	.over
	.str	db caption," = %u",0
.over:	pushad
	mov	ebx,value
	stdcall [GlobalAlloc],GMEM_MOVEABLE+GMEM_ZEROINIT,1000h
	push	eax
	push	eax
	stdcall [GlobalLock],eax
	push	eax
	ccall	[wsprintf],eax,OFFSET .str,ebx
	pop	eax
	stdcall [MessageBox],0,eax,0,MB_OK+MB_ICONASTERISK+MB_APPLMODAL
	call	[GlobalUnlock]
	call	[GlobalFree]
	popad
}
;##########################################################################
macro showhex caption,value {
	local .over,.str
	jmp	.over
	.str	db caption," = %08Xh",0
.over:	pushad
	mov	ebx,value
	stdcall [GlobalAlloc],GMEM_MOVEABLE+GMEM_ZEROINIT,1000h
	push	eax
	push	eax
	stdcall [GlobalLock],eax
	push	eax
	ccall	[wsprintf],eax,OFFSET .str,ebx
	pop	eax
	stdcall [MessageBox],0,eax,0,MB_OK+MB_ICONASTERISK+MB_APPLMODAL
	call	[GlobalUnlock]
	call	[GlobalFree]
	popad
}
;##########################################################################
macro showstr caption,value {
	local .over,.str
	jmp	.over
	.str	db caption," = %s",0
.over:	pushad
	mov	ebx,value
	stdcall [GlobalAlloc],GMEM_MOVEABLE+GMEM_ZEROINIT,1000h
	push	eax
	push	eax
	stdcall [GlobalLock],eax
	push	eax
	ccall	[wsprintf],eax,OFFSET .str,ebx
	pop	eax
	stdcall [MessageBox],0,eax,0,MB_OK+MB_ICONASTERISK+MB_APPLMODAL
	call	[GlobalUnlock]
	call	[GlobalFree]
	popad
}
;##########################################################################
macro showfmt fmtstr,[values] {
	common	local .over,.str,..size
	jmp	.over
	.str	db fmtstr,0
.over:	pushad
	stdcall [GlobalAlloc],GMEM_MOVEABLE+GMEM_ZEROINIT,1000h
	push	eax
	push	eax
	stdcall [GlobalLock],eax
	push	eax
	..size = 8
 reverse
	pushd values
	..size = ..size+4
 common
	push	OFFSET .str
	push	eax
	call	[wsprintf]
	add	esp,..size
	pop	eax
	stdcall [MessageBox],0,eax,0,MB_OK+MB_ICONASTERISK+MB_APPLMODAL
	stdcall [GlobalUnlock]
	stdcall [GlobalFree]
	popad
}
;##########################################################################
macro lasterr {
	pushad
	stdcall [GlobalAlloc],GMEM_MOVEABLE+GMEM_ZEROINIT,1000h
	push	eax
	push	eax
	stdcall [GlobalLock],eax
	push	eax
	call	[GetLastError]
	stdcall [FormatMessage],FORMAT_MESSAGE_FROM_SYSTEM,0,eax,0,[esp+08h],1000h,0
	pop	eax
	stdcall [MessageBox],0,eax,0,MB_OK+MB_ICONASTERISK+MB_APPLMODAL
	call	[GlobalUnlock]
	call	[GlobalFree]
	popad
}
;##########################################################################
macro msgbox value {
	pushad
	stdcall [MessageBox],0,value,0,MB_OK+MB_ICONASTERISK+MB_APPLMODAL
	popad
}
;##########################################################################
macro ucase expr {
	local .over
	cmp	expr,"z"
	ja	.over
	cmp	expr,"a"
	jb	.over
	sub	expr,32
.over:
}
;##########################################################################
macro lcase expr {
	local .over
	cmp	expr,"Z"
	ja	.over
	cmp	expr,"A"
	jb	.over
	add	expr,32
.over:
}
;##########################################################################
macro months [dayscount]
{
  forward
   if DAY <= dayscount
   else
    DAY = DAY-dayscount
    MONTH = MONTH+1
  forward
   end if
}
TIME = %T
DAY = TIME/(24*3600)
DAY = DAY - (DAY+365)/(3*365+366)
YEAR = 1970+DAY/365
DAY = DAY mod 365 + 1
MONTH = 1
months 31,28,31,30,31,30,31,31,30,31,30,31

TIME = TIME mod (24*3600)
HOUR = TIME/3600
MINUTE = (TIME mod 3600)/60
SECOND = (TIME mod 3600) mod 60
DATE equ (DAY / 10 + '0'),(DAY MOD 10 + '0'),".",(MONTH / 10 + '0'),(MONTH MOD 10 + '0'),".",(YEAR / 1000 + '0'),((YEAR / 100) MOD 10 + '0'),((YEAR / 10) MOD 10 + '0'),(YEAR MOD 10 + '0')
TIME equ (HOUR / 10 + '0'),(HOUR MOD 10 + '0'),":",(MINUTE / 10 + '0'),(MINUTE MOD 10 + '0'),":",(SECOND / 10 + '0'),(SECOND MOD 10 + '0')
;##########################################################################
