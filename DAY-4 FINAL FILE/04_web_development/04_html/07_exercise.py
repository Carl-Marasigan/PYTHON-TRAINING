"""
Task: "Guess the Secret Word!"

In this task, you will create a small web application using Flask where users have to guess a secret word.
The application will display a form where users can enter their guess.
Upon submission, the application will check if the guess matches the secret word and return an appropriate response.
    - If the guess is correct, a success message will be shown.
    - If the guess is incorrect, an error message will be displayed, prompting the user to try again.

This exercise helps students practice:

    Form handling in Flask: Understanding how to accept user input via forms and use that input in server-side logic.
    Conditional logic: Using if-statements to check if the user's guess matches the secret word.
    Providing feedback: Giving users clear, immediate feedback based on their input (correct or incorrect).
"""


# from flask import Flask, request
#
# app = Flask(__name__)
#
# # The secret word to guess
# SECRET_WORD = "inventive"
#
#
# @app.route("/", methods=["GET", "POST"])
# def guess_game():
#     message = ""
#
#
#     if request.method == "POST":
#
#         user_guess = request.form.get("user_guess", "").strip().lower()
#
#         #
#         if user_guess == SECRET_WORD:
#             message = "<p>🎉May tama ka!</p>"
#         else:
#             message = "<p>❌ Mali ulitin mo uli!.</p>"
#
#     # Simple HTML form displayed to the user
#     html_form = f"""
#     <h1>Guess the Secret Word!</h1>
#     {message}
#     <form method="POST">
#         <label>Enter your guess: </label>
#         <input type="text" name="user_guess" required>
#         <button type="submit">Submit</button>
#     </form>
#     """
#     return html_form
#
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

# The secret word to guess
SECRET_WORD = "inventive"


@app.route("/", methods=["GET", "POST"])
def guess_game():
    message = ""

    if request.method == "POST":
        user_guess = request.form.get("user_guess", "").strip().lower()

        if user_guess == SECRET_WORD:
            message = '<p class="message success">🎉 May tama ka!</p>'
        else:
            message = '<p class="message error">❌ Mali, ulitin mo uli!</p>'

    # Updated CSS to a crisp Ocean/Royal Blue theme
    html_form = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Guess the Secret Word!</title>
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            body {{
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .card {{
                background: white;
                padding: 2.5rem;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
                width: 100%;
                max-width: 400px;
                text-align: center;
            }}
            h1 {{
                color: #1e3c72;
                font-size: 1.8rem;
                margin-bottom: 1.5rem;
            }}
            .form-group {{
                margin-bottom: 1.5rem;
                text-align: left;
            }}
            label {{
                display: block;
                color: #555;
                font-size: 0.9rem;
                margin-bottom: 0.5rem;
                font-weight: 600;
            }}
            input[type="text"] {{
                width: 100%;
                padding: 0.75rem;
                border: 2px solid #ced4da;
                border-radius: 8px;
                font-size: 1rem;
                transition: border-color 0.3s, box-shadow 0.3s;
            }}
            input[type="text"]:focus {{
                border-color: #2a5298;
                box-shadow: 0 0 0 3px rgba(42, 82, 152, 0.25);
                outline: none;
            }}
            button {{
                width: 100%;
                background: #1e3c72;
                color: white;
                border: none;
                padding: 0.75rem;
                font-size: 1rem;
                font-weight: bold;
                border-radius: 8px;
                cursor: pointer;
                transition: background 0.3s, transform 0.1s;
            }}
            button:hover {{
                background: #162a50;
            }}
            button:active {{
                transform: scale(0.98);
            }}
            .message {{
                padding: 0.75rem;
                border-radius: 8px;
                margin-bottom: 1.5rem;
                font-weight: 500;
                font-size: 0.95rem;
            }}
            .success {{
                background-color: #e6fffa;
                color: #00875a;
                border: 1px solid #b2f5ea;
            }}
            .error {{
                background-color: #fff5f5;
                color: #e53e3e;
                border: 1px solid #fed7d7;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Guess the Secret Word!</h1>
            {message}
            <form method="POST">
                <div class="form-group">
                    <label for="guess">Enter your guess:</label>
                    <input type="text" id="guess" name="user_guess" placeholder="Type here..." required autocomplete="off">
                </div>
                <button type="submit">Submit Guess</button>
            </form>
        </div>
    </body>
    </html>
    """
    return html_form


if __name__ == "__main__":
    app.run(debug=True)