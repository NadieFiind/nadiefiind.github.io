__BRYTHON__.use_VFS = true;
var scripts = {"$timestamp": 1668274764888, "index": [".py", "from pyfyre import render\nfrom pyfyre.nodes import *\nfrom pages import Home,About,Skills,Projects\nfrom components import Background,Nav,SurpriseMessage\ndef page_builder(main):return lambda :Element('div',lambda :[Background(),main,Nav(),SurpriseMessage()])\nrender({'/':page_builder(Home()),'/about':page_builder(About()),'/skills':page_builder(Skills()),'/projects':page_builder(Projects())})\n", ["components", "pages", "pyfyre", "pyfyre.nodes"]]}
__BRYTHON__.update_VFS(scripts)
