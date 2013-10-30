import morepath
import waitress


# the morepath application that contains configuration and is
# WSGI app
app = morepath.App()


# the root model for the application
@app.root()
class Root(object):
    pass


# individual model with id under root
class Model(object):
    def __init__(self, id):
        self.id = id


# publish model under root under {id}
@app.model(model=Model, path="{id}",
           variables=lambda model: {'id': model.id})
def get_model(id):
    return Model(id)


# the default resource for the root is a list of links
# to models
@app.resource(model=Root, render=morepath.render_html)
def root_default(request, model):
    result = []
    for i in range(10):
        result.append(
            '<p><a href="%s">Link to %s</a></p>' % (request.link(Model(i)),
                                                    i))
    return ''.join(result)


# the default resource for a model
@app.resource(model=Model, render=morepath.render_html)
def model_default(request, model):
    return '<p>I am the model: %s</p>' % model.id


def main():
    # set up morepath's own configuration
    morepath.setup()
    # load application specific configuration
    config = morepath.Config()
    import mpdemo
    config.scan(mpdemo)
    config.app(app)
    config.commit()

    # serve app as WSGI app
    waitress.serve(app)
