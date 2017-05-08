import SSH_utility
import pytest
import paramiko



def test_posSSHLog():
	''' Simple test to check positive outcome, the function found something at the location
	'''
	example = SSH_utility.sshLog('192.168.0.0', 'root', 'root', '/home/root/Documents/randomlog.txt','err')
	assert len (example) > 1

def test_negSSHLog():
	''' Test to check the negative outcome
	'''
	example = SSH_utility.sshLog('192.168.0.0', 'root', 'root', '/home/root/Documents/randomlog.txt','I am the very model of a modern major general')
	assert len (example) == 0

def test_valueSSHLog():
	''' Checking to make sure the value is an exact match, may want to drop this or modify for ease of upkeep
	'''
	example = SSH_utility.sshLog('192.168.0.0', 'root', 'root', '/home/root/Documents/randomlog.txt','err')
	assert example[0] == "[2017, 3, 7, 22, 14, 55, 742306] error unknown origin"

def test_noFile():
	'''Giving an incorrect file location and testing to make sure it raises the right type of error
	'''
	with pytest.raises(FileNotFoundError):
		example = SSH_utility.sshLog('192.168.0.0', 'root', 'root', '/home/nonexistentFile.txt', 'Nothing')

def test_noConnect():
	''' Giving an incorrect IP Address and checking that it raises the right error
	'''
	with pytest.raises(paramiko.ssh_exception.NoValidConnectionsError):
		example = SSH_utility.sshLog('192.168.2.16', 'root', 'root', '/home/nonexistentFile.txt', 'Nothing')

def test_wrongUser():
	''' Giving the wrong username and checking the error
	'''
	with pytest.raises(paramiko.ssh_exception.AuthenticationException):
		example = SSH_utility.sshLog('192.168.0.0', 'tim', 'root', '/home/nonexistentFile.txt', 'Nothing')