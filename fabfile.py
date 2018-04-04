from fabric.api import local
from fabric.decorators import task

def hello():
	"""
	Test Fabric framework
	"""
	print("hello world")


@task
def install():
	"""
	Install requirements packages
	"""
	local("pip install -r requirements.txt")

#def install(requirements_env="dev"):
#	local("pip install -r requirments/%s.txt" % requirements_env)
@task
def runserver():
	"""
	Run Django server
	"""
	local("python manage.py runserver")

@task
def pep8():
	"""Check the project for PEP8 compliance using `pep8`"""
	local("pep8 .")

@task
def tag_version(version):
	"""
	Tag New Version
	"""
	local("git tag %s" % version)
	local("git push origin %s" % version)
	