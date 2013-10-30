import morepath
import waitress

app = morepath.App()


@app.root()
class Root(object):
    pass


class Model(object):
    def __init__(self, id):
        self.id = id


@app.model(model=Model, path="{id}",
           variables=lambda model: {'id': model.id})
def get_model(id):
    return Model(id)


@app.resource(model=Root, render=morepath.render_html)
def root_default(request, model):
    result = []
    for i in range(10):
        result.append(
            '<p><a href="%s">Link to %s</a></p>' % (request.link(Model(i)),
                                                    i))
    return ''.join(result)
            

@app.resource(model=Model, render=morepath.render_html)
def model_default(request, model):
    return '<p>I am the model: %s</p>' % model.id


def main():
    morepath.setup()
    config = morepath.Config()
    import mpdemo
    config.scan(mpdemo)
    config.app(app)
    config.commit()
    
    waitress.serve(app)
    
