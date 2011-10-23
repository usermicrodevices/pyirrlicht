struc IMAGE_DATA_DIRECTORY {
  .VirtualAddress    dd      ?
  .isize	     dd      ?
}
struct IMAGE_DATA_DIRECTORY

struc IMAGE_OPTIONAL_HEADER32 {
  .Magic			 dw	 ?
  .MajorLinkerVersion		 db	 ?
  .MinorLinkerVersion		 db	 ?
  .SizeOfCode			 dd	 ?
  .SizeOfInitializedData	 dd	 ?
  .SizeOfUninitializedData	 dd	 ?
  .AddressOfEntryPoint		 dd	 ?
  .BaseOfCode			 dd	 ?
  .BaseOfData			 dd	 ?
  .ImageBase			 dd	 ?
  .SectionAlignment		 dd	 ?
  .FileAlignment		 dd	 ?
  .MajorOperatingSystemVersion	 dw	 ?
  .MinorOperatingSystemVersion	 dw	 ?
  .MajorImageVersion		 dw	 ?
  .MinorImageVersion		 dw	 ?
  .MajorSubsystemVersion	 dw	 ?
  .MinorSubsystemVersion	 dw	 ?
  .Win32VersionValue		 dd	 ?
  .SizeOfImage			 dd	 ?
  .SizeOfHeaders		 dd	 ?
  .CheckSum			 dd	 ?
  .Subsystem			 dw	 ?
  .DllCharacteristics		 dw	 ?
  .SizeOfStackReserve		 dd	 ?
  .SizeOfStackCommit		 dd	 ?
  .SizeOfHeapReserve		 dd	 ?
  .SizeOfHeapCommit		 dd	 ?
  .LoaderFlags			 dd	 ?
  .NumberOfRvaAndSizes		 dd	 ?
  .DataDirectory		 rb	 sizeof.IMAGE_DATA_DIRECTORY*16
}
; struct IMAGE_OPTIONAL_HEADER32

IMAGE_OPTIONAL_HEADER  equ  IMAGE_OPTIONAL_HEADER32

struc IMAGE_FILE_HEADER {
  .Machine		 dw    ?
  .NumberOfSections	 dw    ?
  .TimeDateStamp	 dd    ?
  .PointerToSymbolTable  dd    ?
  .NumberOfSymbols	 dd    ?
  .SizeOfOptionalHeader  dw    ?
  .Characteristics	 dw    ?
}
; struct IMAGE_FILE_HEADER

struc IMAGE_NT_HEADERS {
  .Signature	     dd 		  ?
  .FileHeader	     IMAGE_FILE_HEADER
  .OptionalHeader    IMAGE_OPTIONAL_HEADER32
}
; struct IMAGE_NT_HEADERS

struc IMAGE_EXPORT_DIRECTORY {
  .Characteristics	     dd      ?
  .TimeDateStamp	     dd      ?
  .MajorVersion 	     dw      ?
  .MinorVersion 	     dw      ?
  .nName		     dd      ?
  .nBase		     dd      ?
  .NumberOfFunctions	     dd      ?
  .NumberOfNames	     dd      ?
  .AddressOfFunctions	     dd      ?
  .AddressOfNames	     dd      ?
  .AddressOfNameOrdinals     dd      ?
}
; struct IMAGE_EXPORT_DIRECTORY

struc IMAGE_DOS_HEADER {
  .e_magic	     dw      ?
  .e_cblp	     dw      ?
  .e_cp 	     dw      ?
  .e_crlc	     dw      ?
  .e_cparhdr	     dw      ?
  .e_minalloc	     dw      ?
  .e_maxalloc	     dw      ?
  .e_ss 	     dw      ?
  .e_sp 	     dw      ?
  .e_csum	     dw      ?
  .e_ip 	     dw      ?
  .e_cs 	     dw      ?
  .e_lfarlc	     dw      ?
  .e_ovno	     dw      ?
  .e_res	     rw      04h
  .e_oemid	     dw      ?
  .e_oeminfo	     dw      ?
  .e_res2	     rw      0Ah
  .e_lfanew	     dd      ?
}
; struct IMAGE_DOS_HEADER

struc IMAGE_SECTION_HEADER {
    .Name1 rb 8
    .Misc dd ?
    virtual at .Misc
	.PhysicalAddress dd  ?
	.VirtualSize dd      ?
    end virtual
    .VirtualAddress dd	     ?
    .SizeOfRawData dd	     ?
    .PointerToRawData dd     ?
    .PointerToRelocations dd ?
    .PointerToLinenumbers dd ?
    .NumberOfRelocations dw  ?
    .NumberOfLinenumbers dw  ?
    .Characteristics dd      ?
}
; struct IMAGE_SECTION_HEADER

