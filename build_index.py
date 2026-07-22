import os

with open("assets/cheezh.svg", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Lines 3 to 91 cover the defs and all paths, skipping the <?xml> and <svg> wrapper lines
svg_content = "".join(lines[3:-1])
# Insert the <g id="all-fruits"> wrapper
svg_content = svg_content.replace('</defs>', '</defs>\n<g id="all-fruits">')
svg_content += "\n</g>"

html = f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chezh - LinkTree</title>
    <link rel="stylesheet" href="style.css">
    <!-- Phosphor Icons -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
</head>
<body>
    <!-- Background Illustrations mapped to responsive corners -->
    <div class="bg-container">
        <svg style="display: none;">
            {svg_content}
        </svg>

        <svg class="bg-corner tl" viewBox="0 0 540 928">
            <use href="#all-fruits" />
        </svg>
        <svg class="bg-corner tr" viewBox="540 0 540 928">
            <use href="#all-fruits" />
        </svg>
        <svg class="bg-corner bl" viewBox="0 928 540 928">
            <use href="#all-fruits" />
        </svg>
        <svg class="bg-corner br" viewBox="540 928 540 928">
            <use href="#all-fruits" />
        </svg>
    </div>

    <!-- Main Content -->
    <main class="container">
        <header class="header">
            <img src="assets/logo.PNG" alt="Chezh Logo" class="logo">
        </header>

        <nav class="links">
            <a href="#" class="link-item">
                <i class="ph ph-whatsapp-logo link-icon"></i>
                <span class="link-text">WhatsApp</span>
                <i class="ph ph-arrow-right link-arrow"></i>
            </a>
            
            <a href="#" class="link-item">
                <i class="ph ph-instagram-logo link-icon"></i>
                <span class="link-text">Instagram</span>
                <i class="ph ph-arrow-right link-arrow"></i>
            </a>
            
            <a href="#" class="link-item">
                <i class="ph ph-ghost link-icon"></i>
                <span class="link-text">Snapchat</span>
                <i class="ph ph-arrow-right link-arrow"></i>
            </a>
            
            <a href="#" class="link-item">
                <i class="ph ph-tiktok-logo link-icon"></i>
                <span class="link-text">TikTok</span>
                <i class="ph ph-arrow-right link-arrow"></i>
            </a>
            
            <a href="#" class="link-item">
                <i class="ph ph-facebook-logo link-icon"></i>
                <span class="link-text">Facebook</span>
                <i class="ph ph-arrow-right link-arrow"></i>
            </a>
            
            <a href="#" class="link-item">
                <i class="ph ph-phone link-icon"></i>
                <span class="link-text">Call Us</span>
                <i class="ph ph-arrow-right link-arrow"></i>
            </a>
        </nav>
    </main>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
