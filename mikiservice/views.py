from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'mikiService'}

@view_config(route_name='listPostData', renderer='json', request_method='POST')
def listPostData(request):
    print request.POST
    return {'test': 'POST'}

@view_config(route_name='listGetData', renderer='json', request_method='GET')
def listGetData(request):
    print request
    print 'Hello Python!'
    return {'test': 'GET'}
