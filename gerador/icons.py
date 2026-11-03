"""Line icons (24x24, stroke=currentColor) used by both templates."""

_P = {
    "shield": '<path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
    "broom": '<path d="M14 3l-4 9"/><path d="M6 13h8l2 8H4z"/><path d="M8 17v4M12 17v4"/>',
    "sparkle": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 15l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
    "lang": '<path d="M4 5h8M8 3v2M6 5c0 4 3 7 6 8M10 5c-1 4-4 7-6 8"/><path d="M13 21l4-9 4 9M14.5 18h5"/>',
    "bed": '<path d="M3 18V7"/><path d="M3 14h18v4"/><path d="M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="2"/>',
    "bath": '<path d="M4 12h16v3a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4z"/><path d="M6 12V6a2 2 0 0 1 4 0"/><path d="M7 19l-1 2M17 19l1 2"/>',
    "pool": '<path d="M2 18c2 0 2-1.5 4-1.5S8 18 10 18s2-1.5 4-1.5 2 1.5 4 1.5 2-1.5 4-1.5"/><path d="M8 14V5a2 2 0 0 1 4 0"/><path d="M16 14V5a2 2 0 0 0-4 0"/><path d="M8 8h8M8 11h8"/>',
    "coffee": '<path d="M4 9h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M17 10h1.5a2.5 2.5 0 0 1 0 5H17"/><path d="M8 3c0 1 1 1 1 2s-1 1-1 2M12 3c0 1 1 1 1 2s-1 1-1 2"/>',
    "wifi": '<path d="M2 9a15 15 0 0 1 20 0"/><path d="M5 12.5a10 10 0 0 1 14 0"/><path d="M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19" r="1"/>',
    "car": '<path d="M5 16h14v-4l-2-5H7l-2 5z"/><path d="M5 16v2M19 16v2"/><circle cx="8" cy="13" r="1"/><circle cx="16" cy="13" r="1"/>',
    "paw": '<circle cx="6" cy="10" r="1.6"/><circle cx="10" cy="6" r="1.6"/><circle cx="14" cy="6" r="1.6"/><circle cx="18" cy="10" r="1.6"/><path d="M8 17c0-3 2-5 4-5s4 2 4 5a2 2 0 0 1-2 2c-1 0-1.3-.6-2-.6s-1 .6-2 .6a2 2 0 0 1-2-2z"/>',
    "wave": '<path d="M2 12c2 0 2-2 4-2s2 2 4 2 2-2 4-2 2 2 4 2 2-2 4-2"/><path d="M2 17c2 0 2-2 4-2s2 2 4 2 2-2 4-2 2 2 4 2 2-2 4-2"/><path d="M2 7c2 0 2-2 4-2s2 2 4 2 2-2 4-2 2 2 4 2 2-2 4-2"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "leaf": '<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19l8-8"/>',
    "plane": '<path d="M10 14l-7-3 1.5-1.5 7.5 1 4-4.5a2 2 0 0 1 3 3L14.5 13l1 7.5L14 22l-3-7z"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8"/>',
    "facebook": '<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8z"/>',
    "whatsapp": '<path d="M4 20l1.3-4A8 8 0 1 1 8 18.7z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 .8a4 4 0 0 1-2-2l.8-1-1-2z"/>',
    "snow": '<path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7"/><path d="M9 4l3 2 3-2M9 20l3-2 3 2"/>',
    "tv": '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "kitchen": '<path d="M6 3v8M4 3v4a2 2 0 0 0 4 0V3M6 11v10"/><path d="M17 21V3c-2 1-3 4-3 7h3"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
    "area": '<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    "fish": '<path d="M3 12c3-4 7-5 10-5 4 0 6 2.5 8 5-2 2.5-4 5-8 5-3 0-7-1-10-5z"/><path d="M3 12l-1-3M3 12l-1 3"/><circle cx="16" cy="11" r=".8"/>',
    "kite": '<path d="M12 2l6 7-6 8-6-8z"/><path d="M12 17c0 2 1 3 2 4M6 9h12M12 2v15"/>',
    "boat": '<path d="M3 15h18l-2 4H5z"/><path d="M12 15V3l6 9h-6"/><path d="M12 6l-5 6h5"/>',
    "hike": '<path d="M3 20l6-10 4 6 3-4 5 8z"/><circle cx="17" cy="6" r="2"/>',
    "food": '<circle cx="12" cy="13" r="6"/><path d="M12 10v6M9 13h6"/><path d="M4 3v6M20 3v6"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "chev": '<path d="M9 6l6 6-6 6"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "check": '<path d="M5 12l5 5 9-10"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "shell": '<path d="M12 20c-5 0-8-4-8-8a8 8 0 0 1 16 0c0 4-3 8-8 8z"/><path d="M12 20V6M8 19l2-12M16 19l-2-12M5 15l5-8M19 15l-5-8"/>',
    "lagoon": '<path d="M2 17c3-1 5 1 8 0s5-1 7 0 3 1 5 0"/><path d="M5 13c1-4 3-6 5-6s3 2 4 3 2 1 3 0"/><circle cx="18" cy="6" r="2"/>',
    "board": '<path d="M7 21c-2-4-2-12 5-19 7 7 7 15 5 19z"/><path d="M12 2v19"/>',
    "parking": '<rect x="4" y="3" width="16" height="18" rx="3"/><path d="M10 17V7h3a3 3 0 0 1 0 6h-3"/>',
    "heart": '<path d="M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.5A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M15 8l2 2"/>',
    "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
    "quote":'<path d="M7 7h4v4c0 3-1.5 5-4 6M13 7h4v4c0 3-1.5 5-4 6"/>',
}


def icon(name, size=20, sw=1.4, cls="ico"):
    p = _P.get(name, _P["star"])
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>')


def star_fill(n=5, size=14):
    one = (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" '
           'd="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></svg>')
    return one * n
