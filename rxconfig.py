import reflex as rx

class AppConfig(rx.Config):
    pass

config = rx.Config(
    app_name="reflex_app",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)