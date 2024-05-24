## Flask Application Design

### HTML Files
The application will require two HTML files:

- `index.html`: This file will serve as the homepage of the application, displaying a list of recent news articles. It will include a header, a main section, and a footer. The main section will contain the news articles, which will be dynamically generated using Flask.
- `article.html`: This file will display the details of a specific news article. It will include a header, a main section, and a footer. The main section will contain the title, author, content, and publication date of the article.

### Routes
The application will require three routes:

- `/`: This route will handle the homepage of the application. It will retrieve the list of recent news articles from a data source (e.g., an API or a database) and render the `index.html` template, passing the list of articles to the template as a variable.
- `/article/<id>`: This route will handle the display of a specific news article. It will retrieve the article with the specified `id` from a data source (e.g., an API or a database) and render the `article.html` template, passing the article to the template as a variable.
- `/about`: This route will handle the display of an about page for the application. It will render an `about.html` template, which will include information about the application and its creators.