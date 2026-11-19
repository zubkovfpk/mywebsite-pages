# -*- coding: utf-8 -*-
import math

def radar_svg(labels, current, required, na_label, aria):
    W, H, cx, cy, R = 500, 400, 250, 198, 140
    n = len(labels)
    def pt(i, v):
        a = -math.pi / 2 + 2 * math.pi * i / n
        return cx + R * v / 4 * math.cos(a), cy + R * v / 4 * math.sin(a)
    s = [f'<svg class="radar" viewBox="0 0 {W} {H}" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">']
    for lv in range(1, 5):
        pts = ' '.join('%.1f,%.1f' % pt(i, lv) for i in range(n))
        s.append(f'<polygon points="{pts}" fill="none" stroke="#DFD8C9" stroke-width="1"/>')
        x, y = pt(0, lv)
        s.append(f'<text x="{x + 5:.1f}" y="{y + 4:.1f}" font-size="10" fill="#8B857A" font-family="Segoe UI, Arial, sans-serif">{lv}</text>')
    for i in range(n):
        x, y = pt(i, 4)
        s.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#DFD8C9" stroke-width="1"/>')
    req = ' '.join('%.1f,%.1f' % pt(i, v) for i, v in enumerate(required))
    s.append(f'<polygon points="{req}" fill="rgba(169,116,15,.07)" stroke="#A9740F" stroke-width="1.6" stroke-dasharray="5 4"/>')
    # current profile: broken at unknown values, never interpolated
    for i in range(n):
        j = (i + 1) % n
        if current[i] is not None and current[j] is not None:
            (x1, y1), (x2, y2) = pt(i, current[i]), pt(j, current[j])
            s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#0F5A46" stroke-width="2.4"/>')
    for i, v in enumerate(current):
        if v is not None:
            x, y = pt(i, v)
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#0F5A46"/>')
    for i, lab in enumerate(labels):
        a = -math.pi / 2 + 2 * math.pi * i / n
        c = math.cos(a)
        x, y = cx + (R + 16) * c, cy + (R + 16) * math.sin(a) + 4
        anchor = 'middle' if abs(c) < 0.3 else ('start' if c > 0 else 'end')
        missing = current[i] is None
        fill = '#B3402E' if missing else '#1C1B18'
        extra = f'<tspan x="{x:.1f}" dy="15" font-size="11" fill="#B3402E" font-family="Segoe UI, Arial, sans-serif">{na_label}</tspan>' if missing else ''
        s.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="13" fill="{fill}" font-family="-apple-system,Segoe UI,Arial,sans-serif">{lab}{extra}</text>')
    s.append('</svg>')
    return ''.join(s)
