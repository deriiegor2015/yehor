from contacts import add_contact

@app.route("/voice", methods=["POST"])
def voice():
    user_text = request.form.get("SpeechResult", "Привіт")
    caller_number = request.form.get("From")  # Twilio передає номер того, хто дзвонить

    # Записуємо номер після дзвінка
    add_contact("Новий контакт", caller_number)

    # Виклик OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_text}]
    )
    ai_reply = response.choices[0].message["content"]

    twiml = f"""
    <Response>
        <Say language="uk-UA">{ai_reply}</Say>
    </Response>
    """
    return Response(twiml, mimetype="text/xml")