from routes.shorten import shortenerRoute


def configRoutes(app):
    app.register_blueprint(shortenerRoute)
