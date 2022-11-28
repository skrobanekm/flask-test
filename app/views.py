import logging

from flask_appbuilder.charts.views import (DirectChartView)

from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from flask_appbuilder.charts.views import (
    DirectByChartView
)


from . import appbuilder
from .models import Datas

log = logging.getLogger(__name__)

class Data(ModelView):
    datamodel = SQLAInterface(Datas)
    list_columns = ["id", "cislo"]

class DatasView(DirectByChartView):
    datamodel = SQLAInterface(Datas)
    chart_title = "Data"

    definitions = [
        {
            "group": "id",
            "series": ["cislo"],
        }
    ]

appbuilder.add_view(
    DatasView,
    "Chart",
    icon="fa-dashboard",
    category="Datas",
)
appbuilder.add_view(
    Data,
    "Data",
    icon="fa-dashboard",
    category="Datas",
)