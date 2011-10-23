;##########################################################################
; dll2inc
; 07.12.2003 - 15.12.2003
; coded by comrade <comrade2k@hotmail.com>
; IRC: #asm, #coders, #win32asm on EFnet
; Web: http://comrade64.cjb.net/
;      http://comrade.win32asm.com/
;##########################################################################
format PE console 4.0
entry start
;##########################################################################
_TITLE		equ  "dll2inc"
_NAME		equ  "dll2inc"
_VERSION	equ  "1.0"
_VERSIONTEXT	equ  _VERSION
;##########################################################################
include "%fasminc%/win32a.inc"
;include "%include%/macro/if.inc"
include "macros.inc"
include "imagehdr.inc"
OFFSET equ
;##########################################################################
;##########################################################################
section ".code" code readable executable
;##########################################################################
start:
;##########################################################################
;##########################################################################
	push	ebx esi edi
	stdcall [GetStdHandle],STD_OUTPUT_HANDLE
	mov	[hStdOut],eax
	call	ProcessCmdLine
	cmp	[argc],02h
	mov	ecx,OFFSET szUsage
	jne	.err
	stdcall [CreateFile],[argv+04h],GENERIC_READ,FILE_SHARE_READ,0,OPEN_EXISTING,0,0
	mov	[hFile],eax
	xor	ecx,ecx
	cmp	eax,INVALID_HANDLE_VALUE
	je	.err
	stdcall [ReadFile],eax,OFFSET doshdr,sizeof.IMAGE_DOS_HEADER,esp,0
	cmp	[doshdr.e_magic],"MZ"
	mov	ecx,OFFSET szInvalidFormat
	jne	.err
	stdcall [SetFilePointer],[hFile],[doshdr.e_lfanew],0,FILE_BEGIN
	stdcall [ReadFile],[hFile],OFFSET nthdrs,sizeof.IMAGE_NT_HEADERS,esp,0
	cmp	[nthdrs.Signature],"PE"
	mov	ecx,OFFSET szInvalidFormat
	jne	.err
	mov	esi,dword [nthdrs.OptionalHeader.DataDirectory]
	movzx	ebx,[nthdrs.FileHeader.NumberOfSections]
.sec:	dec	ebx
	mov	ecx,OFFSET szInvalidFormat
	jl	.err
	stdcall [ReadFile],[hFile],OFFSET sechdr,sizeof.IMAGE_SECTION_HEADER,esp,0
	mov	eax,[sechdr.VirtualAddress]
	cmp	eax,esi
	ja	.sec
	add	eax,[sechdr.SizeOfRawData]
	cmp	eax,esi
	jb	.sec
.eos:	sub	esi,[sechdr.VirtualAddress]
	add	esi,[sechdr.PointerToRawData]
	stdcall [SetFilePointer],[hFile],esi,0,FILE_BEGIN
	stdcall [ReadFile],[hFile],OFFSET expdir,sizeof.IMAGE_EXPORT_DIRECTORY,esp,0
	mov	eax,[expdir.nName]
	sub	eax,[sechdr.VirtualAddress]
	add	eax,[sechdr.PointerToRawData]
	stdcall [SetFilePointer],[hFile],eax,0,FILE_BEGIN
	stdcall [ReadFile],[hFile],OFFSET szName,100h,esp,0
	mov	eax,OFFSET szName-1
.lib:	inc	eax
	lcase	byte [eax]
	cmp	byte [eax],"."
	jne	@F
	mov	byte [eax],0
@@:	cmp	byte [eax],0
	jne	.lib
	inc	eax
	ccall	[wsprintf],OFFSET szMessage,OFFSET szLibraryFormat,[esp],[esp+4],eax,OFFSET szName
	stdcall [WriteFile],[hStdOut],OFFSET szMessage,eax,esp,0

	mov	eax,[expdir.AddressOfNames]
	sub	eax,[sechdr.VirtualAddress]
	add	eax,[sechdr.PointerToRawData]
	mov	[dwPosition],eax
