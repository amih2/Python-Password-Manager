import os 
import subprocess

class Superuser:
	
	
	def is_root(self):
		return os.geteuid() == 0

	def mkdir(self, dir):
		return os.mkdir(dir)

	def chmod(self, dir, mod):
		return os.chmod(dir, mod)

	def chown(self, dir,uid, gid):
		return os.chown(dir, uid, gid)



