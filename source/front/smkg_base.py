from flask.views import MethodView, View


class BaseView(MethodView):
    def __init__(self):
        super(BaseView).__init__()
