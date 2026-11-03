"""Hand-drawn style line art for the Aurelia template backgrounds + simple logo marks."""


def _palm(x, y, s=1.0, lean=0.0):
    # trunk + 7 fronds, drawn as quadratic curves
    tx, ty = x + 40 * lean * s, y - 210 * s
    parts = [f'<path d="M{x} {y} Q{x + 18*lean*s + 6*s} {y - 110*s} {tx} {ty}"/>',
             f'<path d="M{x+7*s} {y} Q{x + 22*lean*s + 12*s} {y - 110*s} {tx+5*s} {ty+4*s}"/>']
    for i in range(6):
        parts.append(f'<path d="M{x+3*s} {y - (20 + i*30)*s} l{9*s} {-4*s}"/>')
    fr = [(-120, 30), (-95, -18), (-45, -50), (10, -58), (70, -30), (115, 20), (130, 70), (-130, 85)]
    for dx, dy in fr:
        ex, ey = tx + dx * s, ty + dy * s + 40 * s
        cx, cy = tx + dx * 0.45 * s, ty + (dy - 55) * s
        parts.append(f'<path d="M{tx} {ty} Q{cx} {cy} {ex} {ey}"/>')
        # leaflets
        for k in range(1, 6):
            t = k / 6
            px = (1-t)**2*tx + 2*(1-t)*t*cx + t*t*ex
            py = (1-t)**2*ty + 2*(1-t)*t*cy + t*t*ey
            parts.append(f'<path d="M{px:.0f} {py:.0f} l{(4 if dx>0 else -4)*s:.0f} {16*s:.0f}"/>')
    return ''.join(parts)


def deco(variant='a'):
    if variant == 'a':
        body = (_palm(80, 760, 1.25, -.4) + _palm(190, 790, .85, .3) +
                _palm(1400, 720, 1.1, .35) + _palm(1300, 800, .7, -.2) +
                '<path d="M0 800 Q220 690 420 760 T820 740 T1200 770 T1600 720"/>'
                '<path d="M0 840 Q260 780 520 820 T1040 800 T1600 790"/>'
                '<path d="M560 330 Q700 260 860 310 T1120 300"/><path d="M600 350 q40 -14 80 0 t80 0"/>')
        return (f'<svg class="deco" style="inset:auto 0 0 0;width:100%;height:auto" viewBox="0 0 1600 860" '
                f'fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" aria-hidden="true">{body}</svg>')
    body = (_palm(120, 900, 1.6, -.25) + _palm(1460, 880, 1.4, .3) +
            '<path d="M0 880 Q400 820 800 860 T1600 840"/>')
    return (f'<svg class="deco" style="inset:auto 0 0 0;width:100%;height:auto" viewBox="0 0 1600 940" '
            f'fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" aria-hidden="true">{body}</svg>')


LOGOS = {
    # 28px marks in the spirit of the Aurelia lotus — one per pousada
    'wave': '<path d="M3 17c3 0 3-2.5 6-2.5s3 2.5 6 2.5 3-2.5 6-2.5"/><path d="M5 12.5c1.5-4 4-6.5 7-6.5 2.5 0 4.5 1.6 5 4-1.6-1-3.6-.8-4.8.6"/><circle cx="12" cy="4" r="1"/>',
    'plane': '<path d="M3 15.5l18-6.5-3.5 9-5-2.5-3 3v-4l8-6.5-10 4.5z"/><path d="M3 20h18" opacity=".6"/>',
    'anchor': '<circle cx="12" cy="5" r="2"/><path d="M12 7v13"/><path d="M8 10h8"/><path d="M4 14c0 4 4 6 8 6s8-2 8-6"/><path d="M4 14l-1.5 2M20 14l1.5 2"/>',
    'wing': '<ellipse cx="12" cy="4" rx="4" ry="1.3"/><path d="M12 20c-1.5-3-2-6-1-9"/><path d="M11 11c-2.5-2.5-6-3-8-2 1 3 3.5 5.5 7 5"/><path d="M13 11c2.5-2.5 6-3 8-2-1 3-3.5 5.5-7 5"/><path d="M12 20c1.5-3 2-6 1-9" opacity=".6"/>',
    'palm': '<path d="M12 21V9"/><path d="M12 9c-1-3-4-5-8-5 1 4 4 6 8 5zM12 9c1-3 4-5 8-5-1 4-4 6-8 5z"/><path d="M12 13c-2-1.5-5-1.5-7 0 2 2 5 2 7 0zM12 13c2-1.5 5-1.5 7 0-2 2-5 2-7 0z" opacity=".7"/>',
    'hibiscus': '<circle cx="12" cy="12" r="2"/><path d="M12 10c-1-4 0-7 0-7s1 3 0 7zM14 12c4-1 7 0 7 0s-3 1-7 0zM12 14c1 4 0 7 0 7s-1-3 0-7zM10 12c-4 1-7 0-7 0s3-1 7 0z"/><path d="M13.5 10.5c2-3 5-4 5-4s-1 3-5 4zM10.5 13.5c-2 3-5 4-5 4s1-3 5-4zM13.5 13.5c3 2 4 5 4 5s-3-1-4-5zM10.5 10.5c-3-2-4-5-4-5s3 1 4 5z" opacity=".7"/>',
}


def logo(name, size=30):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{LOGOS[name]}</svg>')
