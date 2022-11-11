from pyfyre import PRODUCTION, Style, MediaQuery

mq_mobile = MediaQuery("(max-height: 720px)")

debug = Style(border="1px solid red") if not PRODUCTION else Style()
centerx = Style(position="relative", left="50%", transform="translateX(-50%)")
