from taipy.gui import navigate
import taipy.gui.builder as tgb

def on_button_press(state, id):
    page_map = {
        "CO2": "co2_sources",
        "CO2Country": "co2_by_country"
    }
    navigate(state, to=page_map.get(id, "home"))

with tgb.Page() as page:
    tgb.text("# Climate Emissions Dashboard", mode='md', class_name="page-title")
    tgb.text("Explore comprehensive insights into global CO2 emissions and climate trends.", 
             mode='md', class_name="page-subtitle")
    
    with tgb.layout(columns="1 1", class_name="dashboard-grid"):
        with tgb.part(class_name="dashboard-card"):
            tgb.text("## CO2 Emissions by Source", mode='md', class_name="card-title")
            tgb.image("images/co2emissionspagesmall.png", class_name="card-image")
            tgb.button("Explore Sources", id="CO2", on_action=on_button_press, class_name="explore-button")
        
        with tgb.part(class_name="dashboard-card"):
            tgb.text("## CO2 Emissions by Country", mode='md', class_name="card-title")
            tgb.image("images/worldtemppagesmall.png", class_name="card-image")
            tgb.button("Explore Countries", id="CO2Country", on_action=on_button_press, class_name="explore-button")
