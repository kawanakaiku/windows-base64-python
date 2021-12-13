import subprocess

excludes="matplotlib scipy setuptools hook distutils site hooks tornado PIL PyQt4 PyQt5 pydoc pythoncom pytz pywintypes sqlite3 pyz pandas sklearn scapy scrapy sympy kivy pyramid opencv tensorflow pipenv pattern mechanize beautifulsoup4 requests wxPython pygi pillow pygame pyglet flask django pylint pytube odfpy mccabe pilkit six wrapt astroid isort future altgraph pip".split()

str = "pyinstaller base64.py --onefile " + " ".join(["--exclude " + x  for x in excludes])

subprocess.run(str.split())
