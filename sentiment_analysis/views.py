from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
from .preprocess_predict import predict_class, preprocess_text
 
def analyze_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        
        # Call the predict_class function to get the predicted class
        predicted_class = predict_class(text)

        # Map the predicted class to sentiment class
        if predicted_class == 5:
            sentiment_class = 'Strong Positive'
        elif predicted_class == 4:
            sentiment_class = 'Positive'
        elif predicted_class == 3:
            sentiment_class = 'Neutral'
        elif predicted_class == 2:
            sentiment_class = 'Negative'
        elif predicted_class == 1:
            sentiment_class = 'Strong Negative'
        else:
            sentiment_class = 'Unknown'  # Handle unexpected class values

        context = {
            'class': sentiment_class,
        }
        return render(request, 'sentiment_analysis_api/analyze_sentiment.html', context)
    else:
        return render(request, 'sentiment_analysis_api/analyze_sentiment.html')

@api_view(['POST','GET'])    
def home(request):
    return render(request, 'sentiment_analysis_api/home.html')

def info(request):
    return render(request, 'sentiment_analysis_api/info.html')
