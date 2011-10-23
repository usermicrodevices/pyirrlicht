;
; for FASM 1.54
;
; d2inc - ��������� DLL ��������� � INC ����� ��� FASM'a.
; (c) 2004, ������� �. ���������� (ksoft@mail.ru)
;
; udapted to fasm 1.69 Maxim Kolosov 18.05.2010
;
	format PE console on 'null.stub'
	entry _start

	include '%fasminc%/win32a.inc'
	include 'fasm32.mac'
	include 'imagehdr.inc'

	IMAGE_NT_SIGNATURE	 equ 00004550h

	_AUTHOR 		 equ 'Dmitry N. Kolesnikov'
	_PROG_NAME		 equ 'd2incA'			; ��� ��������� ("d2incU" - ��� UNICODE ������).
	_VERSION		 equ '0.7A'			; ������ ("0.7U" - ��� UNICODE ������).
	_OUT_TYPE		 equ 'ANSI'			; ��� ("UNICODE" - ��� UNICODE ������).
	_TRUE_CHAR		 equ 'A'			; ("W" - ��� UNICODE ������).
	_FALSE_CHAR		 equ 'W'			; ("A" - ��� UNICODE ������).

	; struct IMAGE_EXPORT_DIRECTORY
		; Characteristics dw ?
		; TimeDateStamp dw ?
		; MajorVersion db ?
		; MinorVersion db ?
		; dwName dw ?
		; Base dw ?
		; NumberOfFunctions dw ?
		; NumberOfNames dw ?
		; AddressOfFunctions dd ?
		; AddressOfNames dd ?
		; AddressOfNameOrdinals db ?
	; ends

; #########################################################################
;
 section '.code' code readable executable
