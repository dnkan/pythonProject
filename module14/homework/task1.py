import platform
import sys

# Информация о системе

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture()
)

print(info)

with open('OS_info.txt', 'w', encoding='utf8') as file:
    file.write(info)