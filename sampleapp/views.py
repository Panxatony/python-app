from sampleapp import myapp

@myapp.route('/')
def helloworld():
    return 'Hello Again - DEV Stage!'
