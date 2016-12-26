import paramiko

class local_sftp_digitalocean():
    def __init__(self, username, password, host, port):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def open_connection(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username = self.username, password = self.password)
        return paramiko.SFTPClient.from_transport(transport)
        print 'Connection created Succesfully!'

    def download_file(self, remotefile, localfile):
        """
        Simple method to download files from remote digitalocean server.
        upload_file(remotefile, localfile)
        """
        try:
            connection = self.open_connection()
            connection.get(remotefile, localfile)
        except Exception, e:
            print 'File could not be downloaded, errormessage:\n', e
            print e
        else:
            print 'File download completed!'
        connection.close()

    def upload_file(self, localfile, remotefile):
        """
        Simple method to upload files to remote digitalocean server.
        upload_file(localfile, remotefile)
        """
        
        try:
            connection = self.open_connection()
            connection.put(localfile, remotefile)
        except Exception, e:
            print 'File could not be uploaded, errormessage:\n', e
        else:
            print 'File upload completed!'       
        connection.close()

if __name__ == '__main__':
    #sftp = local_sftp_digitalocean('username','passw','serveradress', port (often 22))
    #sftp.download_file('path','file')
    #sftp.upload_file(localfile,remotefile)
    print 'Done.'
















