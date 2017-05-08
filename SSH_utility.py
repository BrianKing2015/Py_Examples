import paramiko
import argparse

def sshLog (host, user, passwrd, doc, target):
	'''
	Uses paramiko lib to contact another computer and read a file.
	Opens an SSH connection, looks at a specific file and checks line by line for certain words.
	Return type is a list of strings.
	'''
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname = host, username = user, password = passwrd)
	sftp_client = client.open_sftp()
	remote_file = sftp_client.open(doc)
	targetText = []
	for line in remote_file:
		if target in line:
			targetText.append (line.rstrip())

	remote_file.close()
	client.close()

	return targetText

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-ip', action ='store', dest = 'host', help='Input the host ip address')
	parser.add_argument('-u', action='store', dest = 'user', default = 'root', help= 'Input the user name for the destination system')
	parser.add_argument('-p', action='store', dest = 'passwrd', default = 'playerpass', help= 'Provide the password for the username provided above')
	parser.add_argument('-d', action='store', dest = 'doc', help= 'Give the full path to the target document')
	parser.add_argument('-t', action='store', dest = 'target', help= 'Input the full or partial text to search for')
	
	results = parser.parse_args()
	
	try:
		logOut = sshLog(results.host, results.user, results.passwrd, results.doc, results.target)
		for line in logOut: 
			print (line)

	except IOError:
		print ('No such file is accessible, check path and IP Address.')