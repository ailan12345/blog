from django.shortcuts import render



def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    html = '''
    gbhjknjkl;k
    
    '''
    context = {'like':'1361141323'}
    return render(request, 'main/main.html', context)


def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')


