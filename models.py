"""
Define Anki models for Swahili vocabulary
"""

import genanki

STYLE = """
.card {
  font-family: arial;
  font-size: 24px;
  text-align: center;
  color: black;
  background-color: white;
}

.cloze {
  font-weight: bold;
  color: blue;
}
"""

VOCAB_REVERSE = genanki.Model(
    1325469472,
    "TEST Swahili vocabulary note",
    fields=[
        {
            "name": "Swahili",
        },
        {
            "name": "English",
        },
    ],
    templates=[
        {
            "name": "Vocabulary Card (front)",
            "qfmt": "{{Swahili}}",
            "afmt": "{{FrontSide}}<hr id=\"answer\">{{English}}",
        },
        {
            "name": "Vocabulary Card (back)",
            "qfmt": "{{English}}",
            "afmt": "{{FrontSide}}<hr id=\"answer\">{{Swahili}}",
        },
    ],
    css=STYLE,
)


VOCAB_REVERSE2 = genanki.Model(
    1325469472,
    "TEST Swahili vocabulary note",
    fields=[
        {
            "name": "Swahili",
        },
        {
            "name": "English",
        },
        {
            "name": "Audio",
        },
    ],
    templates=[
        {
            "name": "Vocabulary Card (front)",
            "qfmt": "{{Swahili}}<br />{{Audio}}",
            "afmt": "{{FrontSide}}<hr id=\"answer\">{{English}}",
        },
        {
            "name": "Vocabulary Card (back)",
            "qfmt": "{{English}}",
            "afmt": "{{FrontSide}}<hr id=\"answer\">{{Swahili}}<br />{{Audio}}",
        },
    ],
    css=STYLE,
)
