from taipy.gui import Gui
from pages.home import page as homepage
from pages.CO2_src_chart import page as co2page
from pages.CO2_map import page as CO2countrypage
import taipy.gui.builder as tgb

footer_text = "Powered by Taipy | Climate Insights Dashboard"

root_md = f"""
<|navbar|class_name=modern-navbar|>
<|content|>
<div class="footer-layout">{footer_text}</div>
"""

pages = {
    "/": root_md,
    "home": homepage,
    "CO2_Sources": co2page,
    "CO2_by_Country": CO2countrypage,
}

# Enable dark mode and customize theme
Gui(pages=pages).run(
    dark_mode=True, 
    title="Climate Emissions Dashboard",
    use_reloader=True,
    run_browser=False,
    host="0.0.0.0",
    port=3000,
    css_file="styles.css"
)