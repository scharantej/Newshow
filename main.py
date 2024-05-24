
# Import the necessary modules.
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance.
app = Flask(__name__)

# define the main route
@app.route('/')
def index():
    # Retrieve the list of recent news articles from the API.
    news_articles = get_news_articles()
    # Render the index.html template, passing the list of articles to the template.
    return render_template('index.html', articles=news_articles)

# Define the route to display a specific news article.
@app.route('/article/<id>')
def article(id):
    # Retrieve the article with the specified id from the API.
    article = get_news_article(id)
    # Render the article.html template, passing the article to the template.
    return render_template('article.html', article=article)

# Define the route to display the about page.
@app.route('/about')
def about():
    # Render the about.html template.
    return render_template('about.html')

# Start the Flask application.
if __name__ == '__main__':
    app.run(debug=True)
