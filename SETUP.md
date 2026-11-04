# Areeb-coder profile README — revised

## What's changed
- Removed the entire **GitHub telemetry** section and its stats, stack, and portrait cards.
- Moved the animated pixel-art room to the very top of the README.
- The room GIF uses a fixed camera: no zoom, scale, or pan. Only ambient screen refresh, cursor, rain, cup steam, and a small PC status light move.
- Moved the Areeb-coder terminal wordmark directly below the room animation.
- Rewrote the terminal tagline around general development interests; it does not position chess engines as your main identity.
- Kept one contribution-city image as a separate visual section, generated from public GitHub contribution activity.
- Rebuilt the clickable KnightForge chessboard preview using the live game's palette: background #0b1118, light squares #d7e2dc, dark squares #547565, white pieces #ffffff, and dark pieces #17231f.

## Install
The special profile repository is `Areeb-coder/Areeb-coder`. The files in this package mirror its root README and `assets/` folder. Keep the folder names unchanged.

## KnightForge
The board preview links to https://areeb-coder.github.io/KnightForge/. The live game is a separate page because GitHub profile READMEs render images and links, not embedded JavaScript games. Enable **Settings → Pages → Build and deployment → Source → GitHub Actions** in KnightForge, then run its build/deploy workflow.

## Animated room
The included GIF is a 16-frame, 640×360 loop. It uses the original room's first frame with subtle ambient movement. In the repository, `.github/workflows/refresh-coder-room.yml` regenerates the GIF from its existing first frame whenever this README/animation workflow is updated.
