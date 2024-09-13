import os

listC = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
listB = []
listA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
special_chars = [" ", "!", "?", "\n"]

for la922 in listA:
    listB.append(la922.lower())

def sanitize_filename(char):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', ' ']
    if char in invalid_chars:
        return '_'
    return char

def write_asm_file(char, filename):
    if char == "\n":
        charn = "0Ah"
    else:
        charn = char
    with open(filename, "w") as f:
        if charn != "0Ah":
            f.write(f"""
    section .data
        hello db '{charn}', 0

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
    """)
        else:
            f.write(f"""
section .data
    hello db {charn}, 0

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
""")

def compile_asm_file(filename):
    obj_file = filename.replace(".asm", ".obj")
    os.system(f"nasm -f win64 {filename} -o {obj_file}")
    os.system(f"GoLink /console {obj_file} kernel32.dll")

for la911 in listA:
    filename = f"Prints\\Assembly\\{sanitize_filename(la911)}.asm"
    write_asm_file(la911, filename)
    compile_asm_file(filename)

for lb911 in listB:
    filename = f"Prints\\Assembly\\{sanitize_filename(lb911)}.asm"
    write_asm_file(lb911, filename)
    compile_asm_file(filename)

for lc911 in listC:
    filename = f"Prints\\Assembly\\{sanitize_filename(lc911)}.asm"
    write_asm_file(lc911, filename)
    compile_asm_file(filename)

for sc in special_chars:
    if sc == " ":
        filename = f"Prints\\Assembly\\SPACE.asm"
    elif sc == "\n":
        filename = f"Prints\\Assembly\\NEWLINE.asm"
    else:
        filename = f"Prints\\Assembly\\{sanitize_filename(sc)}.asm"
    write_asm_file(sc, filename)
    compile_asm_file(filename)
