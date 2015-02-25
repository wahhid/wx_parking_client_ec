import xmlrpclib

class Openerp():
	
	def __init__(self,parent):
		self.dbname = 'parking'
		
	def sock_common(self):
	    return xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
		
	def sock_object(self):
		return xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
		
	def auth(self,username,password):
		sock_common = self.sock_common()		
		return sock_common.login(self.dbname,username,password)