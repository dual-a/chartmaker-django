import io
from django.http import HttpResponse
import matplotlib

matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import json


def generate_chart(request):
    # Retrieve data labels and values from query parameters
    data_labels = request.GET.get("labels")
    data_values = request.GET.get("data1")

    if data_labels and data_values:
        data_labels = json.loads(data_labels)
        data_values = [float(value) for value in data_values.split(",")]
    else:
        data_labels = ["Label 1", "Label 2", "Label 3"]  # Default labels
        data_values = [4, 2, 7]  # Default values

    width_in_inches = request.GET.get("width")
    height_in_inches = request.GET.get("height")
    # Set the size of the plot
    width_in_inches = 720 / 96  # Convert pixels to inches
    height_in_inches = 180 / 96  # Convert pixels to inches

    # Create a chart using Matplotlib
    fig, ax = plt.subplots(figsize=(width_in_inches, height_in_inches))
    ax.bar(data_labels, data_values)

    # Adjust the bottom margin to prevent cutting off
    plt.subplots_adjust(bottom=0.2)

    # Save the chart to a buffer
    buffer = io.BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buffer)
    plt.close(fig)

    # Return the buffer as an image response
    return HttpResponse(buffer.getvalue(), content_type="image/png")
