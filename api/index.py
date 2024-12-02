from flask import Flask

app = Flask(__name__)

site = """
<html data-darkreader-proxy-injected="true"><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">#[derive(Debug)]
struct Url(&'static str);

#[derive(Debug)]
struct StackInfo {
    name: &'static str,
    version: f32,
    url: Url,
}

#[derive(Debug)]
struct Links {
    github: (&'static str, Url),
    discord: (&'static str, Url),
}

#[derive(Debug)]
struct Stack {
    langs: Vec<StackInfo>,
    frameworks: Vec<StackInfo>,
    os: Vec<StackInfo>,
    /// String - Other "Type"
    other: Vec<(StackInfo, &'static str)>,
}

#[derive(Debug)]
struct Me {
    nick: &'static str,
    avatar: &'static str,
    about: &'static str,
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
            about: "I'm a Developer specialized in Web (backend) development. I'm also learning             Rust and F#.",
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
}</pre></body></html>
"""

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return site
