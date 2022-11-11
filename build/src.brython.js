__BRYTHON__.use_VFS = true;
var scripts = {"$timestamp": 1668156068993, "index": [".py", "from pyfyre import render\nfrom pyfyre.nodes import *\nfrom widgets import Background\nfrom home import Home\nfrom about import About\nclass HomePage(Widget):\n def build(self):return [Background(),Home()]\nclass AboutPage(Widget):\n def build(self):return [Background(),About()]\nrender({'/':lambda :HomePage(),'/about':lambda :AboutPage()})\n", ["about", "home", "pyfyre", "pyfyre.nodes", "widgets"]]}
__BRYTHON__.update_VFS(scripts)
