from pyfyre import PRODUCTION, Style, MediaQuery

mq_mobile = MediaQuery("(max-width: 720px)")

debug = Style(border="1px solid red") if not PRODUCTION else Style()
head_style = Style(font_wight="bold", font_family="Open Sans", font_size="3rem")
centerx = Style(position="relative", left="50%", transform="translateX(-50%)")
