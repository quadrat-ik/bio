from flask import Flask, render_template_string

app = Flask(__name__)

site = """
```rs
#[derive(Debug)]
struct Url(&amp;'static str);

#[derive(Debug)]
struct StackInfo {
    name: &amp;'static str,
    version: f32,
    url: Url,
}

#[derive(Debug)]
struct Links {
    github: (&amp;'static str, Url),
    discord: (&amp;'static str, Url),
}

#[derive(Debug)]
struct Stack {
    langs: Vec&lt;StackInfo&gt;,
    frameworks: Vec&lt;StackInfo&gt;,
    os: Vec&lt;StackInfo&gt;,
    /// String - Other "Type"
    other: Vec&lt;(StackInfo, &amp;'static str)&gt;,
}

#[derive(Debug)]
struct Me {
    nick: &amp;'static str,
    avatar: &amp;'static str,
    about: &amp;'static str,
}

#[derive(Debug)]
struct Info {
    me: Me,
    links: Links,
    stack: Stack,
    projects: Option<(&'static str, (Stack, Url))>,
}

fn main() {
    let info: Info = Info {
        me: Me {
            nick: "MeSSengeR.qs",
            avatar: "https://cdn.discordapp.com/avatars/1140982742100746260/115bd7f5b63b0c0dad5f502cf873a6dc?size=2048",
            about: "I'm a Developer specialized in Web (backend) development. I'm also learning Rust and F#.",
        },
        links: Links {
            github: (
                "messenger.qs",
                Url("https://discord.andcool.ru/1140982742100746260"),
            ),
            discord: ("quadrat-ik", Url("https://github.com/quadrat-ik")),
        },
        stack: Stack {
            langs: vec![
                StackInfo {
                    name: "rust",
                    version: 1.85,
                    url: Url("https://rust-lang.org/"),
                },
                StackInfo {
                    name: "zig",
                    version: 0.13,
                    url: Url("https://ziglang.org/"),
                },
                StackInfo {
                    name: "F#",
                    version: 12.9,
                    url: Url("https://fsharp.org/"),
                },
            ],
            frameworks: vec![StackInfo {
                name: "actix",
                version: 4.9,
                url: Url("https://actix.rs/"),
            }],
            os: vec![StackInfo {
                name: "ArchLinux",
                version: 1_12.2024,
                url: Url("https://actix.rs/"),
            }],
            other: vec![(
                StackInfo {
                    name: "RustRover",
                    version: 2024.2_5,
                    url: Url("https://jetbrains.com/rust/"),
                },
                "IDE",
            )],
        },
        projects: None,
    };

    println!("{:?}", info)
}
```
"""

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template_string(f"""<html lang='en'>
    <head>
        <title>mSSr</title>
        <link href="https://cdn.jsdelivr.net/npm/github-markdown-css/github-markdown-light.css" rel="stylesheet">
        <style>
            body {{
                margin: 2rem;
                font-family: sans-serif;
            }}
            .markdown-body {{
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                padding: 2rem;
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>
        <article class="markdown-body">{site}</article>
    </body>
    </html>""")
