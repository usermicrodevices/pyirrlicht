' (C) Roberto Bianchi

uses "UI"

%OPT1 = 101
%OPT2 = 102
%OPT3 = 103
%OPT4 = 104
%OPT5 = 105
%OPT6 = 106
%LBL1 = 201

FUNCTION ChooseDriver(sTitle as string) as long
    DIM Msg       AS LONG
    DIM wParam    AS LONG
    DIM lParam    AS LONG
    DIM hDlg      AS DWORD
    dim lResult   as long
    dim sResult   as string
    dim Count     as long

    DIALOG NEW 0, sTitle, -1, -1, 180, 158, %WS_SYSMENU or %ds_center OR %WS_CAPTION TO hDlg
    CONTROL ADD LABEL , hDlg, %LBL1, "Please select the driver you want for this example:", 6, 8, 170, 30
    CONTROL ADD OPTION, hDlg, %OPT1, "NullDevice",               15,  24, 110, 14, %WS_GROUP OR %WS_TABSTOP
    CONTROL ADD OPTION, hDlg, %OPT2, "Software Renderer",                15,  38, 110, 14
    CONTROL ADD OPTION, hDlg, %OPT3, "Burnings Video",                  15,  52, 110, 14
    CONTROL ADD OPTION, hDlg, %OPT4, "OpenGL",           15,  66, 110, 14
    CONTROL ADD OPTION, hDlg, %OPT5, "Direct3D8",              15,  80, 110, 14
    CONTROL ADD OPTION, hDlg, %OPT6, "Direct3D9",                  15,  94, 110, 14
    CONTROL ADD BUTTON, hDlg, %IDOK, "OK",                          50, 122,  80, 14, %WS_GROUP OR %WS_TABSTOP

    '---Set the initial state to OPTION button 2
    CONTROL SET OPTION hDlg, %OPT2, %OPT1, %OPT6

  DIALOG SHOW MODELESS hDlg

  '---Start the main message loop
  WHILE IsWindow(hDlg)                  

    '---Get the message and fill wParam and lParam
    Msg = GetMessage(hDlg, wParam, lParam)        
    SELECT CASE Msg
      CASE %WM_COMMAND

        '---Test which control has been clicked
        SELECT CASE wParam

          '---A number was activated
          CASE %IDOK
            sResult = ""
            for Count = %OPT1 to %OPT6
              CONTROL GET CHECK hDlg, Count TO lResult
              if lResult then exit for
            next
            select case Count
                case %OPT1
                    function = %EDT_NULL
                case %OPT2
                    function = %EDT_SOFTWARE
                case %OPT3
                    function = %EDT_BURNINGSVIDEO
                case %OPT4
                    function = %EDT_OPENGL
                case %OPT5
                    function = %EDT_DIRECT3D8
                case %OPT6
                    function = %EDT_DIRECT3D9
            END SELECT
            exit while

        END SELECT

      CASE %WM_SYSCOMMAND

        SELECT CASE wParam
            
          CASE %SC_CLOSE
            EXIT WHILE

              
        END SELECT

      CASE ELSE
      
    END SELECT
    
  WEND

  DIALOG END hDlg


END FUNCTION