.name:	dec	[expdir.NumberOfNames]
	jl	.quit
	stdcall [SetFilePointer],[hFile],[dwPosition],0,FILE_BEGIN
	add	[dwPosition],04h
	stdcall [ReadFile],[hFile],OFFSET lpName,04h,esp,0
	mov	eax,[lpName]
	sub	eax,[sechdr.VirtualAddress]
	add	eax,[sechdr.PointerToRawData]
	stdcall [SetFilePointer],[hFile],eax,0,FILE_BEGIN
	stdcall [ReadFile],[hFile],OFFSET szName,100h,esp,0
	ccall	[wsprintf],OFFSET szMessage,OFFSET szImportFormat,dword [esp],OFFSET szName
	stdcall [WriteFile],[hStdOut],OFFSET szMessage,eax,esp,0
	cmp	[expdir.NumberOfNames],0
	je	.name
	stdcall [WriteFile],[hStdOut],OFFSET szNext,5,esp,0
	jmp	.name
.err:	test	ecx,ecx
	jne	@F
	call	[GetLastError]
	stdcall [FormatMessage],FORMAT_MESSAGE_FROM_SYSTEM,0,eax,0,OFFSET szMessage,100h,0
	mov	ecx,OFFSET szMessage
@@:	push	ecx
	stdcall strlen,ecx
	pop	ecx
	stdcall [WriteFile],[hStdOut],ecx,eax,esp,0
.quit:	stdcall [CloseHandle],[hFile]
	pop	edi esi ebx
	stdcall [ExitProcess],0
;##########################################################################
ProcessCmdLine:
	push	ebx esi edi
	call	[GetCommandLine]
	mov	esi,eax
	mov	edi,OFFSET argv
	xor	ecx,ecx
	xor	ebx,ebx
	xor	edx,edx
.cmss:	mov	eax,esi
	mov	dl,20h
	cmp	byte [esi],22h
	sete	cl
	lea	edx,[edx+ecx*2]
	add	eax,ecx
	stosd
.cm00:	inc	esi
	cmp	byte [esi], 0
	je	.cm01
	cmp	byte [esi], dl
	jne	.cm00
	mov	byte [esi], 0
	add	esi,ecx
	inc	esi
	cmp	byte [esi], 0
	je	.cm01
	inc	[argc]
	jmp	.cmss
.cm01:	pop	edi esi ebx
	inc	[argc]
	ret
;##########################################################################
strlen:
	xor	eax,eax
	mov	edx,[esp+04h]
	test	edx,edx
	jz	.quit
	dec	eax
	dec	edx
@@:	inc	edx
	inc	eax
	cmp	byte [edx],0
	jne	@B
.quit:	retn
;##########################################################################
;##########################################################################
;##########################################################################
;##########################################################################
section ".data" import data readable writeable
	library kernel32,"kernel32.dll",user32,"user32.dll"
	include "%fasminc%/api/kernel32.inc"
	include "%fasminc%/api/user32.inc"
;##########################################################################
;##########################################################################
	szUsage 	db	"Usage: ",_NAME,".exe library.dll",13,10,0
	szInvalidFormat db	"Invalid format.",13,10,0
	szNext		db	",\\"
	szNewLine	db	13,10
	szTab		db	9
	szError 	db	"Error",0
	szLibraryFormat db	"library %s,""%s.%s""",13,10,"import %s,",0
	szImportFormat	db	"%s,""%s""",0
;##########################################################################
	hStdOut 	rd	01h
	hFile		rd	01h
	lpName		rd	01h
	dwPosition	rd	01h
	argc		rd	01h
	argv		rd	10h
	szName		rb	100h
	szMessage	rb	100h
	doshdr		IMAGE_DOS_HEADER
	nthdrs		IMAGE_NT_HEADERS
	sechdr		IMAGE_SECTION_HEADER
	expdir		IMAGE_EXPORT_DIRECTORY
;##########################################################################
;##########################################################################
section ".rsrc" resource data readable
	; identifiers
	IDV_MAIN		= 01
	; resources
	directory RT_VERSION,versions
	resource versions,IDV_MAIN,SUBLANG_NEUTRAL+LANG_NEUTRAL,version
	; version
	version version,VOS__WINDOWS32,VFT_APP,VFT2_UNKNOWN,SUBLANG_NEUTRAL+LANG_NEUTRAL,0,\
		"FileDescription",_TITLE,\
		"LegalCopyright",<0A9h," comrade">,\
		"FileVersion",_VERSION,\
		"ProductVersion",_VERSION,\
		"ProductName",_TITLE,\
		"InternalName",_NAME,\
		"OriginalFilename",<_NAME,".exe">
;##########################################################################
;##########################################################################