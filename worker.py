import os
import time
import stat
import sys
directory = os.getcwd()

def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)     

repo_name = input('input project name (press enter to continue with directory name) : ')
if repo_name.strip() == '':
    repo_name = os.path.split(directory)[1]
input(f"project name : {repo_name} , press enter to continue.")

# dir name
os.rename(os.path.join(directory , 'repo_name') , os.path.join(directory , repo_name))

# tests/test_import.py
with open(os.path.join(directory , 'tests/test_import.py') , 'r+' , encoding='utf-8') as f:
    out = list(map(lambda x:x.replace('repo_name' , repo_name) , f.readlines()))
with open(os.path.join(directory , 'tests/test_import.py') , 'w' , encoding='utf-8') as f:
    f.writelines(out)

# README.md
with open(os.path.join(directory , 'README.md') , 'r+' , encoding='utf-8') as f:
    out = list(map(lambda x:x.replace('bare_pypi_init_update' , repo_name) , f.readlines()))
with open(os.path.join(directory , 'README.md') , 'w' , encoding='utf-8') as f:
    f.writelines(out)

# docs/README.md
with open(os.path.join(directory , 'docs/README.md') , 'r+' , encoding='utf-8') as f:
    out = list(map(lambda x:x.replace('bare_pypi_init_update' , repo_name) , f.readlines()))
with open(os.path.join(directory , 'docs/README.md') , 'w' , encoding='utf-8') as f:
    f.writelines(out)

# docs/source/conf.py
with open(os.path.join(directory , 'docs/source/conf.py') , 'r+' , encoding='utf-8') as f:
    out = list(map(lambda x:x.replace('bare_pypi_init_update' , repo_name) , f.readlines()))
with open(os.path.join(directory , 'docs/source/conf.py') , 'w' , encoding='utf-8') as f:
    f.writelines(out)

# docs/source/index.rst
with open(os.path.join(directory , 'docs/source/index.rst') , 'r+' , encoding='utf-8') as f:
    out = list(map(lambda x:x.replace('bare_pypi_init_update' , repo_name) , f.readlines()))
with open(os.path.join(directory , 'docs/source/index.rst') , 'w' , encoding='utf-8') as f:
    f.writelines(out)

# docs/source/index.rst
with open(os.path.join(directory , 'requirements.txt') , 'r+' , encoding='utf-8') as f:
    out = list(map(lambda x:x.replace('bare_pypi_init_update' , repo_name) , f.readlines()))
with open(os.path.join(directory , 'requirements.txt') , 'w' , encoding='utf-8') as f:
    f.writelines(out)


# docs/source/_templates/sidebarlinks.html
with open(os.path.join(directory , 'docs/source/_templates/sidebarlinks.html') , 'r+' , encoding='utf-8') as f:
    out = list(map(lambda x:x.replace('bare_pypi_init_update' , repo_name) , f.readlines()))
with open(os.path.join(directory , 'docs/source/_templates/sidebarlinks.html') , 'w' , encoding='utf-8') as f:
    f.writelines(out)

# docs/source/api_manual/moduleinterface.rst
with open(os.path.join(directory , 'docs/source/api_manual/moduleinterface.rst') , 'r+' , encoding='utf-8') as f:
    out = list(map(lambda x:x.replace('bare_pypi_init_update' , repo_name) , f.readlines()))
with open(os.path.join(directory , 'docs/source/api_manual/moduleinterface.rst') , 'w' , encoding='utf-8') as f:
    f.writelines(out)

# docs/source/user_guide/quickstart.rst
with open(os.path.join(directory , 'docs/source/user_guide/quickstart.rst') , 'r+' , encoding='utf-8') as f:
    out = list(map(lambda x:x.replace('bare_pypi_init_update' , repo_name) , f.readlines()))
with open(os.path.join(directory , 'docs/source/user_guide/quickstart.rst') , 'w' , encoding='utf-8') as f:
    f.writelines(out)

