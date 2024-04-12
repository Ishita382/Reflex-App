import reflex as rx

class AppConfig(rx.Config):
    pass

config = rx.Config(
    app_name="reflex_app",
    db_url="sqlite:///reflex.db",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)