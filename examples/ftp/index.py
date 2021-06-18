from ftplib import FTP

# Работаем только с настроенной директорией
# https://linuxconfig.org/how-to-setup-ftp-server-on-ubuntu-20-04-focal-fossa-linux

HOST = "192.168.1.93"
USER = "ftpuser"
PASSWORD = "ftpuser"

ftp = FTP(host=HOST, user=USER, passwd=PASSWORD)

# Выводим список файлов
print(ftp.dir())

# Переходим в папку
ftp.cwd('files')
print(ftp.dir())

# # Скачиваем нужный файл
# with open('Example.py', 'wb') as fp:
#     ftp.retrbinary('RETR file.py', fp.write)

# # Создание папки
# # ftp.mkd('my_dir')
# # print(ftp.dir())
#
# Загружаем наш файл в эту папку
with open('logo.png', 'rb') as fp:
    ftp.storbinary('STOR logo.png', fp)

ftp.quit()
