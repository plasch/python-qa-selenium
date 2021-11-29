from .CommonSelectors import css, partial_link, link_text


class MainPage:
    class menu:
        class desktops:
            link = (link_text, "Desktops")
            show_all = (partial_link, "Show All Desktops")

    promoblock = (css, "#slideshow0")
