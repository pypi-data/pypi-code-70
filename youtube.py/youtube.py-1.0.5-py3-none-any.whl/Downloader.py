# -*- coding: utf-8 -*-

__author__ = 'Mayank Gupta'
__version__ = '1.1'
__license__ = 'License :: MIT License'

from typing import Union, Callable
from typing import List, Tuple
from typing import Dict, Type
from typing import Any, Optional
import socket,select,re,ssl,threading,sys,os
from urllib.parse import urlparse, unquote
from time import sleep, time
import tempfile, os, logging
from select import select
from random import randint

logg = logging.getLogger(__name__)

class Download(object):
	'''
	This :class:`Download <Download>` will download streams with multi-connections.

	:param str url: 
		Pass the download link
	:param str name: 
		(optional) Pass the name of file name. 
	:param str dire: 
		(optional) Pass the dir for output file with excluding filename.
	:param bool status: 
		(optional) Pass if you want to enable process bar. **Default[False]**
	:param int connection: 
		(optional) Pass number is connection to be create. **Default[8]**
	:param int chunk: 
		(optional) Pass the chunk/buffer size for accepting packets. **Default[5120]**

	:rtype: str
	:returns: the file name

	'''
	def __init__(self,url:str,dire:str="",name:str="",status:bool=False,connection:int=8, chunk:int = 5120) -> None:
		self.name = name.replace(" ","_")
		self.dire = dire
		if self.dire:
			self.dire = self.create_user_dir(dire)
			if self.dire[-1] == "/":
				self.dire = self.dire[:-1]
		self.status = status
		self.chunk = chunk
		self.connection = connection
		self.url = unquote(url)

	def start(self) -> str:
		'''
		Start will fire up the downloading
		'''
		protocol, url, host =self.RawData(self.url)
		logg.debug(f'protocol: {protocol}, host: {host}')

		check = self.check_multi(protocol, self.url, host)
		logg.debug(f'Download check status: {check}')
		if check[0] == "0":

			# Data for process bar
			# gg= bytes downloaded, size total size of file,
			# when is bool vaule to start and stop the process bar
			self.size = int(self.header["content-length"]) 
			self.gg = 0 # download bytes
			self.when = True

			#get filename
			name = self.getfilename()
			logg.debug(f'Filename: {name}, Filesize: {self.size}')

			# Create ranges for downloading chunks in parts
			ranges = self.get_range(int(self.header["content-length"]),self.connection)

			self.files = {}
			threads = []
			for n,m in enumerate(ranges):
				req=self.gen_req(host,url,{"range":f"bytes={m}"})
				threads.append(threading.Thread(target=self.down, args=(protocol, host, req, m, str(n))))
				# break
			if self.status:threading.Thread(target=self.run).start()
			for n in threads:n.start()
			for n in threads:n.join()
			
			# End of process bar 
			self.when = False

			with open(name,"wb") as f:
				for n in range(len(self.files)):
					ff=self.files[n]
					ff.seek(0)
					f.write(ff.read())
					ff.close()
			f.close()

			# end of procedd bar with 100%
			p=int(int(self.gg)*50/int(self.size))
			if self.status:print("Process: [{}] {}% Complete {:<10}".format("█"*p+"-"*(50-p), p*100/50,"0.0 Kb/s"))
			logg.debug(f"Downloading conpleted 100% Filename{name}")

			# print(name)
			return name

		elif check[0] == "1" :
			name = self.getfilename()
			req=self.gen_req(host,url)
			sock=self.connect(protocol,host)
			sock.sendall(req)
			data=sock.recv(self.chunk)
			header,image=self.hparsec(data)
			f = open(name,"wb")
			f.write(image)


			# gg= bytes downloaded, size total size of file,
			# when is bool vaule to start and stop the process bar
			self.gg = len(image)
			self.size = int(header["content-length"]) 
			self.when = True

			#Start The process bar if status TRUE
			if self.status:threading.Thread(target=self.run).start()

			logg.debug(f'Filename: {name}, Filesize: {self.size}')

			while True:
				try:
					data = sock.recv(self.chunk)
					if not data:break
					f.write(data)
					self.gg += len(data)
				except socket.timeout:
					break

			#End od process bar
			self.when = False

			# end of procedd bar with 100%
			p=int(int(self.gg)*50/int(self.size))
			if self.status:print("Process: [{}] {}% Complete {:<10}".format("█"*p+"-"*(50-p), p*100/50,"0.0 Kb/s"))

			# Return the file name
			return name
		else:
			return check[1]

	def create_user_dir(self,foldername:str) -> str:
		if not os.path.exists(foldername):
			os.makedirs(foldername)
		return foldername

	def rangediff(self,s):
		c,b = s.split("-")
		c,b = int(c),int(b)
		if self.size == b:
			diff = b-c
			return diff
		else:
			diff = b-c
			return diff+1

	def down(self, protocol:str, host:str, req:bytes, range:list, id:str="") -> None:
		f = tempfile.TemporaryFile()
		if id is not "":self.files[int(id)] = f
		sock=self.connect(protocol,host)
		diff = self.rangediff(range)
		sock.settimeout(5)
		sock.sendall(req)
		data=sock.recv(self.chunk)
		header,image=self.hparsec(data)
		self.gg += len(image)
		local_gg = 0
		local_gg =+len(image)
		f.write(image)
		while True:
			try:
				data = sock.recv(self.chunk)
				if not data:break
				f.write(data)
				self.gg += len(data)
				local_gg =+len(data)
				if local_gg >= diff: break
			except socket.timeout:
				break

		f.seek(0)

	def run(self):
		self.temp1=0
		while self.when:
			speed=(self.gg-self.temp1)/1024
			p=int(int(self.gg)*50/int(self.size))
			print("Process: [{}] {}% Complete {:<8}Kb/s".format("█"*p+"-"*(50-p), p*100/50,"{:.2f}".format(speed)),end="\r")
			self.temp1=self.gg
			sleep(1)

	def get_range(self, length:int, conn:int) -> List[str]:
		av = int(length/conn)
		r=[]
		start = 0
		r.append(f'{start}-{start+av}')
		start+=av
		if conn>1:
			for n in range(conn-2):
				r.append(f'{start+1}-{start+av}')
				start+=av
			r.append(f'{start+1}-{length}')
		return r

	def getfilename(self) -> str:
		finalname = ""
		name = ""
		if self.dire:
			if not self.name:
				if self.tmpname:
					finalname = f'{self.dire}/{randint(10,99)}{self.tmpname}'
				else:
					dd=self.header["content-type"].split("/")[1].split("+")[0]
					finalname = f'{self.dire}/{randint(10,99)}{int(time())}.{dd}'
			finalname = f'{self.dire}/{randint(10,99)}{self.name}'
		else:
			if not self.name:
				if self.tmpname:
					finalname = f'{randint(10,99)}{self.tmpname}'
				else:
					dd=self.header["content-type"].split("/")[1].split("+")[0]
					finalname = f'{randint(10,99)}{int(time())}.{dd}'
			finalname = f'{randint(10,99)}{self.name}'

		for n in finalname:
			if n not in '\\ /:*?"<>|':
				name+=n
				
		return name

	def check_multi(self, protocol:str, url:str, host:str) -> str:
		req=self.gen_req(host,url)
		sock=self.connect(protocol,host)
		sock.sendall(req)
		data=sock.recv(self.chunk)
		self.header,image=self.hparsec(data)
		if int(self.header["status"]) is not 200:
			try:
				sock.close()
				name = self._Download(self.header["location"], dire=self.dire, name=self.name, status=self.status, chunk=self.chunk, connection=self.connection)
				return "2",name
			except Exception as err:
				print(f"Error: {err}")
				print("We cant download from this URL Contact Admin with URL OR can't save with this file name")
				sock.close()
				sys.exit(1)

		if "accept-ranges" in self.header.keys():
			return "0",""
		return "1",""
	
	@classmethod
	def _Download(cls,*args,**kwargs):
		return cls(*args,**kwargs).start()


	def connect(self, protocol:str, host:str) -> socket.socket:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if protocol=="https":
			s.connect((host, 443))
			s = ssl.create_default_context().wrap_socket(s, server_hostname=host)
		elif protocol=="http":
			s.connect((host, 80))
		else:
			print("we only support HTTP and HTTPS")
			s.close()
			sys.exit(1)
		return s

	def hparsec(self,data:bytes) -> Tuple[Dict[str,str], bytes]:
		header =  data.split(b'\r\n\r\n')[0]
		store =  data[len(header)+4:]
		html = data[len(header)+4:]
		header=header.decode().split("\r\n")
		out={}
		out["status"]=header[0].split()[1]
		for n in header[1:]:
			temp=n.split(":")
			value=""
			for n in temp[1:]:
				value+=n+":"
			out[temp[0].lower()]=value[1:len(value)-1]
		return out,store

	def gen_req(self, host:str, url:str, header:Dict[str,str] = {}) -> bytes:
		req=f'GET {url} HTTP/1.1\r\nhost: {host}\r\nuser-agent: MayankFawkes/bot\r\nconnection: close\r\n'
		for n, m in header.items():
			req += f'{n}:{m}\r\n'
		req+="\r\n"
		return req.encode()

	def RawData(self,web_url:str)-> Tuple[str, str, str]:
		o=urlparse(web_url)
		host=o.netloc
		protocol=o.scheme
		if o.query:
			url=(o.path+"?"+o.query)
			self.tmpname = ""
		else:
			url=o.path
			self.tmpname = o.path.split("/")[-1]
		return protocol, url, host

