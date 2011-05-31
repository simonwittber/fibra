from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis

import timeit
import gc

results = dict()
RANGE = range(0, 100000, 10000)[1:]
for lib in "stacklessb", "fibrab", "kamaeliab":
    results[lib] = eval(open("%s.results"%lib).read())

# Set the vertical range from 0 to 100
max_y = max(max(i) for i in results.values())  * 1.1
print max_y

# Chart size of 200x125 pixels and specifying the range for the Y axis
chart = SimpleLineChart(400, 300, y_range=[0, max_y])

chart.set_colours(['0000FF', "00FF00", "FF0000", "FFFF00"])
print sorted(results.keys())
for k in sorted(results.keys()):
    data = results[k]
    chart.add_data(data)

# Set the vertical stripes
chart.fill_linear_stripes(Chart.CHART, 0, 'CCCCCC', 0.2, 'FFFFFF', 0.2)

# Set the horizontal dotted lines
chart.set_grid(0, 25, 5, 5)

# The Y axis labels contains 0 to 100 skipping every 25, but remove the
# first number because it's obvious and gets in the way of the first X
# label.
left_axis = range(0, (max_y*1000), 1000)
left_axis[0] = ''
chart.set_axis_labels(Axis.LEFT, left_axis)

# X axis labels
chart.set_axis_labels(Axis.BOTTOM, [i/100 for i in RANGE])

chart.download('line-stripes.png')
