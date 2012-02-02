// Copyright(c) Max Kolosov 2010 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef _MSC_VER
#include <windows.h>

char* code_to_name(unsigned int code)
{
	switch(code)
	{
	case EXCEPTION_ACCESS_VIOLATION:
		return "EXCEPTION_ACCESS_VIOLATION";
		break;
	case EXCEPTION_ARRAY_BOUNDS_EXCEEDED:
		return "EXCEPTION_ARRAY_BOUNDS_EXCEEDED";
		break;
	case EXCEPTION_BREAKPOINT:
		return "EXCEPTION_BREAKPOINT";
		break;
	case EXCEPTION_DATATYPE_MISALIGNMENT:
		return "EXCEPTION_DATATYPE_MISALIGNMENT";
		break;
	case EXCEPTION_FLT_DENORMAL_OPERAND:
		return "EXCEPTION_FLT_DENORMAL_OPERAND";
		break;
	case EXCEPTION_FLT_DIVIDE_BY_ZERO:
		return "EXCEPTION_FLT_DIVIDE_BY_ZERO";
		break;
	case EXCEPTION_FLT_INEXACT_RESULT:
		return "EXCEPTION_FLT_INEXACT_RESULT";
		break;
	case EXCEPTION_FLT_INVALID_OPERATION:
		return "EXCEPTION_FLT_INVALID_OPERATION";
		break;
	case EXCEPTION_FLT_OVERFLOW:
		return "EXCEPTION_FLT_OVERFLOW";
		break;
	case EXCEPTION_FLT_STACK_CHECK:
		return "EXCEPTION_FLT_STACK_CHECK";
		break;
	case EXCEPTION_FLT_UNDERFLOW:
		return "EXCEPTION_FLT_UNDERFLOW";
		break;
	case EXCEPTION_ILLEGAL_INSTRUCTION:
		return "EXCEPTION_ILLEGAL_INSTRUCTION";
		break;
	case EXCEPTION_IN_PAGE_ERROR:
		return "EXCEPTION_IN_PAGE_ERROR";
		break;
	case EXCEPTION_INT_DIVIDE_BY_ZERO:
		return "EXCEPTION_INT_DIVIDE_BY_ZERO";
		break;
	case EXCEPTION_INT_OVERFLOW:
		return "EXCEPTION_INT_OVERFLOW";
		break;
	case EXCEPTION_INVALID_DISPOSITION:
		return "EXCEPTION_INVALID_DISPOSITION";
		break;
	case EXCEPTION_NONCONTINUABLE_EXCEPTION:
		return "EXCEPTION_NONCONTINUABLE_EXCEPTION";
		break;
	case EXCEPTION_PRIV_INSTRUCTION:
		return "EXCEPTION_PRIV_INSTRUCTION";
		break;
	case EXCEPTION_SINGLE_STEP:
		return "EXCEPTION_SINGLE_STEP";
		break;
	case EXCEPTION_STACK_OVERFLOW:
		return "EXCEPTION_STACK_OVERFLOW";
		break;
	default:
		return "Unknown exception code.";
	}
}

int filter(unsigned int code, struct _EXCEPTION_POINTERS *ep, char* caller_name = "UNKNOWN CALLER")
{
	struct _EXCEPTION_RECORD* er = ep->ExceptionRecord;
	printf("%s - ERROR EXECUTION\n", caller_name);
	while (er)
	{
		printf("ExceptionCode: %d\n", er->ExceptionCode);
		printf("ExceptionName: %s\n", code_to_name(er->ExceptionCode));
		printf("ExceptionAddress: %x (%d)\n", er->ExceptionAddress, er->ExceptionAddress);
		printf("ExceptionFlags: %d\n", er->ExceptionFlags);
		printf("NumberParameters: %d\n", er->NumberParameters);
		er = er->ExceptionRecord;
	}
	return EXCEPTION_EXECUTE_HANDLER;
}
#endif
