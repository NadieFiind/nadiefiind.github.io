from pyfyre import Style

debug = Style()  # if PRODUCTION else Style(border="1px solid red")
title_style = Style(font_weight="bold", font_family="Open Sans", font_size="3rem")
center_x = Style(position="relative", left="50%", transform="translateX(-50%)")
center_y = Style(position="relative", top="50%", transform="translateY(-50%)")
center_xy = Style(
    position="absolute",
    top="50%",
    left="50%",
    transform="translate3d(-50%, -50%, 0)",
)