;
; #########################################################################

 _start:
	      xor     ebx,ebx
	      @call   [GetStdHandle],STD_OUTPUT_HANDLE
	      mov     [h_output],eax

	      call    [GetCommandLine]
	      mov     edi,eax
	      push    MAX_PATH
	      pop     ecx
	      movzx   eax,byte [edi]
	      cmp     eax,22h
	      jne     @F
	      inc     edi
	      repne   scasb

	      @@:
	      mov     al,20h
	      repne   scasb
	      cmp     byte [edi],bl
	      je      _write_about
	      mov     esi,edi
	      mov     edi,FileNameIn
	      push    edi

	      @@:
		lods	byte [esi]				; ��������� ��� ����� �� ����������
		cmp	al,22h					; ������ � ���������� 'FileNameIn' �
	      je      @B					; ������ ������ ("), ���� ����.
		stos	byte [edi]				;
		test	al,al					;
	      jnz     @B					;
	      pop     edi					; � EDI ��������� �� FileNameIn.

; #########################################################################

	      @call   [GetFileAttributes],edi			; ���� ����, ��������� � ����������
	      inc     eax					; ������, �� ����������, �� ��������
	      je      _error.file_not_found			; ������.
	      dec     eax

	      @call   [CreateFile],edi,GENERIC_READ,FILE_SHARE_READ,ebx,OPEN_EXISTING,ebx,ebx
	      test    eax,eax
	      jz      _error.not_open
	      mov     [h_file1],eax

	      mov     esi,FileNameOut
	      @call   [GetFileTitle],edi,esi,MAX_PATH
	      @call   GetStringLenght,esi
	      mov     dword [eax+esi-4],'.inc'			; ������ ���������� � '.dll' �� '.inc'.
	      @call   [CharLower],esi				;
	      mov     edi,ModName				;
	      @@:
		lods	byte [esi]				;
		cmp	al,'.'					;
	      je      @F					;
		stos	byte [edi]				;
	      jmp     @B					;
	      @@:
	      mov     byte [edi],bl

	      @call   [CreateFileMapping],[h_file1],ebx,PAGE_READONLY,ebx,ebx,ebx
	      test    eax,eax
	      jz      _error.not_create_mapping
	      mov     [h_map],eax
	      @call   [MapViewOfFile],eax,FILE_MAP_READ,ebx,ebx,ebx
	      test    eax,eax
	      jz      _error.not_mapping
	      mov     [p_map],eax

	      mov     esi,dword [eax+3Ch]			; � ESI ����� ������ PE ��������� (������������ ������ �����).
	      cmp     dword [eax+esi],IMAGE_NT_SIGNATURE	; ��� "PE" ����?
	      jne     _error.not_PE				;

	      mov     esi,dword [eax+esi+78h]			; ������� "Export table RVA".
	      test    esi,esi					; ���� ��� ����, �� DLL ��
	      jz      _error.no_exp				; �������� ���������� ������.

	      @call   RVAToFileMap,eax,esi			; ��������� "Export table RVA"
	      mov     esi,eax					; � �������� �������� � �����(������).
	      mov     [exp_va],eax

	      virtual at esi					;
		  ied IMAGE_EXPORT_DIRECTORY			; assume esi:ptr IMAGE_EXPORT_DIRECTORY
	      end virtual					;

	      mov     eax,dword [ied.NumberOfNames]			; ���� ����� ��������������
	      test    eax,eax					; ������� = 0,
	      jz      _error.no_exp				; �� �������� ������.
	      mov     [n_names],eax

	      @call   [CreateFile],FileNameOut,GENERIC_WRITE,FILE_SHARE_WRITE,ebx,CREATE_ALWAYS,FILE_ATTRIBUTE_NORMAL,ebx
	      mov     [h_file2],eax

	      mov     edi,FirstLine
	      @call   GetStringLenght,edi
	      @call   [WriteFile],[h_file2],edi,eax,tmp_var,ebx
;
; #########################################################################
;
	      mov     esi,[exp_va]
	      mov     eax,[ied.AddressOfNames]			; �������� ����� ������
	      @call   RVAToFileMap,[p_map],eax			; ������� ���� ��������������
	      mov     eax,dword [eax]				; �������.
	      @call   RVAToFileMap,[p_map],eax			;
	      mov     esi,eax					; ESI ��������� �� ������ ����� ������ �������.
 _read_next:
	      @call   GetStringLenght,esi
	      mov     [ln_name],eax
	      xor     edx,edx
	      mov     dl,byte [eax+esi-1]			; � DL ��������� ������ ����� �������.
	      cmp     edx,_FALSE_CHAR				; ���� ��� �� ������ ������, ��
	      je      _empty_line				; ��������� ��� �������.
	      xor     ecx,ecx					;
	      cmp     edx,_TRUE_CHAR				;
	      setne   cl					;
	      add     eax,ecx					;
	      @call   [lstrcpyn],FuncName,esi,eax		;

	      mov     edi,output_buffer 			; ��������� ��������� ��������
	      @call   [wsprintf],edi,format_str,eax,esi 	; ������ � ����� �� � ����.
	      add     esp,10h					; �������� ����, �.� �-�� wsprintf ����� C ���������.
	      @bpush  [h_file2],edi,eax,tmp_var,ebx		; -\
	      @bpush  [h_file2],end_line,4,tmp_var,ebx		;\  \
	      call    [WriteFile]				;/  /
	      call    [WriteFile]				; -/

 _empty_line:
	      add     esi,[ln_name]				    ; ESI ��������� �� ������ ��������� �������
	      inc     esi					    ; � ������� ���� �������������� �������.
	      mov     eax,[n_names]				    ; � EAX ����� ������� �������������� �� DLL.
	      dec     eax					    ; ��������� �� 1.
	      mov     [n_names],eax				    ;
	      jnz     _read_next				    ; ���� �� ����, �� ������� ��� ����.

	      @call   [WriteFile],[h_file2],crlf,2,tmp_var,ebx
	      @call   [CloseHandle],[h_file2]

 _exit_prog:
	      @call   [UnmapViewOfFile],[p_map]
	 .1:  @call   [CloseHandle],[h_map]
	 .2:  @call   [CloseHandle],[h_file1]
	 .3:  @call   [ExitProcess],ebx
;
; #########################################################################
;
 _write_about:
	      @call   [WriteConsole],[h_output],AboutMsg,l_AboutMsg,tmp_var,ebx
	      jmp     _exit_prog.3
 _error:
    .file_not_found:
	      @call   [WriteConsole],[h_output],errMsg1,l_errMsg1,tmp_var,ebx
	      jmp     _exit_prog.3
    .not_open:
	      @call   [WriteConsole],[h_output],errMsg2,l_errMsg2,tmp_var,ebx
	      jmp     _exit_prog.3
    .not_create_mapping:
	      @call   [WriteConsole],[h_output],errMsg3,l_errMsg3,tmp_var,ebx
	      jmp     _exit_prog.2
    .not_mapping:
	      @call   [WriteConsole],[h_output],errMsg4,l_errMsg4,tmp_var,ebx
	      jmp     _exit_prog.1
    .not_PE:
	      @call   [WriteConsole],[h_output],errMsg5,l_errMsg5,tmp_var,ebx
	      jmp     _exit_prog
    .no_exp:
	      @call   [WriteConsole],[h_output],errMsg6,l_errMsg6,tmp_var,ebx
	      jmp     _exit_prog
;
; #########################################################################
;

; ��������� "GetStringLenght"
 GetStringLenght:	; lpzStr
	      cld
	      push    edi
	      mov     edi,dword [esp+04h+04h]	 ; ��������� �� ������.
	      or      ecx,-1
	      xor     eax,eax
	      repnz   scas byte [edi]
	      xor     ecx,-1
	      dec     ecx			 ; ������� ������ ������.
	      mov     eax,ecx
	      pop     edi
	      ret     04h


; ��������� "RVAToFileMap"
 RVAToFileMap:		; pFileMap:DWORD, RVA:DWORD
	      push    edi esi edx ecx
	      mov     esi,dword [esp+04h+10h]  ;esi == pFileMap

		   virtual at esi
			s_idh IMAGE_DOS_HEADER
		   end virtual

	      add     esi,[s_idh.e_lfanew]

		   virtual at esi
			s_inth IMAGE_NT_HEADERS
		   end virtual

	      mov     edi,dword [esp+08h+10h]  ; edi == RVA
	      mov     edx,esi
	      add     edx,sizeof.IMAGE_NT_HEADERS
	      xor     ecx,ecx
	      mov     cx,[s_inth.FileHeader.NumberOfSections]

		   virtual at edx
			s_ish IMAGE_SECTION_HEADER
		   end virtual

	     .@_1:
	      cmp     edi,[s_ish.VirtualAddress]
	      jb      .@_2
	      mov     eax,[s_ish.VirtualAddress]
	      add     eax,[s_ish.SizeOfRawData]
	      cmp     edi,eax
	      ja      .@_2
	      mov     eax,[s_ish.VirtualAddress]
	      sub     edi,eax
	      mov     eax,[s_ish.PointerToRawData]
	      add     eax,edi
	      add     eax,dword [esp+04h+10h]
	      jmp     .@_3
	     .@_2:
	      add     edx,sizeof.IMAGE_SECTION_HEADER
	      dec     ecx
	      jnz     .@_1
	      mov     eax,edi
	     .@_3:
	      pop     ecx edx esi edi
	      ret     08h
;
; #########################################################################
;
 data import
	library kernel32,'KERNEL32.DLL',\
		user32,'USER32.DLL',\
		comdlg32,'COMDLG32.DLL'

	include '%fasminc%/api/kernel32.inc'
	include '%fasminc%/api/user32.inc'
	include '%fasminc%/api/comdlg32.inc'
 end data
;
; #########################################################################
;
  section '.data' data readable writeable
;
; #########################################################################
;
 AboutMsg	   db 'DLL to ',_OUT_TYPE,' FASM include file converter Version ',_VERSION,0Dh,0Ah
		   db '(c) ',_AUTHOR,' 2004 <ksoft@mail.ru>',0Dh,0Ah,0Dh,0Ah
		   db 'Syntax: ',_PROG_NAME,'.exe srcname.dll',0Dh,0Ah
 l_AboutMsg = $ - AboutMsg

 errMsg1	   db 'Cannot find DLL file',0Dh,0Ah
 l_errMsg1 = $ - errMsg1

 errMsg2	   db 'Cannot open the file for reading',0Dh,0Ah
 l_errMsg2 = $ - errMsg2

 errMsg3	   db 'Cannot open the file for memory mapping',0Dh,0Ah
 l_errMsg3 = $ - errMsg3

 errMsg4	   db 'Cannot map the file into memory',0Dh,0Ah
 l_errMsg4 = $ - errMsg4

 errMsg5	   db 'This file is not a valid PE',0Dh,0Ah
 l_errMsg5 = $ - errMsg5

 errMsg6	   db 'No export information in this file',0Dh,0Ah
 l_errMsg6 = $ - errMsg6

; #########################################################################

 FirstLine	   db '; Created by using ',_PROG_NAME		; ������ ������,
		   db 0Dh,0Ah,0Dh,0Ah				; ������� ����� ��������
		   db 'import',20h				; � �������� ����.
 ModName	   rb 10					;
;
 end_line	   db ',\\'					; ��� ����� �����������
 crlf		   db 0Dh,0Ah					; � ����� ������ ������.
;
 format_str:	   times 7 db 20h				;
		   db "%s,'%s'",0				;
 output_buffer	   rb 620					;
 FuncName	   rb 300					;

 FileNameIn	   rb MAX_PATH					; ����� ��� ��� �������� �����.
 FileNameOut	   rb MAX_PATH					; ����� ��� ��� ��������� �����.

 h_output	   dd ? 					; ����� �������.
 h_file1	   dd ? 					; ����� �������� �����.
 h_file2	   dd ? 					; ����� ��������� �����.
 h_map		   dd ? 					; ����� ��������� ������.
 p_map		   dd ? 					; ��������� �� ��������� ������.
 n_names	   dd ? 					; ����� �������������� �������.
 ln_name	   dd ? 					; ������ ����� �������.
 exp_va 	   dd ? 					;
 tmp_var	   dd ? 					; ���������� ��� ������ ����.
;
; #########################################################################
;