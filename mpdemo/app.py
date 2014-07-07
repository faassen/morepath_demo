import morepath
import waitress


# the morepath application class contains configuration and its
# instance is a WSGI app
class app(morepath.App):
    pass


# the root path for the application
@app.path(path='')
class Root(object):
    pass


# individual model with id under root
class Model(object):
    def __init__(self, id):
        self.id = id


# publish model under root under {id}
@app.path(model=Model, path="{id}",
          variables=lambda model: {'id': model.id})
def get_model(id):
    return Model(id)


# the default view for the root is a list of links
# to models
@app.view(model=Root, render=morepath.render_html)
def root_default(self, request):
    result = []
    for i in range(10):
        result.append(
            '<p><a href="%s">ELLink to %s</a></p>' % (request.link(Model(i)),
                                                    i))
    return ''.join(result)


# the default view for a model
@app.view(model=Model, render=morepath.render_html)
def model_default(self, request):
    return '<p>I am the model: %s</p>' % self.id

@app.view(model=Model, request_method='POST', render=morepath.render_html)
def another_view(self, request):
    pass

class M(object):
    pass

@app.view(model=M, request_method='GET')
def get_test(self, request):
    pass

def main():
    # set up morepath's own configuration
    config = morepath.setup()
    # load application specific configuration
    config.scan()
    config.commit()

    # serve app as WSGI app
    waitress.serve(app())
