
    section .data
        hello db 'k', 0

    section .bss
        hConsole resq 1

    section .text
        extern GetStdHandle, WriteConsoleA, ExitProcess
        global Start

    Start:
        ; Get the handle to the console
        sub rsp, 28h
        mov rcx, -11
        call GetStdHandle
        mov [hConsole], rax

        ; Write the message to the console
        mov rcx, [hConsole]
        lea rdx, [hello]
        mov r8, 1
        lea r9, [rsp+20h]
        mov qword [rsp+20h], 0
        call WriteConsoleA

        ; Exit the program
        xor rcx, rcx
        call ExitProcess
    