if __name__ == '__main__':
	# link=input("Enter Url -->")
	link='https://storge.pic2.me/download/origin/257714.jpeg'
	# link="https://r2---sn-ci5gup-civl.googlevideo.com/videoplayback?expire=1606610611&ei=U5rCX9fZKImlwgPP0KOwDQ&ip=171.60.177.128&id=o-AOTEor8QB7nEzOV58ZY1GegCDzqGoCJFH4yqW6Scpeqh&itag=248&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=DC&mm=31%2C29&mn=sn-ci5gup-civl%2Csn-ci5gup-cvh6&ms=au%2Crdu&mv=m&mvi=2&pcm2cms=yes&pl=20&gcr=in&initcwndbps=695000&vprv=1&mime=video%2Fwebm&ns=vUXVdwbvoJzjIECjxScz6IUF&gir=yes&clen=12295247&dur=193.680&lmt=1606586572289453&mt=1606588849&fvip=2&keepalive=yes&c=WEB&txp=5532432&n=y9n0dSPriQCxsQyupR2&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPE6C_TL49N8jIqMp9hVgj9bqs8zY93wOjjW7ZONuFo2AiEA81M8BnT1W519Y90XZhYpaF0wmSMvFMSKNGhmggOcPdE%3D&sig=AOq0QJ8wRgIhAOAdoYf8jUSErCo7XlxjSb4ePQIYpS2IRzUaIW5_Fk0GAiEAgbqa68gBBkWUdml0tzts_dphR7JxQXSQ8C5AhQnV86s="
	# link="http://www.macaronisoup.com/songs/mp3/LoobyLoo.mp3"
	# link = "https://portswigger.net/burp/releases/download?product=community&version=2020.11.2&type=WindowsX64"
	dd=Download(link ,name = "", status = True, connection = 8, chunk = 5120).start()
	print(dd)