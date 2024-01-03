from html_template import HTML_Template

class Routes(): 
    def index_route() -> str:
        html_tokens = {}
        with open("./templates/nav.html") as nav_html:
            html_tokens["nav_bar"] = nav_html.read()
        with open("./templates/index.html") as index_html:
            html_tokens["content"] = index_html.read()
        html_tokens["Test"] = "Hopaaa"
        return HTML_Template("template.html", html_tokens).html_string
