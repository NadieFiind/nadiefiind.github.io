__BRYTHON__.use_VFS = true;
var scripts = {"$timestamp": 1671538283940, "index": [".py", "from pyfyre import render,Style\nfrom pyfyre.nodes import *\nfrom components import Background\nfrom pages import Home,Services\ndef page_builder(main):\n def route_builder(arg):return Element('div',lambda :[Background(),main(),Link('https://twitter.com/adityar51253736/status/1584827745112317953?t=0518MJBJHHmQZxub23fPhA&s=19',lambda :[Text('Background by Aditya')],styles=[Style(position='fixed',bottom='0',right='5px',font_family='Syne Mono',opacity='0.5',font_size='1rem',z_index='2000')],attrs={'target':'_blank'})],styles=[Style(padding_bottom='70px')])\n return route_builder\nrender({'/':page_builder(Home),'/services':page_builder(Services)})\n", ["components", "pages", "pyfyre", "pyfyre.nodes"]]}
__BRYTHON__.update_VFS(scripts)
