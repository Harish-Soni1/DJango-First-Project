from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):

    myText = request.POST.get('text', 'default')
    isPuncOn = request.POST.get('puncRemover', 'off')
    isSpaceOn = request.POST.get('extraSpaceRemover', 'off')
    isUpperOn = request.POST.get('applyUpper', 'off')
    isLineOn = request.POST.get('newLineRemover', 'off')

    if isPuncOn == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in myText:
            if char not in punctuations:
                analyzed = analyzed + char

        myText = analyzed

    if isSpaceOn == 'on':
        analyzed = ""
        for index, char in enumerate(myText):
            try:
                if not(myText[index] == " " and myText[index+1]==" "):
                    analyzed = analyzed + char
            except:
                pass
        myText = analyzed

    if isUpperOn == 'on':
        analyzed = ""
        for char in myText:
            analyzed = analyzed + char.upper()

        myText = analyzed

    if isLineOn == 'on':
        analyzed = ""
        for char in myText:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        myText = analyzed

    if (isPuncOn != 'on' and isSpaceOn != 'on' and 
        isLineOn != 'on' and isUpperOn != 'on'): 
        return render(request, 'analyze.html', {'purpose': "Text-Utils", "analyzed_text": "Error"})

    else:
        return render(request, 'analyze.html', {'purpose': "Text-Utils", "analyzed_text": myText})


