from motion_detector import df
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, ColumnDataSource

cds = ColumnDataSource(df)
p = figure(x_axis_type = "datetime", width = 500, height = 250, sizing_mode = "stretch_both")
p.title.text = "Motion Graph"
p.title.text_color = "black"
p.title.text_font = "arial"
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1
hover = HoverTool(
    tooltips = [
        ("Start", "@Start{%Y-%m-%d %H:%M:%S}"),
        ("End", "@End{%Y-%m-%d %H:%M:%S}")
    ],
    formatters = {
        "@Start" : "datetime",
        "@End" : "datetime"
    }
)
p.add_tools(hover)
q = p.quad(left = "Start", right = "End", top = 0, bottom = 1, color = "green", source =cds)
output_file("Graph.html")
show(p)