# docs/source/licence.rst
with open(os.path.join(directory , 'docs/source/license.rst') , 'r+' , encoding='utf-8') as f:
    out1 = f.readlines()
if os.path.exists('LICENSE'):
    with open(os.path.join(directory , 'LICENSE') , 'r+' , encoding='utf-8') as f:
        out2 = f.readlines()
    out1.extend(out2)
with open(os.path.join(directory , 'docs/source/license.rst') , 'w' , encoding='utf-8') as f:
    f.writelines(out1)

# setup.py
with open(os.path.join(directory , 'setup.py') , 'r+' , encoding='utf-8') as f:
    out = list(map(lambda x:x.replace('repo_name' , repo_name) , f.readlines()))
with open(os.path.join(directory , 'setup.py') , 'w' , encoding='utf-8') as f:
    f.writelines(out)

r1 = os.system('python setup.py sdist bdist_wheel')
r2 = os.system('twine upload dist/*')

setup_cont = f'''
from setuptools import setup, find_packages
from requests import get as rget
from bs4 import BeautifulSoup
import logging , sys
# init logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
sh = logging.StreamHandler(stream=sys.stdout) 
format = logging.Formatter("%(message)s")#("%(asctime)s - %(message)s") 
sh.setFormatter(format)
logger.addHandler(sh)

#
def get_install_requires(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    return [x.strip() for x in lines]

# 
url = 'https://github.com/GoodManWEN/{repo_name}'
release = f'{{url}}/releases/latest'
headers = {{
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
}}

html = BeautifulSoup(rget(url , headers).text ,'lxml')
description = html.find('meta' ,{{'name':'description'}}).get('content')
for kw in (' - GitHub', ' - GoodManWEN'):
    if ' - GitHub' in description:
        description = description[:description.index(' - GitHub')]
html = BeautifulSoup(rget(release , headers).text ,'lxml')
logger.info(f"description: {{description}}")

#
with open('tagname','r',encoding='utf-8') as f:
    version = f.read()
if ':' in version:
    version = version[:version.index(':')].strip()
version = version.strip()
logger.info(f"version: {{version}}")

#
with open('README.md','r',encoding='utf-8') as f:
    long_description_lines = f.readlines()

long_description_lines_copy = long_description_lines[:]
long_description_lines_copy.insert(0,'r"""\\n')
long_description_lines_copy.append('"""\\n')

# update __init__ docs
with open('{repo_name}/__init__.py','r',encoding='utf-8') as f:
    init_content = f.readlines()

for line in init_content:
    if line == "__version__ = ''\\n":
        long_description_lines_copy.append(f"__version__ = '{{version}}'\\n")
    else:
        long_description_lines_copy.append(line)

with open('{repo_name}/__init__.py','w',encoding='utf-8') as f:
    f.writelines(long_description_lines_copy)

setup(
    name="{repo_name}", 
    version=version,
    author="WEN",
    description=description,
    long_description=''.join(long_description_lines),
    long_description_content_type="text/markdown",
    url="https://github.com/GoodManWEN/{repo_name}",
    packages = find_packages(),
    install_requires = get_install_requires('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Framework :: AsyncIO',
    ],
    python_requires='>=3.7',
    keywords=["{repo_name}" ,]
)
'''
if r1 != 0 or r2 != 0:
    sys.exit(1)
with open(os.path.join(directory , 'setup.py') , 'w' , encoding='utf-8') as f:
    f.write(setup_cont)

time.sleep(2)
rmtree(os.path.join(directory , f'build'))
rmtree(os.path.join(directory , f'dist'))
rmtree(os.path.join(directory , f'{repo_name.replace("-","_")}.egg-info'))

os.remove(os.path.join(directory , 'init_&_upload_&_init.cmd'))
os.remove(os.path.join(directory , 'worker.py'))

os.system("git add -A")
os.system("git status")
os.system('git commit -m "Init"')
os.system('git push')
input("\nRepo is now up to date.")
