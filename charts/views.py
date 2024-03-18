import io
from django.http import HttpResponse
import matplotlib

matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt


def generate_chart(request):
    # Create a chart using Matplotlib
    fig, ax = plt.subplots()
    ax.bar([1, 2, 3], [4, 2, 7])

    # Save the chart to a buffer
    buffer = io.BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buffer)
    plt.close(fig)

    # Return the buffer as an image response
    return HttpResponse(buffer.getvalue(), content_type="image/png")
