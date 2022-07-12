import io
import base64
from chickpy.processor import Command

chart_container = Element("chart-container")
chart_script = Element("new-chart-script")


def create_chart_event(e):
    if e.key == "Enter":
        create_chart()


def create_chart(*ags, **kws):
    input = chart_script.element.value
    try:
        fig = Command.render(f"""{input}""")
        string_io_bytes = io.BytesIO()
        fig.savefig(string_io_bytes, format="png")
        image = (
            base64.b64encode(string_io_bytes.getvalue())
            .decode("utf-8")
            .replace("\n", "")
        )
        chart_content = chart_container.select("p")
        chart_content.element.innerHTML = f'<img src="data:image/png;base64,{image}">'
    except Exception as e:
        chart_content = chart_container.select("p")
        chart_content.element.innerHTML = f"<code>{str(e)}</code>"


chart_script.element.onkeypress = create_chart_event
