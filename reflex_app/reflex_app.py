"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

# docs_url = "https://reflex.dev/docs/getting-started/introduction/"
# filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1rem"
    )

def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!"
        ),
        (
            "What can I make with it?",
            "Anything from a simple "
        )
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )


def index() -> rx.Component:
    return rx.container(
        rx.box(
            "What is Reflex?",
            # The user's question is on the right.
            text_align="right",
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            # The answer is on the left.
            text_align="left",
        ),
    )


app = rx.App()
app.add_page(index)
