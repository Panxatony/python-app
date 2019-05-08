from sampleapp import myapp

@myapp.route('/')
def helloworld():
    return 'Hello Again - Prod Stage - Release v1.0.0!'
