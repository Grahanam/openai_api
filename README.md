# OpenAI API - Emojify Movie Name

Emojify Movie Name is a fun web application that generates emoji-based representations of movie titles.
It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework.Follow the instructions below to get set up.


## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd openai_api
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)!

## Testing

1. Run the tests.py: 
   ```bash
   $ python -m unittest tests.py
   ```
