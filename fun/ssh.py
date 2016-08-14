#-*- coding: utf-8 -*-

import paramiko

my_host = "115.29.52.104"
my_username = "root"
my_password = "CHh314159"
#上传文件
def uploading(filename):
    t = paramiko.Transport((my_host,22))

    t.connect(username = my_username, password = my_password)

    sftp = paramiko.SFTPClient.from_transport(t)
    # /usr/share/tomcat/webapps
    remotepath = '/usr/share/tomcat/webapps/' + filename

    localpath ='C:/Users/Administrator/Desktop/' + filename

    sftp.put(localpath,remotepath)

    t.close()
    print 'upload success!'

# 执行命令
def execute_command(my_command):
    
    #复制
    #my_command = "cp /usr/nebula/test.txt /usr/nebula/test2.txt"
    #删除文件夹和文件
    #my_command = "rm -rf /usr/nebula/test1.txt"
    #
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(my_host,22,my_username, my_password)

    stdin, stdout, stderr = ssh.exec_command(my_command)

    result = stdout.readlines()
    
    ssh.close()

    print 'execute command success!'

    return result

#下载文件
def download_file():
    t = paramiko.Transport((my_host,22))

    t.connect(username = my_username, password = my_password)

    sftp = paramiko.SFTPClient.from_transport(t)

    remotepath='/usr/nebula/test.txt'

    localpath='D:/test1.txt'

    sftp.get(remotepath, localpath)

    t.close()

    print 'download file success!'


result = execute_command("cd /usr/share/tomcat/webapps ; ls")
for re in result:
    print re
    if u'community.war\n'==re:
        print "begin execute delete execute command ..."
        execute_command("rm -rf /usr/share/tomcat/webapps/community.war")
        execute_command("rm -rf /usr/share/tomcat/webapps/community")
        print "delete execute command done"

        print "begin execute upload execute command ..."
        uploading("community.war")
        print "upload execute command done"
#download_file()

x = input("done: ") 




    
