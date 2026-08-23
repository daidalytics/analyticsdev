#!/usr/bin/env python3
"""Rasterise the AnalyticsDev mark into favicon.ico and apple-touch-icon.png.

The mark is two monospace slashes carrying the wordmark's weight break:
a hairline "Analytics" slash and a bold "Dev" slash on the site's ink.

assets/favicon.svg is the source of truth for the shape. The geometry below
mirrors it. If you change one, change both and re-run:

    python3 tools/render-favicon.py

No third-party packages needed — PNG and ICO are written by hand.
"""
import os
import struct
import zlib

# --- Colours, from the site tokens in css/style.css, lifted for a dark ground
INK = (0x11, 0x18, 0x27)      # --color-text
LIGHT = (0xC7, 0xCD, 0xD6)    # between --color-border and --color-text-muted
GREEN = (0x2F, 0xB3, 0x5F)    # --color-accent-hl (#15803d), same hue, lifted

# --- Geometry, in the 32x32 design space shared with assets/favicon.svg
SIZE = 32.0
RADIUS = 7.0
LIGHT_SLASH = [(4.75, 26), (11.75, 6), (15, 6), (8, 26)]
BOLD_SLASH = [(14, 26), (21, 6), (27.25, 6), (20.25, 26)]

SUPERSAMPLE = 4               # samples per axis, per pixel

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def in_round_rect(x, y):
    if not (0 <= x <= SIZE and 0 <= y <= SIZE):
        return False
    cx = min(max(x, RADIUS), SIZE - RADIUS)
    cy = min(max(y, RADIUS), SIZE - RADIUS)
    dx, dy = x - cx, y - cy
    return dx * dx + dy * dy <= RADIUS * RADIUS


def in_poly(x, y, poly):
    """Point in convex polygon: every edge cross-product shares a sign."""
    sign = 0
    for i in range(len(poly)):
        ax, ay = poly[i]
        bx, by = poly[(i + 1) % len(poly)]
        cross = (bx - ax) * (y - ay) - (by - ay) * (x - ax)
        if cross == 0:
            continue
        s = 1 if cross > 0 else -1
        if sign == 0:
            sign = s
        elif s != sign:
            return False
    return True


def sample(x, y, opaque):
    if in_poly(x, y, LIGHT_SLASH):
        return LIGHT + (255,)
    if in_poly(x, y, BOLD_SLASH):
        return GREEN + (255,)
    if opaque or in_round_rect(x, y):
        return INK + (255,)
    return (0, 0, 0, 0)


def render(size, opaque=False):
    """Supersampled RGBA rows. opaque skips the rounded mask — iOS masks its own."""
    step = (SIZE / size) / SUPERSAMPLE
    total = SUPERSAMPLE * SUPERSAMPLE
    rows = []
    for py in range(size):
        row = bytearray()
        for px in range(size):
            ar = ag = ab = aa = 0
            for sy in range(SUPERSAMPLE):
                y = (py * SUPERSAMPLE + sy + 0.5) * step
                for sx in range(SUPERSAMPLE):
                    x = (px * SUPERSAMPLE + sx + 0.5) * step
                    r, g, b, a = sample(x, y, opaque)
                    # premultiplied, so the rounded tile edge antialiases cleanly
                    ar += r * a
                    ag += g * a
                    ab += b * a
                    aa += a
            if aa == 0:
                row += b"\0\0\0\0"
            else:
                row += bytes((round(ar / aa), round(ag / aa),
                              round(ab / aa), round(aa / total)))
        rows.append(bytes(row))
    return rows


def png(rows, size):
    def chunk(tag, data):
        body = tag + data
        return (struct.pack(">I", len(data)) + body
                + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF))

    raw = b"".join(b"\0" + row for row in rows)   # filter type 0 per row
    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9))
            + chunk(b"IEND", b""))


def ico(entries):
    """ICO holding PNG-compressed images — read by every current browser."""
    header = struct.pack("<HHH", 0, 1, len(entries))
    offset = 6 + 16 * len(entries)
    directory = b""
    body = b""
    for size, data in entries:
        directory += struct.pack("<BBBBHHII", size % 256, size % 256, 0, 0,
                                 1, 32, len(data), offset)
        offset += len(data)
        body += data
    return header + directory + body


def main():
    entries = [(s, png(render(s), s)) for s in (16, 32, 48)]
    with open(os.path.join(ROOT, "favicon.ico"), "wb") as f:
        f.write(ico(entries))
    with open(os.path.join(ROOT, "assets", "apple-touch-icon.png"), "wb") as f:
        f.write(png(render(180, opaque=True), 180))
    print("wrote favicon.ico (16/32/48) and assets/apple-touch-icon.png (180)")


if __name__ == "__main__":
    main()
